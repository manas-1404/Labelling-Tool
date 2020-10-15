
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
    The :py:func:`Data_Load_Save_pkl` is used for loading and saving data as pickle file

    Attributes
    ----------
    path_base : str
        a formatted string containing your base directory path
    path_data_processed : str
        a formatted string containing your processed data directory path
    path_data_saved : str
        a formatted string containing your saved data directory path

    Methods
    -------
    load_pkl(name):
        Loads a pickle file named 'name'
    """

    def __init__(self, path_base = 'path_base', path_data_processed = 'path_data_processed', path_data_saved = 'path_data_saved'):

        """
        Creates an instance of the :py:func:`Data_Load_Save_pkl` class


        Parameters
        ----------
        path_base : str
            a formatted string containing your base directory path
        path_data_processed : str
            a formatted string containing your processed data directory path
        path_data_saved : str
            a formatted string containing your saved data directory path

        """  
        self.path_base = path_base
        self.path_data_processed = path_data_processed
        self.path_data_saved = path_data_saved

    def load_pkl(self, name):


        """
        The purpose of the :py:func:`Data_Load_Save_pkl.load_pkl` is to load a pickle file named 'name'


        Parameters
        ----------
        name : str
            a formatted string containing the name of the pickle file


        Returns
        -------
        df1 : dataframe
        """


        file = open(self.path_base + self.path_data_processed + name, 'rb')  # open a file, where you stored the pickled data
        df1 = pickle.load(file)   # dump information to that file
        file.close()   # close the file
        return df1
    