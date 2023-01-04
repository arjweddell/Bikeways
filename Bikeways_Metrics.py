# Script Name: Bikeways_Metrics.py
#
# Author: Angie Weddell
#
# This script summarizes route data stored in csv files, and calculates
# the mean, median, minimum, maximum, standard deviation, and interquartile 
# range for each file, then summarizes this data in a table by census tract.
#
# Arguments: Input:  any number of route data tables (csv)
#            Output: dataframe summarizing route data        
#
# Created: November 2020
# Designed to work with Python 3.6

# Import libraries

import sys
import pandas as pd
from pandas import DataFrame
import numpy as np
import glob
import os
import scipy
from scipy import stats 

# Import Route Files

os.chdir("C:/Users/Angie/Documents/Python/Census Tracts")
files = glob.glob('*.csv')
data = []
for csv in files:
    frame = pd.read_csv(csv)
    frame['filename'] = os.path.basename(csv)
    data.append(frame)

# Calculate summary statistics for each census tract and create data frame

CTs = [df['filename'].iloc[0].strip('T_Routes_table.csv').replace("_","") for df in data]
mean = [df['Shape_Length'].mean() for df in data]
median = [df['Shape_Length'].median() for df in data]
stdev = [df['Shape_Length'].std() for df in data]
maxi = [df['Shape_Length'].max() for df in data]
mini = [df['Shape_Length'].min() for df in data]
iq = [scipy.stats.iqr(df['Shape_Length']) for df in data]
count = [len(df.index) for df in data]

stats_all_df = DataFrame(list(zip(CTs,mean,median,stdev,maxi,mini,iq,count)),columns=['CTs','mean','median','stdev','maximum','minimum','IQ','count'])