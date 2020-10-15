
import os
import numpy as np
import pandas as pd
import csv
import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot
import matplotlib.gridspec as gridspec
import itertools
from sklearn import preprocessing
import seaborn as sns
import datetime as datetime
from datetime import timedelta
import pickle
from random import sample 
from pathlib import Path
from numpy import dstack
from pandas import read_csv
import random

import warnings
import sklearn.exceptions
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)


#########################################################################


class Labels_proc:


    """
    The :py:func:`Labels_proc` is used for processing and saving labelled data for the UWO case

    Methods
    -------
    rem_dates(df2, df_bf_00, drop = True)
        Remove dates of variable df_bf_00 from dataframe df2 where temporal resolution is wrong

    get_date_time(data_df, sr0, multi = 0):
           # Get date_time list for variable sro in dataframe data_df

    rearr_cols(df):
        rearrange columns of dataframe df as 'index', 'date', 'time'

    save_pkl(name, path_base, path_data_processed,  df):
        Saves the dataframe df as pickle file

        """ 

    def __init__(self):

        """
        Create an instance of the :py:func:`Labels_proc` class

        """  

    

    def rem_dates(self, df2, df_bf_00, drop = True):   
    


        """
        The purpose of the :py:func:`Labels_proc.rem_dates` is to Remove dates of variable df_bf_00 from dataframe df2 where temporal resolution is wrong


        Parameters
        ----------

        df2: a dataframe

        df_bf_00 : variable name


        Returns
        -------
        df2 : dataframe without corrupted dates
        date_list : list of unique dates

        """

        i_date = df2.index.get_level_values(0)          # get all dates
        idx_date = np.unique(df2.index.get_level_values(0), return_index=True)[1]      # get index of unique dates
        date_list = i_date[idx_date]   # get list of all dates

        for pl_i in range(len(date_list)):
            if len(df_bf_00[date_list[pl_i].date()].values) != 288:
                print('Corrupted date:', date_list[pl_i].date())
                print('Corrupted date index:',idx_date[pl_i])
                print('Corrupted date shape:', df2.loc[date_list[pl_i].date()].shape) 
                if drop == True:
                    df2.drop(date_list[pl_i].date(),level='date',inplace=True)

        # Get new dates list
        
        i_date = df2.index.get_level_values(0)          # get all dates
        idx_date = np.unique(df2.index.get_level_values(0), return_index=True)[1]      # get index of unique dates
        date_list = i_date[idx_date]   # get list of all dates
                
        return df2, date_list


 
    def get_date_time(self, data_df, sr0, multi = 0):


        """
        The purpose of the :py:func:`Labels_proc.get_date_time` is to Get date_time list for variable sro in dataframe data_df


        Parameters
        ----------

        data_df: a dataframe

        sr0 : variable name


        Returns
        -------
        data_lab_1 : dataframe with date and time columns

        
        """

        if multi == 0:
            data_lab_1 = pd.DataFrame(data_df[sr0])
            data_lab_1 = data_lab_1.reset_index(level=[0,1])
            data_lab_1['date'] = [x.strftime('%Y-%m-%d') for x in (pd.to_datetime([i for i in data_lab_1['date']], format='%Y-%m-%d'))] 
            data_lab_1['time'] = [x.strftime('%H:%M:%S') for x in (pd.to_datetime([i for i in data_lab_1['time']], format='%H:%M:%S'))] 
        else:
            data_lab_1 = data_df.copy()
            data_lab_1 = data_lab_1.reset_index(level=[0,1])
            data_lab_1['date'] = [x.strftime('%Y-%m-%d') for x in (pd.to_datetime([i for i in data_lab_1['date']], format='%Y-%m-%d'))] 
            data_lab_1['time'] = [x.strftime('%H:%M:%S') for x in (pd.to_datetime([i for i in data_lab_1['time']], format='%H:%M:%S'))] 
            
        return data_lab_1


    def rearr_cols(self, df):

        """
        The purpose of the :py:func:`Labels_proc.rearr_cols` is to rearrange columns of dataframe df as 'index', 'date', 'time'

        Parameters
        ----------
        df: a dataframe

        Returns
        -------
        df : dataframe with rearranged date and time columns

        """

        df.drop(columns=['index', 'date', 'time'], inplace=True)
        cols = df.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        df = df[cols]
        
        return df



    ########### SAVE LOAD

    def save_pkl(self, name, path_base, path_data_processed,  df):

        """
        The purpose of the :py:func:`Labels_proc.save_pkl` is to save the dataframe df as pickle file


        Parameters
        ----------

        name: name of the file 
        path_base, path_data_processed : data paths
        df: dataframe to be saved
        
        """

        file = open(path_base + path_data_processed + name, 'wb')   # open a file, where you want to store the data
        pickle.dump(df, file, protocol=4)   # dump information to that file
        file.close()  



