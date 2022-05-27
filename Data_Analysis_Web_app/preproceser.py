# -*- coding: utf-8 -*-
"""
Created on Sun May 22 13:09:34 2022

@author: Lenovo
"""


# this function is used for any data cleaning or manipulation

def preprocess(df):
    
    #df.drop(['ARAI_Certified_Mileage_for_CNG'], axis=1,inplace=True)
    df['Seating_Capacity'] = df['Seating_Capacity'].astype(int)
    df['Low_Fuel_Warning'] = df['Low_Fuel_Warning'].astype(int)

    df['ARAI_Certified_Mileage'].isnull().sum()
    df['ARAI_Certified_Mileage'] = df['ARAI_Certified_Mileage'].fillna(df['ARAI_Certified_Mileage'].mean())
    df.drop_duplicates(inplace=True)
    return df