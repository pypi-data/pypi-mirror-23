from pathlib import Path
import numpy as np
import os
import warnings
import copy

from NeuNorm.loader import load_hdf, load_tiff, load_fits
from NeuNorm.roi import ROI
from NeuNorm._utilities import get_sorted_list_images, average_df

class Normalization(object):

    def __init__(self):
        self.shape = {'width': np.NaN,
                      'height': np.NaN}
        self.dict_image = { 'data': [],
                            'oscilation': [],
                            'file_name': [],
                            'shape': self.shape.copy()}
        self.dict_ob = {'data': [],
                        'oscilation': [],
                        'file_name': [],
                        'shape': self.shape.copy()}
        self.dict_df = {'data': [],
                        'data_average': [],
                        'file_name': [],
                        'shape': self.shape.copy()}

        __roi_dict = {'x0': np.NaN,
                      'x1': np.NaN,
                      'y0': np.NaN,
                      'y1': np.NaN}
        self.roi = {'normalization': __roi_dict.copy(),
                    'crop': __roi_dict.copy()}

        self.__exec_process_status = {'df_correction': False,
                                      'normalization': False,
                                      'crop': False,
                                      'oscillation': False,
                                      'bin': False}

        self.data = {}
        self.data['sample'] = self.dict_image
        self.data['ob'] = self.dict_ob
        self.data['df'] = self.dict_df
        self.data['normalized'] = []
    
    def load(self, file='', folder='', data_type='sample'):
        '''
        Function to read individual files or entire files from folder specify for the given
        data type
        
        Parameters:
           file: full path to file
           folder: full path to folder containing files to load
           data_type: ['sample', 'ob', 'df]

        Algorithm won't be allowed to run if any of the main algorithm have been run already, such as
        oscillation, crop, binning, df_correction.

        '''
        list_exec_flag = [_flag for _flag in self.__exec_process_status.values()]
        if True in list_exec_flag:
            raise IOError("Operation not allowed as you already worked on this data set!")
        
        if not file == '':
            self.load_file(file=file, data_type=data_type)
        
        if not folder == '':
            # load all files from folder
            list_images = get_sorted_list_images(folder=folder)
            for _image in list_images:
                full_path_image = os.path.join(folder, _image)
                self.load_file(file=full_path_image, data_type=data_type)
        
    def load_file(self, file='', data_type='sample'):
        """
        Function to read data from the specified path, it can read FITS, TIFF and HDF.
    
        Parameters
        ----------
        file : string_like
            Path of the input file with his extention.
        data_type: ['sample', 'df']
    
        Notes
        -----
        In case of corrupted header it skips the header and reads the raw data.
        For the HDF format you need to specify the hierarchy.
        """
    
        my_file = Path(file)
        if my_file.is_file():
            data = []
            if file.lower().endswith('.fits'):
                data = load_fits(my_file)
            elif file.lower().endswith(('.tiff','.tif')) :
                data = load_tiff(my_file)
            elif file.lower().endswith(('.hdf','.h4','.hdf4','.he2','h5','.hdf5','.he5')): 
                data = load_hdf(my_file)
            else:
                raise OSError('file extension not yet implemented....Do it your own way!')     

            self.data[data_type]['data'].append(data)
            self.data[data_type]['file_name'].append(file)
            self.save_or_check_shape(data=data, data_type=data_type)

        else:
            raise OSError("The file name does not exist")

    def save_or_check_shape(self, data=[], data_type='sample'):
        '''save the shape for the first data loaded (of each type) otherwise
        check the size match
    
        Raises:
        IOError if size do not match
        '''
        [height, width] = np.shape(data)
        if np.isnan(self.data[data_type]['shape']['height']):
            _shape = self.shape.copy()
            _shape['height'] = height
            _shape['width'] = width
            self.data[data_type]['shape'] = _shape
        else:
            _prev_width = self.data[data_type]['shape']['width']
            _prev_height = self.data[data_type]['shape']['height']
            
            if (not (_prev_width == width)) or (not (_prev_height == height)):
                raise IOError("Shape of {} do not match previous loaded data set!".format(data_type))

    def normalization(self, roi=None, force=False):
        '''normalization of the data 
                
        Parameters:
        ===========
        roi: ROI object that defines the region of the sample and OB that have to match 
        in intensity
        force: boolean (default False) that if True will force the normalization to occur, even if it had been
        run before with the same data set

        Raises:
        =======
        IOError: if no sample loaded
        IOError: if no OB loaded
        IOError: if size of sample and OB do not match
        
        '''
        if not force:
            # does nothing if normalization has already been run
            if self.__exec_process_status['normalization']:
                return
        self.__exec_process_status['normalization'] = True
        
        # make sure we loaded some sample data
        if self.data['sample']['data'] == []:
            raise IOError("No normalization available as no data have been loaded")

        # make sure we loaded some ob data
        if self.data['ob']['data'] == []:
            raise IOError("No normalization available as no OB have been loaded")

        # make sure that the length of the sample and ob data do match
        nbr_sample = len(self.data['sample']['file_name'])
        nbr_ob = len(self.data['ob']['file_name'])
        if nbr_sample != nbr_ob:
            raise IOError("Number of sample and ob do not match!")
              
        # make sure the data loaded have the same size
        if not self.data_loaded_have_matching_shape():
            raise ValueError("Data loaded do not have the same shape!")
              
        # make sure, if provided, roi has the rigth type and fits into the images
        if roi:
            if not type(roi) == ROI:
                raise ValueError("roi must be a ROI object!")
            if not self.__roi_fit_into_sample(roi=roi):
                raise ValueError("roi does not fit into sample image!")
        
        if roi:
            _x0 = roi.x0
            _y0 = roi.y0
            _x1 = roi.x1
            _y1 = roi.y1
        
        # heat normalization algorithm
        _sample_corrected_normalized = []
        _ob_corrected_normalized = []
        
        if roi:
            _sample_corrected_normalized = [_sample / np.mean(_sample[_y0:_y1+1, _x0:_x1+1]) 
                                               for _sample in self.data['sample']['data']]
            _ob_corrected_normalized = [_ob / np.mean(_ob[_y0:_y1+1, _x0:_x1+1])
                                           for _ob in self.data['ob']['data']]
        else:
            _sample_corrected_normalized = copy.copy(self.data['sample']['data'])
            _ob_corrected_normalized = copy.copy(self.data['ob']['data'])
            
        self.data['sample']['data'] = _sample_corrected_normalized
        self.data['ob']['data'] = _ob_corrected_normalized
            
        # produce normalized data
        sample_ob = zip(self.data['sample']['data'], self.data['ob']['data'])
        normalized_data = []
        for [_sample, _ob] in sample_ob:
            _working_ob = _ob.copy()
            _working_ob[_working_ob == 0] = np.NaN
            _norm = np.divide(_sample, _working_ob)
            _norm[np.isnan(_norm)] = 0
            _norm[np.isinf(_norm)] = 0
            normalized_data.append(_norm)

        self.data['normalized'] = normalized_data

        return True
    
    def data_loaded_have_matching_shape(self):
        '''check that data loaded have the same shape
        
        Returns:
        =======
        bool: result of the check
        '''
        _shape_sample = self.data['sample']['shape']
        _shape_ob = self.data['ob']['shape']
        
        if not (_shape_sample == _shape_ob):
            return False
        
        _shape_df = self.data['df']['shape']
        if not np.isnan(_shape_df['height']):
            if not (_shape_sample == _shape_df):
                return False
            
        return True
    
    def __roi_fit_into_sample(self, roi=[]):
        '''check if roi is within the dimension of the image
        
        Returns:
        ========
        bool: True if roi is within the image dimension
        
        '''
        [sample_height, sample_width] = np.shape(self.data['sample']['data'][0])
        
        [_x0, _y0, _x1, _y1] = [roi.x0, roi.y0, roi.x1, roi.y1]
        if (_x0 < 0) or (_x1 >= sample_width):
            return False
        
        if (_y0 < 0) or (_y1 >= sample_height):
            return False

        return True
    
    def df_correction(self, force=False):
        '''dark field correction of sample and ob
        
        Parameters
        ==========
        force: boolean (default False) that if True will force the df correction to occur, even if it had been
        run before with the same data set

        sample_df_corrected = sample - DF
        ob_df_corrected = OB - DF

        '''
        if not force:
            if self.__exec_process_status['df_correction']:
                return
        self.__exec_process_status['df_correction'] = True
        
        if not self.data['sample']['data'] == []:
            self.__df_correction(data_type='sample')
            
        if not self.data['ob']['data'] == []:
            self.__df_correction(data_type='ob')
    
    def __df_correction(self, data_type='sample'):
        '''dark field correction
        
        Parameters:
           data_type: string ['sample','ob]
        '''
        if not data_type in ['sample', 'ob']:
            raise KeyError("Wrong data type passed. Must be either 'sample' or 'ob'!")

        if self.data['df']['data'] == []:
            return
        
        if self.data['df']['data_average'] == []:
            _df = self.data['df']['data']
            if len(_df) > 1:
                _df = average_df(df=_df)
            self.data['df']['data_average'] = _df
        else:
            _df = self.data['df']['data_average']

        if np.shape(self.data[data_type]['data'][0]) != np.shape(self.data['df']['data'][0]):
            raise IOError("{} and df data must have the same shpae!".format(data_type))
    
        _data_df_corrected = [_data - _df for _data in self.data[data_type]['data']]
        self.data[data_type]['data'] = _data_df_corrected
    
    def crop(self, roi=None, force=False):
        ''' Cropping the sample and ob normalized data
        
        Parameters:
        ===========
        roi: ROI object that defines the region to crop
        force: Boolean (default False) that force or not the algorithm to be run more than once
        with the same data set

        Raises:
        =======
        ValueError if sample and ob data have not been normalized yet
        '''
        if (self.data['sample']['data'] == []) or \
           (self.data['ob']['data'] == []):
            raise IOError("We need sample and ob Data !")

        if not type(roi) == ROI:
            raise ValueError("roi must be of type ROI")

        if not force:
            if self.__exec_process_status['crop']:
                return
        self.__exec_process_status['crop'] = True
        
        _x0 = roi.x0
        _y0 = roi.y0
        _x1 = roi.x1
        _y1 = roi.y1
        
        new_sample = [_data[_y0:_y1+1, _x0:_x1+1] for 
                      _data in self.data['sample']['data']]
        self.data['sample']['data'] = new_sample        
       
        new_ob = [_data[_y0:_y1+1, _x0:_x1+1] for 
                  _data in self.data['ob']['data']]
        self.data['ob']['data'] = new_ob        
        
        if not (self.data['df']['data'] == []):
            new_df = [_data[_y0:_y1+1, _x0:_x1+1] for 
                      _data in self.data['df']['data']]
            self.data['df']['data'] = new_df
            
        if not (self.data['normalized'] == []):
            new_normalized = [_data[_y0:_y1+1, _x0:_x1+1] for 
                              _data in self.data['normalized']]
            self.data['normalized'] = new_normalized        
        
        return True
    
   