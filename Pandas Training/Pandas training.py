# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:35:22 2022

@author: marin
"""

import pandas as pd

"""
Reading Data and creating data
"""
# Read all data
DataFrame = pd.read_csv("telco_churn.csv")#Read CSV,XML.....

#Create dictionary dataframe
TempDict = {'Col_1':[1,2,3],'Col_2':[4,5,6],'Col_3':[7,8,9]}
DictDataFrame = pd.DataFrame.from_dict(TempDict)

# Get first N Rows
First5 = DataFrame.head(5)
# Get Last 5 Rows
Last5 = DataFrame.tail(5)
#Show Columns names
ColumnName = DataFrame.columns
# Get type of data
Types = DataFrame.dtypes

"""
Summary statistic
"""
Descirbe = DataFrame.describe(include = 'object')

"""
Filter Columns
"""
StateColumn = DataFrame['State']
MultipleChoice = DataFrame[['State','International plan']]

# returns unique values
UniqueValues = DataFrame.Churn.unique()

"""
Filtering Rows
"""
SpecRows = DataFrame[DataFrame['International plan']=='No']
#Disnt leave buisness and international plan
JustInternationalPlans = DataFrame[  (DataFrame['International plan']=='No')  &  (DataFrame['Churn']==False)  ]
"""
indexing
"""
#WITH ILOC
Row_14 = DataFrame.iloc[14]
Row_14_last = DataFrame.iloc[14,-1]

Rows_22to33 = DataFrame.iloc[22:33]


#With LOC
state = DataFrame.copy()
state.set_index('State',inplace=True)
#just ohio state data
OhioState = state.loc['OH']

"""
Update
"""
#Droping rows
DataFrame2 = DataFrame.copy()
#drop data with missing values
DataFrame2.dropna(inplace=True)
#DropCOllumn
DataFrame2.drop('Area code', axis=1)

"""
Created Calculated column
"""
DataFrame2['New Column'] = DataFrame2['Total night minutes'] + DataFrame2['Total intl minutes']

#Update signle value
DataFrame2.iloc[0,-1] = 10

#apply update values from one to another
DataFrame2['Churn Binary'] = DataFrame2['Churn'].apply(lambda x: 1 if x==True else 0)

"""
Output data
"""
DataFrame2.to_csv('scv_output.csv')
OhioState.to_excel('excell_output.xlsx')




