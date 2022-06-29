# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 19:48:43 2022

@author: RJ HARI
"""

#importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing data set
df = pd.read_csv("data sets/hotel_bookings.csv")

#to find more information or null values in given data set
df.info()
df.isnull().sum()

#cleaning outlayers in data
#creating dummy container 
a= df.fillna(method="ffill") 
a.isnull().sum()
a.info()
b=a.fillna(method="bfill")
b.isnull().sum()
b.info()

#high data set means we can use to see 5 calums
df.head()

#we can drop some unnessary colums
df = df.drop(columns=['required_car_parking_spaces', 'market_segment', 'is_repeated_guest '])

# by this be can locate index value of colum and row
df.iloc[:20, 10:20]

# we can specify exact row and colum in this function
df.loc[[3, 10, 14, 23], ['reserved_room_type', 'assigned_room_type', "reservation_status"]]

#including only selected data types ie:(int64)
a.select_dtypes(include='int64')

#for excluding
df.select_dtypes(exclude='int64')

#it provides us cumulative value of specified colum
df[['adr', 'lead_time ']].cumsum()

#if we have to much of big data we can choose how many we need
df.sample(n = 200)
df.sample(frac = 0.25)

#if we have 0 to 100 means we need to know what data is bigger than n means
df['adr'].where(df['adr'] > 50)
#by adding zero in the end we can avoid nan outputs that shown value below n
df['adr'].where(df['adr'] > 50, 0)

#we can see unique values that present in desired colum
df.country.unique()
df.meal.unique()

#to know number of unique values in the dataset
df.nunique()

#if we need to replace any present value in colum
df.replace(0, 1)
df.replace({0:1,  4.0: 4.1, 3.0: 3.1})
 
#if we need to rename any colum name means 
df.replace({1.0: 1.1,  15: 10})

#comparing by object and group 
df.groupby("country")['distribution_channel'].sum()

#counting the value of desired colum 
df['adr'].value_counts()
df['adr'].value_counts(ascending=True)

#cross tabing the desired colums
pd.crosstab(df['league_rank'], df['international_reputation'])

#This gives you the dataset with n number of largest values or smallest values of a specified variable
df.nlargest(5, "agent")
df.nsmallest(5, "agent")

#some basic statistical method to find on needed colum
a['adr'].describe()
a['agent'].describe()

#for finding duplicates
df.drop_duplicates(inplace = True)
print(df.to_string())
df.info()

#
