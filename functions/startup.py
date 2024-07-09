
from IPython import get_ipython
ipython = get_ipython()

# If in ipython, load autoreload extension
if 'ipython' in globals():
    ipython.run_line_magic('load_ext', 'autoreload')
    ipython.run_line_magic('autoreload','2')

# Import Statements

import os
import numpy as np
import pandas as pd
import csv
import datetime as dt
import itertools
import seaborn as sns
import datetime as datetime
from datetime import timedelta
from pathlib import Path
import time
from numpy import dstack
from pandas import read_csv
import pickle
import random
import itertools
import warnings
import sklearn.exceptions
from sklearn import preprocessing


# Plot
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from matplotlib import pyplot
import matplotlib.gridspec as gridspec
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

from matplotlib.widgets import Button
from matplotlib.widgets import SpanSelector
import random
import fcsparser


# Options
warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)

print('All libraries have been loaded.')