class Labels_proc_NEST:

    """
    The :py:func:`Labels_proc_NEST` is used for processing and saving labelled data for the NEST case

    Methods
    -------
    data_labels_load (path_base, folder, labels, ss):
        Loads data with associated labels

    process_data(data_all_labels):
           # Process data and removes duplicates and rearrage columns for date and time

    process_data_coll(data_all_labels):
        # Process data and removes duplicates and rearrage columns for date and time

    """ 

    def __init__(self):

        """
        Create an instance of the :py:func:`Labels_proc_NEST` class

        """  
    def data_labels_load (self, path_base, folder, labels, ss):


        """
        The purpose of the :py:func:`Labels_proc_NEST.data_labels_load` is to load data with associated labels

        Parameters
        ----------
        path_base: data path (base)
        folder: folder containing the data
        labels: folder name containing the labels
        ss: string, name of the labels, e.g. "'_labels_timep1'"


        Returns
        -------
        data_all : dataframe with data and labels
        
        """


        ss = ss + '.csv'
        data_files = []
        data_files_path = []
        for name in os.listdir(path_base + folder + labels):
            if name.endswith(ss):
                data_files.append(name)
                data_files_path.append(path_base + folder + labels + name)
            data_files_path = sorted(data_files_path) 
            
        tmp = []
        data_all = pd.DataFrame()
        for fn in data_files_path:
            df = pd.read_csv(fn,index_col=[0])
            tmp = pd.concat([data_all, df] , ignore_index=True)
            data_all = tmp.copy()
            
        return data_all


    def process_data(self, data_all_labels):


        """
        The purpose of the :py:func:`Labels_proc_NEST.process_data` is to process data and removes duplicates and rearrage columns for date and time

        Parameters
        ----------
        data_all_labels: dataframe

        Returns
        -------
        data_all_labels : processed dataframe 
        
        """

        data_all_labels['datetime'] = pd.to_datetime(data_all_labels['day']+ ' ' + data_all_labels['time'])
        data_all_labels.drop_duplicates('datetime',inplace=True)
        print('Fraction of anomalies: ', np.sum(data_all_labels['Anomaly'] ==1)/data_all_labels.shape[0])
        print('Shape:', data_all_labels.shape)
        data_all_labels.reset_index(inplace=True)
        return data_all_labels

    def process_data_coll(self, data_all_labels):


        """
        The purpose of the :py:func:`Labels_proc_NEST.process_data_coll` is to process data and removes duplicates and rearrage columns for date and time

        Parameters
        ----------
        data_all_labels: dataframe

        Returns
        -------
        data_all_labels : processed dataframe 
        
        """
        
        data_all_labels['datetime'] = pd.to_datetime(data_all_labels['day']+ ' ' + data_all_labels['time'])
        data_all_labels.drop_duplicates('datetime',inplace=True)
        print('Fraction of anomalies: ', np.sum(data_all_labels['Tot_anomalies'] ==1)/data_all_labels.shape[0])
        print('Shape:', data_all_labels.shape)
        data_all_labels.reset_index(inplace=True)
        return data_all_labels

