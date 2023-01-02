# Script Name: Census Metrics.py
#
# Author: Angie Weddell
#
# This python script is used for extracting the Jounrey to Work commute
# mode data from the census table and summarizing it by census tract.
# This script also summarizes route data stored in csv files, and calculates
# the mean, median, minimum, maximum, standard deviation, and interquartile 
# range for each file, then summarizes this data in a table by census tract.
#
# Arguments: Input:  census data table (csv)
#                    any number of route data tables (csv)
#            Output: dataframe containing census commute mode data by census tract
#                    dataframe summarizing route data        
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

# Import Census Data Table

van_codes_df = pd.read_csv("Vancouver_Codes.csv")
van_codes = van_codes_df['Geo Code'].tolist()
df_van = pd.read_csv("van_data.csv")

# Pivot table and summarize commute data

df_van_pivot = df_van.pivot(index="ALT_GEO_CODE", columns="Member ID: Profile of Census Tracts (2247)",values="Dim: Sex (3): Member ID: [1]: Total - Sex")
df_van_commute = df_van_pivot.iloc[:,[0,1929,1930,1931,1932,1933,1934,1935]]
df_van_commute=df_van_commute.rename(columns={1:"Total_Pop",1930:"Commute_Pop",1931:"Car_Driver",1932: "Car_Passenger",1933:"Transit",1934:"Walk",1935:"Bike",1936:"Other"})

# remove invalid data and convert to float

def rep(i):
    if i == "x":
        i = 0
    elif i == "F":
        i = 0
    elif i == "...":
        i = 0
    elif i == "..":
        i = 0
    else:
        i = float(i)
    return i

df_van_commute['Total_Pop']=df_van_commute['Total_Pop'].apply(rep)
df_van_commute['Commute_Pop']=df_van_commute['Commute_Pop'].apply(rep)
df_van_commute['Car_Driver']=df_van_commute['Car_Driver'].apply(rep)
df_van_commute['Car_Passenger']=df_van_commute['Car_Passenger'].apply(rep)
df_van_commute['Transit']=df_van_commute['Transit'].apply(rep)
df_van_commute['Walk']=df_van_commute['Walk'].apply(rep)
df_van_commute['Bike']=df_van_commute['Bike'].apply(rep)
df_van_commute['Other']=df_van_commute['Other'].apply(rep)

# calculate cycling mode share, generate summary statistics and plots:

df_van_commute['bike_mode']=df_van_commute['Bike']/df_van_commute['Commute_Pop']

commute_box=df_van_commute.boxplot(column=['bike_mode'])
commute_hist=df_van_commute.hist(column=['bike_mode'],bins=18)
commute_mean = df_van_commute['bike_mode'].mean()
commute_median = df_van_commute['bike_mode'].median()
commute_stdev = df_van_commute['bike_mode'].std()
commute_maximum = df_van_commute['bike_mode'].max()
commute_minimum = df_van_commute['bike_mode'].min()
commute_iq = scipy.stats.iqr(df_van_commute['bike_mode'])

commute_stats = pd.DataFrame(["mean","median","stdev","minimum","maximum","iq"],[commute_mean,commute_median,commute_stdev,commute_minimum,commute_maximum,commute_iq])

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


