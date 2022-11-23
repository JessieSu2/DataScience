#!/usr/bin/env python
# coding: utf-8

# In[121]:


import pandas as pd
import numpy as np
import random
import os
print(os.getcwd())


# In[122]:


df = pd.read_csv("filtered_data.csv")
print(df.shape)
print(df.info())
print(df.head())
#(6129757, 9)


# In[123]:


# question we are answering
"""
We will be building a model to see if we could predict violation 
code based on vehicle descriptions and location.
Hence, this brings the awareness where people could try to be more careful if they match description
"""


# In[ ]:





# In[124]:


# observe data
print(df.isnull().sum())
# there are only null values in the following columns
# Vehicle Body Type
# Vehicle Make
# Violation Time
# Violation County
# Vehicle Color


# In[125]:


# violation code -> clean this first 
#     find lower threshold and remove violation tickets that dont lower threshold
# time -> format HHMM(A/P) -> use this to categorize time
# Vehicle Maker 
# Registration State
# Plate Type
# Vehicle Body Type
# Vehicle Color
#     find lower threshold by count and remove violation tickets that dont lower threshold
#     do by count 

# reason why we decide threshold by count
# the more people that has this description, the more relevant it is
# the less people that has this description, the less relevant it is 
# in terms of reflecting general population

# Hence
# reasoning to remove lower threshold
# this is because these descriptions do not reflect the overall population as the descriptions are not common
# lower threshold does not reflect 

# reason to keep upper threshold
# the more people that follows these descriptions, the more it reflects the general population
# hence, if we to remove upper threshold, it will essentially remove a huge chunk of our data that reflects general
# population

# for example
# if a violation code 'X' has only 1 violation 
# then it does not make sense to include 'X' since it does not reflect overall population
# and if a violation code 'Y' has 1000000
# then it does make sense to include Y

# in comparison to the total number of data
# a small portion of data has None values
# also in this context, we cannot use stuff we dont know as filling the none values will introduce inaccurate values
# so we could first drop Null values as it would not have a significant impact on the data

df = df.dropna()
print(df.isnull().sum())


# In[126]:


# approximately 500000 rows are removed mostly from color
print(df.shape)


# In[127]:


# inspect each column values to what needs further processing
print(df['Registration State'].unique())
# '99' do not look like a state so see how many vehicles are under this state
df = df[df['Registration State'] != '99']
print(df['Registration State'].unique())


# In[128]:


print(df['Plate Type'].unique())
# '999' do not look like a plate type so see how many under this and remove
df = df[df['Plate Type'] != '999']
print(df['Plate Type'].unique())
print(df['Plate Type'].value_counts())


# In[129]:


print(df['Violation Code'].unique())
# all violation codes in data
# choose violations that most reflect general population
print(df['Violation Code'].value_counts())
# df violtion code where code not in code_set
# create a dataframe
# violation code : count
# 


# In[ ]:





# In[130]:


print(df['Vehicle Body Type'].unique())
# choose body type that most reflect general population
print(df['Vehicle Body Type'].value_counts())


# In[131]:


print(df['Vehicle Make'].unique(), len(df['Vehicle Make'].unique()))
# too many vehicle makers
# choose relevant vehicle makers that reflects general population


# In[132]:


print(df['Violation Precinct'].unique(), len(df['Violation Precinct'].unique()))
# prob nothing to be done here


# In[133]:


print(df['Violation Time'].unique(), len(df['Violation Time'].unique()))

# remove rows of string length violation time less than 5
df = df[df['Violation Time'].apply(lambda x: len(str(x)) == 5)]
print(df.shape)
# too many time, standardize time

# Parts of the Day

# Morning     5 am to 12 pm (noon)

# Afternoon     12 pm to 5 pm

# Evening     5 pm to 9 pm

# Night         9 pm to 4 am

# create a new column "Violation Day" iterate through each row and 
violation_time = df["Violation Time"]

violation_day = []
start_morning = 5
end_morning = 12

start_noon = 12
end_noon = 5 + 12

start_evening = 5 + 12
end_evening = 9 + 12


for i, time in enumerate(violation_time):
    hour = int(time[0:2])
    # edge case
    if(hour == 12 and time[4] == 'A'):
        hour = 0
    elif(hour != 12 and time[4] == 'P'):
        hour = hour + 12

    if hour >= start_morning and hour < end_morning:
        violation_day.append("Morning")
    elif hour >= start_noon and hour < end_noon:
        violation_day.append("Afternoon")
    elif hour >= start_evening and hour < end_evening:
        violation_day.append("Evening")
    else:
        violation_day.append("Night")
        
print("done")    
df["Violation Day"] = violation_day
#drop violation column, no longer need it
df = df.drop(columns="Violation Time")
print(df["Violation Day"].value_counts())


# In[134]:


print(df['Violation County'].unique(), len(df['Violation County'].unique()))
# violation county has same county but different abbreivations

county_mapping = {'NY': 'NY','BX':'BX', 'Q':'QNS', 'R':'R', 'K':'K', 'MS': 'MS', 'BK': 'BK',
           'QN': 'QNS', 'MN': 'MN', 'Kings': 'K',
           'Qns': 'QNS', 'Bronx': 'BX', 'Rich': 'R', 'ST':'ST', 'QNS':'QNS', 'ABX': 'ABX'}

df['Violation County'] = df['Violation County'].map(county_mapping)
print(df['Violation County'].unique())
print(df['Violation County'].value_counts())
#drop 'MS' and 'ABX'
df = df[df['Violation County'] != 'MS']
df = df[df['Violation County'] != 'ABX']


# In[135]:


print(df['Violation County'].value_counts())
print(df['Vehicle Color'].unique(), len(df['Vehicle Color'].unique()))
# on closer inspection
# color abbreivation is not standardized
# so we see same colors with different abbreivation
# transform this


# In[136]:


# transformation to be done
# select data that reflects general population
# this includes
# plate type
# violation type
# vehicle maker
# color -> choose color that we could easily translate
# 
print(df['Vehicle Color'].value_counts())


# In[137]:


# write a funciton to get the counts + quartile + iqr
# find lower threshold remove it
# apply function on each of the data
# analyze data

