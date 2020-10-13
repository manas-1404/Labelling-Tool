
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
    The :py:func:`Active_Learning_UNC` class implements the active learning method based on Uncertainty sampling
    
    Returns    
    -------
    al_tst : Instance of the :py:func:`Active_Learning_UNC` class

    
    """

    def __init__(self):

        """
        Create an instance of the :py:func:`Active_Learning_UNC` class

        """  



    

    def rem_dates(self, df2, df_bf_00, drop = True):   # Remove dates where temporal resolution is wrong
        # Accessing dates
        i_date = df2.index.get_level_values(0)          # get all dates
        idx_date = np.unique(df2.index.get_level_values(0), return_index=True)[1]      # get index of unique dates
        date_list = i_date[idx_date]   # get list of all dates
        #print('Unique dates:',date_list)

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


    # Get date_time
    def get_date_time(self, data_df, sr0, multi = 0):
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
        df.drop(columns=['index', 'date', 'time'], inplace=True)
        cols = df.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        df = df[cols]
        
        return df



    ########### SAVE LOAD

    def save_pkl(self, name, path_base, path_data_processed,  df):
        file = open(path_base + path_data_processed + name, 'wb')   # open a file, where you want to store the data
        pickle.dump(df, file, protocol=4)   # dump information to that file
        file.close()  



class Labels_proc_NEST:

    """
    The :py:func:`Active_Learning_UNC` class implements the active learning method based on Uncertainty sampling
    
    Returns    
    -------
    al_tst : Instance of the :py:func:`Active_Learning_UNC` class

    
    """

    def __init__(self):

        """
        Create an instance of the :py:func:`Active_Learning_UNC` class

        """  
    def data_labels_load (self, path_base, folder, labels, ss):
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
        data_all_labels['datetime'] = pd.to_datetime(data_all_labels['day']+ ' ' + data_all_labels['time'])
        data_all_labels.drop_duplicates('datetime',inplace=True)
        print('Fraction of anomalies: ', np.sum(data_all_labels['Anomaly'] ==1)/data_all_labels.shape[0])
        print('Shape:', data_all_labels.shape)
        data_all_labels.reset_index(inplace=True)
        return data_all_labels

    def process_data_coll(self, data_all_labels):
        data_all_labels['datetime'] = pd.to_datetime(data_all_labels['day']+ ' ' + data_all_labels['time'])
        data_all_labels.drop_duplicates('datetime',inplace=True)
        print('Fraction of anomalies: ', np.sum(data_all_labels['Tot_anomalies'] ==1)/data_all_labels.shape[0])
        print('Shape:', data_all_labels.shape)
        data_all_labels.reset_index(inplace=True)
        return data_all_labels

