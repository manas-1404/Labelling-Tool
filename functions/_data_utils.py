
import os
import numpy as np
import pandas as pd
import csv
import datetime as dt
import pickle
from random import sample 
from pathlib import Path

import warnings
import sklearn.exceptions
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)


#########################################################################


class Data_Load_Save_pkl:

    """
    The :py:func:`Active_Learning_UNC` class implements the active learning method based on Uncertainty sampling
    
    Returns    
    -------
    al_tst : Instance of the :py:func:`Active_Learning_UNC` class

    
    """

    def __init__(self, path_base = 'path_base', path_data_processed = 'path_data_processed', path_data_saved = 'path_data_saved'):

        """
        Create an instance of the :py:func:`Active_Learning_UNC` class

        """  
        self.path_base = path_base
        self.path_data_processed = path_data_processed
        self.path_data_saved = path_data_saved

    def load_pkl(self, name):
        file = open(self.path_base + self.path_data_processed + name, 'rb')  # open a file, where you stored the pickled data
        df1 = pickle.load(file)   # dump information to that file
        file.close()   # close the file
        return df1
        
    def load_results(self, model_name = 'KNN', mode = '_SUP'):
       
        name = mode + 'tot_results_f1_' + model_name
        completePath = os.path.join(self.path_data_saved, name)
        file = open(completePath, 'rb')  # open a file, where you stored the pickled data
        tot_results_f1_ = pickle.load(file)   # dump information to that file
        file.close()   # close the file
        
        name = mode + 'tot_results_roc_' + model_name
        completePath = os.path.join(self.path_data_saved, name)
        file = open(completePath, 'rb')  # open a file, where you stored the pickled data
        tot_results_roc_ = pickle.load(file)   # dump information to that file
        file.close()   # close the file
       
        return tot_results_f1_, tot_results_roc_

    def save_results(self, tot_results_f1, roc_df, model_name = 'KNN', mode = '_SUP'):

        save_name = mode + 'tot_results_f1_' + model_name
        save_name = self.path_data_saved + save_name
        file = open(save_name, 'wb')   # open a file, where you want to store the data
        pickle.dump(tot_results_f1, file, protocol=4)   # dump information to that file
        file.close()   # close the file
        
        save_name = mode + 'tot_results_roc_' + model_name
        save_name = self.path_data_saved + save_name
        file = open(save_name, 'wb')   # open a file, where you want to store the data
        pickle.dump(roc_df, file, protocol=4)   # dump information to that file
        file.close()   # close the file
