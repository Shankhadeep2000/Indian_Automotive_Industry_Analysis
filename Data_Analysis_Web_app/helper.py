# -*- coding: utf-8 -*-
"""
Created on Sun May 22 13:23:32 2022

@author: Shankhadeep Sarkar
"""
# importing the library
import numpy as np

#Functions which will take the input and compare it with the csv data and show the relaed answer

#This function will define the columns to be taken for the respective analysis
def Engine_Performace(df):
    engine_df1 = df.drop_duplicates(subset=['ARAI_Certified_Mileage', 'Torque',  'price', 'Cylinders', 'Turbocharger', 'Displacement'])
    engine_df1 = engine_df1.groupby('Body_Type').mean()[['Power','price','ARAI_Certified_Mileage','Cylinders']].sort_values('Power',ascending=False).reset_index()
    return engine_df1

#This will define the options for each functions as per dataset
def Body_cylinder(df):
    body = df['Body_Type'].unique().tolist()
    body.sort()
    body.insert(0,'Overall')
    
    cylinder = df['Cylinders'].unique().tolist()
    cylinder.sort()
    cylinder.insert(0,'Overall')
    
    return body,cylinder

#It will fetch the input and display the related data
def fetch_medal_tally(df, cylinder, body):
    engine_df1 = df.drop_duplicates(subset=['ARAI_Certified_Mileage', 'Torque',  'price', 'Cylinders', 'Turbocharger', 'Displacement'])
    flag = 0
    if cylinder == 'Overall' and body == 'Overall':
        temp_df = engine_df1
    if cylinder == 'Overall' and body != 'Overall':
        flag = 1
        
        temp_df = engine_df1[engine_df1['Body_Type'] == body]
    if cylinder != 'Overall' and body == 'Overall':
        temp_df = engine_df1[engine_df1['Cylinders'] == int(cylinder)]
    if cylinder != 'Overall' and body != 'Overall':
        temp_df = engine_df1[(engine_df1['Cylinders'] == cylinder) & (engine_df1['Body_Type'] == body)]
    if flag == 1:
        x = temp_df.groupby('Cylinders').mean()[['Power','price','ARAI_Certified_Mileage','Torque']].sort_values('Power',ascending=False).reset_index()
        
        x['ARAI_Certified_Mileage'] = x['ARAI_Certified_Mileage'].astype('int')
        x['Cylinders'] = x['Cylinders'].astype('int')
        x['price'] = x['price'].astype('int')
        
    else:
        x = temp_df.groupby('Body_Type').mean()[['Power','price','ARAI_Certified_Mileage','Cylinders']].sort_values('Power',ascending=False).reset_index()
        
        x['ARAI_Certified_Mileage'] = x['ARAI_Certified_Mileage'].astype('int')
        x['Cylinders'] = x['Cylinders'].astype('int')
        x['price'] = x['price'].astype('int')                                                                               

    return x

#This function will define the columns to be taken for the respective analysis
def body_type(df):
    body_df1 = df.drop_duplicates(subset=['Make', 'price','Body_Type','Power','Seating_Capacity','Fuel_Type'])
    body_df1 = body_df1.groupby('Body_Type','Make','Fuel_Type').mean()[['Power','price','Seating_Capacity']].sort_values('Power',ascending=False).reset_index()
    
    return body_df1 
 

def body_make_fuel(df):
    body = df['Body_Type'].unique().tolist()
    body.sort()
    body.insert(0,'Overall')
    
    make = df['Make'].unique().tolist()
    make.sort()
    make.insert(0,'Overall')
    
    fuel = df['Fuel_Type'].unique().tolist()
    fuel.sort()
    fuel.insert(0,'Overall')
    
    seat = df['Seating_Capacity'].unique().tolist()
    seat.sort()
    seat.insert(0,'Overall')
    
    return body,make,fuel,seat



#It will fetch the input and display the related data
def fetch_body_type(df, make, body, seat, fuel):
    body_df1 = df.drop_duplicates(subset=['Make', 'price','Body_Type','Power','Seating_Capacity','Fuel_Type'])
   
    if make == 'Overall' and body == 'Overall' and seat == 'Overall' and fuel == 'Overall':
        temp_df = body_df1
    if make == 'Overall' and body == 'Overall' and seat == 'Overall' and fuel != 'Overall':
       
        
        temp_df = body_df1[body_df1['Fuel_Type'] == fuel]
    if make == 'Overall' and body == 'Overall' and seat != 'Overall' and fuel == 'Overall':
        
        temp_df = body_df1[body_df1['Seating_Capacity'] == int(seat)]
    if make == 'Overall' and body != 'Overall' and seat == 'Overall' and fuel == 'Overall':
        
        temp_df = body_df1[body_df1['Body_Type'] == body]
    if make != 'Overall' and body == 'Overall' and seat == 'Overall' and fuel == 'Overall':
        
        temp_df = body_df1[body_df1['Make'] == make]
    
    if make != 'Overall' and body != 'Overall' and seat == 'Overall' and fuel == 'Overall':
        
        temp_df = body_df1[(body_df1['Make'] == make) & (body_df1['Body_Type'] == body)]
        
    if make != 'Overall' and body == 'Overall' and seat != 'Overall' and fuel == 'Overall':
        
        temp_df = body_df1[(body_df1['Make'] == make) & (body_df1['Seating_Capacity'] == seat)]
        
    if make != 'Overall' and body == 'Overall' and seat == 'Overall' and fuel != 'Overall':
        
        temp_df = body_df1[(body_df1['Make'] == make) & (body_df1['Fuel_Type'] == fuel)]
    if make != 'Overall' and body != 'Overall' and seat == 'Overall' and fuel == 'Overall':
        temp_df = body_df1[(body_df1['Make'] == make) & (body_df1['Body_Type'] == body)]
    if make == 'Overall' and body != 'Overall' and seat != 'Overall' and fuel == 'Overall':
        temp_df = body_df1[(body_df1['Body_Type'] == body) & (body_df1['Seating_Capacity'] == seat)]
    if make == 'Overall' and body != 'Overall' and seat == 'Overall' and fuel != 'Overall':
        temp_df = body_df1[(body_df1['Body_Type'] == body) & (body_df1['Fuel_Type'] == fuel)]
    if make != 'Overall' and body == 'Overall' and seat != 'Overall' and fuel == 'Overall':
        temp_df = body_df1[(body_df1['Seating_Capacity'] == seat) & (body_df1['Make'] == make)]
    if make == 'Overall' and body != 'Overall' and seat != 'Overall' and fuel == 'Overall':
        
        temp_df = body_df1[(body_df1['Seating_Capacity'] == seat) & (body_df1['Body_Type'] == body)]
    if make == 'Overall' and body == 'Overall' and seat != 'Overall' and fuel != 'Overall':
        
        temp_df = body_df1[(body_df1['Seating_Capacity'] == seat) & (body_df1['Fuel_Type'] == fuel)]
        
    if make == 'Overall' and body != 'Overall' and seat == 'Overall' and fuel != 'Overall':
        
        temp_df = body_df1[(body_df1['Body_Type'] == body) & (body_df1['Fuel_Type'] == fuel)]
    if make != 'Overall' and body == 'Overall' and seat == 'Overall' and fuel != 'Overall':
        
        temp_df = body_df1[(body_df1['Make'] == make) & (body_df1['Fuel_Type'] == fuel)]
        
    if make != 'Overall' and body == 'Overall' and seat != 'Overall' and fuel != 'Overall':
        temp_df = body_df1[(body_df1['Make'] == make) & (body_df1['Fuel_Type'] == fuel) & (body_df1['Seating_Capacity'] == seat)]
        
    if make != 'Overall' and body != 'Overall' and seat != 'Overall' and fuel == 'Overall':
        temp_df = body_df1[(body_df1['Make'] == make) & (body_df1['Body_Type'] == body) & (body_df1['Seating_Capacity'] == seat)]
        
    if make != 'Overall' and body != 'Overall' and seat == 'Overall' and fuel != 'Overall':
        temp_df = body_df1[(body_df1['Make'] == make) & (body_df1['Fuel_Type'] == fuel) & (body_df1['Body_Type'] == body)]
        
    if make == 'Overall' and body != 'Overall' and seat != 'Overall' and fuel != 'Overall':
        temp_df = body_df1[(body_df1['Body_Type'] == body) & (body_df1['Fuel_Type'] == fuel) & (body_df1['Seating_Capacity'] == seat)]
        
    if make != 'Overall' and body != 'Overall' and seat != 'Overall' and fuel != 'Overall':
        
        temp_df = body_df1[(body_df1['Make'] == make) & (body_df1['Fuel_Type'] == fuel) & (body_df1['Seating_Capacity'] == seat) & (body_df1['Body_Type'] == body)]
        
    x = temp_df.groupby('Body_Type').mean()[['Power','price','Seating_Capacity']].sort_values('Power',ascending=False).reset_index()
    
    x['Seating_Capacity'] = x['Seating_Capacity'].astype('int')
    x['Power'] = x['Power'].astype('int') 
    x['price'] = x['price'].astype('int')                                                                                

    return x


#This function will define the columns to be taken for the respective analysis
def Safety(df):
    safe_df = df.drop_duplicates(subset=['Central_Locking', 'Sun_Visor',  'price', 'Number_of_Airbags', 'Child_Safety_Locks','EBA_(Electronic_Brake_Assist)','EBD_(Electronic_Brake-force_Distribution)', 'Parking_Assistance','ABS_(Anti-lock_Braking_System)'])
    safe_df = safe_df.groupby('Body_Type').mean()[['Central_Locking',  'price', 'Number_of_Airbags', 'Child_Safety_Locks','EBA_(Electronic_Brake_Assist)','EBD_(Electronic_Brake-force_Distribution)','ABS_(Anti-lock_Braking_System)']].sort_values('price',ascending=False).reset_index()
    return safe_df

def safe(df):
    airbag = df['Number_of_Airbags'].unique().tolist()
    airbag.sort()
    airbag.insert(0,'Overall')
    
    eba = df['EBA_(Electronic_Brake_Assist)'].unique().tolist()
    eba.sort()
    eba.insert(0,'Overall')
    
    ebd = df['EBD_(Electronic_Brake-force_Distribution)'].unique().tolist()
    ebd.sort()
    ebd.insert(0,'Overall')
    
    abso = df['ABS_(Anti-lock_Braking_System)'].unique().tolist()
    abso.sort()
    abso.insert(0,'Overall')
    
    return airbag,eba,ebd,abso


#It will fetch the input and display the related data
def fetch_safety_type(df, eba, airbag, abso, ebd):
    safe_df = df.drop_duplicates(subset=['Central_Locking', 'Sun_Visor',  'price', 'Number_of_Airbags', 'Child_Safety_Locks','EBA_(Electronic_Brake_Assist)','EBD_(Electronic_Brake-force_Distribution)', 'Parking_Assistance','ABS_(Anti-lock_Braking_System)'])
   
    if eba == 'Overall' and airbag == 'Overall' and abso == 'Overall' and ebd == 'Overall':
        temp_df = safe_df
    if eba == 'Overall' and airbag == 'Overall' and abso == 'Overall' and ebd != 'Overall':
       
        
        temp_df = safe_df[safe_df['EBD_(Electronic_Brake-force_Distribution)'] == ebd]
    if eba == 'Overall' and airbag == 'Overall' and abso != 'Overall' and ebd == 'Overall':
        
        temp_df = safe_df[safe_df['ABS_(Anti-lock_Braking_System)'] == int(abso)]
    if eba == 'Overall' and airbag != 'Overall' and abso == 'Overall' and ebd == 'Overall':
        
        temp_df = safe_df[safe_df['Number_of_Airbags'] == airbag]
    if eba != 'Overall' and airbag == 'Overall' and abso == 'Overall' and ebd == 'Overall':
        
        temp_df = safe_df[safe_df['EBA_(Electronic_Brake_Assist)'] == eba]
    
    if eba != 'Overall' and airbag != 'Overall' and abso == 'Overall' and ebd == 'Overall':
        
        temp_df = safe_df[(safe_df['EBA_(Electronic_Brake_Assist)'] == eba) & (safe_df['Number_of_Airbags'] == airbag)]
        
    if eba != 'Overall' and airbag == 'Overall' and abso != 'Overall' and ebd == 'Overall':
        
        temp_df = safe_df[(safe_df['EBA_(Electronic_Brake_Assist)'] == eba) & (safe_df['ABS_(Anti-lock_Braking_System)'] == abso)]
        
    if eba != 'Overall' and airbag == 'Overall' and abso == 'Overall' and ebd != 'Overall':
        
        temp_df = safe_df[(safe_df['EBA_(Electronic_Brake_Assist)'] == eba) & (safe_df['EBD_(Electronic_Brake-force_Distribution)'] == ebd)]
    if eba != 'Overall' and airbag != 'Overall' and abso == 'Overall' and ebd == 'Overall':
        temp_df = safe_df[(safe_df['EBA_(Electronic_Brake_Assist)'] == eba) & (safe_df['Number_of_Airbags'] == airbag)]
    if eba == 'Overall' and airbag != 'Overall' and abso != 'Overall' and ebd == 'Overall':
        temp_df = safe_df[(safe_df['Number_of_Airbags'] == airbag) & (safe_df['ABS_(Anti-lock_Braking_System)'] == abso)]
    if eba == 'Overall' and airbag != 'Overall' and abso == 'Overall' and ebd != 'Overall':
        temp_df = safe_df[(safe_df['Number_of_Airbags'] == airbag) & (safe_df['EBD_(Electronic_Brake-force_Distribution)'] == ebd)]
    if eba != 'Overall' and airbag == 'Overall' and abso != 'Overall' and ebd == 'Overall':
        temp_df = safe_df[(safe_df['ABS_(Anti-lock_Braking_System)'] == abso) & (safe_df['EBA_(Electronic_Brake_Assist)'] == eba)]
    if eba == 'Overall' and airbag != 'Overall' and abso != 'Overall' and ebd == 'Overall':
        
        temp_df = safe_df[(safe_df['ABS_(Anti-lock_Braking_System)'] == abso) & (safe_df['Number_of_Airbags'] == airbag)]
    if eba == 'Overall' and airbag == 'Overall' and abso != 'Overall' and ebd != 'Overall':
        
        temp_df = safe_df[(safe_df['ABS_(Anti-lock_Braking_System)'] == abso) & (safe_df['EBD_(Electronic_Brake-force_Distribution)'] == ebd)]
        
    if eba == 'Overall' and airbag != 'Overall' and abso == 'Overall' and ebd != 'Overall':
        
        temp_df = safe_df[(safe_df['Number_of_Airbags'] == airbag) & (safe_df['EBD_(Electronic_Brake-force_Distribution)'] == ebd)]
    if eba != 'Overall' and airbag == 'Overall' and abso == 'Overall' and ebd != 'Overall':
        
        temp_df = safe_df[(safe_df['EBA_(Electronic_Brake_Assist)'] == eba) & (safe_df['EBD_(Electronic_Brake-force_Distribution)'] == ebd)]
        
    if eba != 'Overall' and airbag == 'Overall' and abso != 'Overall' and ebd != 'Overall':
        temp_df = safe_df[(safe_df['EBA_(Electronic_Brake_Assist)'] == eba) & (safe_df['EBD_(Electronic_Brake-force_Distribution)'] == ebd) & (safe_df['ABS_(Anti-lock_Braking_System)'] == abso)]
        
    if eba != 'Overall' and airbag != 'Overall' and abso != 'Overall' and ebd == 'Overall':
        temp_df = safe_df[(safe_df['EBA_(Electronic_Brake_Assist)'] == eba) & (safe_df['Number_of_Airbags'] == airbag) & (safe_df['ABS_(Anti-lock_Braking_System)'] == abso)]
        
    if eba != 'Overall' and airbag != 'Overall' and abso == 'Overall' and ebd != 'Overall':
        temp_df = safe_df[(safe_df['EBA_(Electronic_Brake_Assist)'] == eba) & (safe_df['EBD_(Electronic_Brake-force_Distribution)'] == ebd) & (safe_df['Number_of_Airbags'] == airbag)]
        
    if eba == 'Overall' and airbag != 'Overall' and abso != 'Overall' and ebd != 'Overall':
        temp_df = safe_df[(safe_df['Number_of_Airbags'] == airbag) & (safe_df['EBD_(Electronic_Brake-force_Distribution)'] == ebd) & (safe_df['ABS_(Anti-lock_Braking_System)'] == abso)]
        
    if eba != 'Overall' and airbag != 'Overall' and abso != 'Overall' and ebd != 'Overall':
        
        temp_df = safe_df[(safe_df['EBA_(Electronic_Brake_Assist)'] == eba) & (safe_df['EBD_(Electronic_Brake-force_Distribution)'] == ebd) & (safe_df['ABS_(Anti-lock_Braking_System)'] == abso) & (safe_df['Number_of_Airbags'] == airbag)]
        
    x = temp_df.groupby('Body_Type').mean()[['Central_Locking',  'price', 'Number_of_Airbags', 'Child_Safety_Locks','EBA_(Electronic_Brake_Assist)','EBD_(Electronic_Brake-force_Distribution)','ABS_(Anti-lock_Braking_System)']].sort_values('price',ascending=False).reset_index()
                                                                                      
    x['EBA_(Electronic_Brake_Assist)'] = x['EBA_(Electronic_Brake_Assist)'].astype('int')
    x['price'] = x['price'].astype('int')
    x['Central_Locking'] = x['Central_Locking'].astype('int')
    x['Number_of_Airbags'] = x['Number_of_Airbags'].astype('int')
    x['Child_Safety_Locks'] = x['Child_Safety_Locks'].astype('int')
    x['EBD_(Electronic_Brake-force_Distribution)'] = x['EBD_(Electronic_Brake-force_Distribution)'].astype('int')
    x['ABS_(Anti-lock_Braking_System)'] = x['ABS_(Anti-lock_Braking_System)'].astype('int')
    
    return x

#This function will define the columns to be taken for the respective analysis
def Fuel(df):
    fuel_df = df.drop_duplicates(subset=['Low_Fuel_Warning', 'Fuel_Type',  'price', 'Fuel_System', 'Fuel_Tank_Capacity'])
    fuel_df = fuel_df.groupby('Fuel_Type').mean()[['Low_Fuel_Warning',  'price', 'Fuel_Tank_Capacity']].sort_values('price',ascending=False).reset_index()
    return fuel_df



def fuel(df):
    fs = df['Fuel_System'].unique().tolist()
    fs.sort()
    fs.insert(0,'Overall')
    
    lfw = df['Low_Fuel_Warning'].unique().tolist()
    lfw.sort()
    lfw.insert(0,'Overall')
    
    ftc = df['Fuel_Tank_Capacity'].unique().tolist()
    ftc.sort()
    ftc.insert(0,'Overall')
    
    ft = df['Fuel_Type'].unique().tolist()
    ft.sort()
    ft.insert(0,'Overall')
    
    return fs,lfw,ftc,ft


#It will fetch the input and display the related data
def fetch_fuel_features(df, lfw, fs, ft, ftc):
    fuel_df = df.drop_duplicates(subset=['Low_Fuel_Warning', 'Fuel_Type',  'price', 'Fuel_System', 'Fuel_Tank_Capacity'])
   
    if lfw == 'Overall' and fs == 'Overall' and ft == 'Overall' and ftc == 'Overall':
        temp_df = fuel_df
    if lfw == 'Overall' and fs == 'Overall' and ft == 'Overall' and ftc != 'Overall':
       
        
        temp_df = fuel_df[fuel_df['Fuel_Tank_Capacity'] == ftc]
    if lfw == 'Overall' and fs == 'Overall' and ft != 'Overall' and ftc == 'Overall':
        
        temp_df = fuel_df[fuel_df['Fuel_Type'] == ft]
    if lfw == 'Overall' and fs != 'Overall' and ft == 'Overall' and ftc == 'Overall':
        
        temp_df = fuel_df[fuel_df['Fuel_System'] == fs]
    if lfw != 'Overall' and fs == 'Overall' and ft == 'Overall' and ftc == 'Overall':
        
        temp_df = fuel_df[fuel_df['Low_Fuel_Warning'] == lfw]
    
    if lfw != 'Overall' and fs != 'Overall' and ft == 'Overall' and ftc == 'Overall':
        
        temp_df = fuel_df[(fuel_df['Low_Fuel_Warning'] == lfw) & (fuel_df['Fuel_System'] == fs)]
        
    if lfw != 'Overall' and fs == 'Overall' and ft != 'Overall' and ftc == 'Overall':
        
        temp_df = fuel_df[(fuel_df['Low_Fuel_Warning'] == lfw) & (fuel_df['Fuel_Type'] == ft)]
        
    if lfw != 'Overall' and fs == 'Overall' and ft == 'Overall' and ftc != 'Overall':
        
        temp_df = fuel_df[(fuel_df['Low_Fuel_Warning'] == lfw) & (fuel_df['Fuel_Tank_Capacity'] == ftc)]
    if lfw != 'Overall' and fs != 'Overall' and ft == 'Overall' and ftc == 'Overall':
        temp_df = fuel_df[(fuel_df['Low_Fuel_Warning'] == lfw) & (fuel_df['Fuel_System'] == fs)]
    if lfw == 'Overall' and fs != 'Overall' and ft != 'Overall' and ftc == 'Overall':
        temp_df = fuel_df[(fuel_df['Fuel_System'] == fs) & (fuel_df['Fuel_Type'] == ft)]
    if lfw == 'Overall' and fs != 'Overall' and ft == 'Overall' and ftc != 'Overall':
        temp_df = fuel_df[(fuel_df['Fuel_System'] == fs) & (fuel_df['Fuel_Tank_Capacity'] == ftc)]
    if lfw != 'Overall' and fs == 'Overall' and ft != 'Overall' and ftc == 'Overall':
        temp_df = fuel_df[(fuel_df['Fuel_Type'] == ft) & (fuel_df['Low_Fuel_Warning'] == lfw)]
    if lfw == 'Overall' and fs != 'Overall' and ft != 'Overall' and ftc == 'Overall':
        
        temp_df = fuel_df[(fuel_df['Fuel_Type'] == ft) & (fuel_df['Fuel_System'] == fs)]
    if lfw == 'Overall' and fs == 'Overall' and ft != 'Overall' and ftc != 'Overall':
        
        temp_df = fuel_df[(fuel_df['Fuel_Type'] == ft) & (fuel_df['Fuel_Tank_Capacity'] == ftc)]
        
    if lfw == 'Overall' and fs != 'Overall' and ft == 'Overall' and ftc != 'Overall':
        
        temp_df = fuel_df[(fuel_df['Fuel_System'] == fs) & (fuel_df['Fuel_Tank_Capacity'] == ftc)]
    if lfw != 'Overall' and fs == 'Overall' and ft == 'Overall' and ftc != 'Overall':
        
        temp_df = fuel_df[(fuel_df['Low_Fuel_Warning'] == lfw) & (fuel_df['Fuel_Tank_Capacity'] == ftc)]
        
    if lfw != 'Overall' and fs == 'Overall' and ft != 'Overall' and ftc != 'Overall':
        temp_df = fuel_df[(fuel_df['Low_Fuel_Warning'] == lfw) & (fuel_df['Fuel_Tank_Capacity'] == ftc) & (fuel_df['Fuel_Type'] == ft)]
        
    if lfw != 'Overall' and fs != 'Overall' and ft != 'Overall' and ftc == 'Overall':
        temp_df = fuel_df[(fuel_df['Low_Fuel_Warning'] == lfw) & (fuel_df['Fuel_System'] == fs) & (fuel_df['Fuel_Type'] == ft)]
        
    if lfw != 'Overall' and fs != 'Overall' and ft == 'Overall' and ftc != 'Overall':
        temp_df = fuel_df[(fuel_df['Low_Fuel_Warning'] == lfw) & (fuel_df['Fuel_Tank_Capacity'] == ftc) & (fuel_df['Fuel_System'] == fs)]
        
    if lfw == 'Overall' and fs != 'Overall' and ft != 'Overall' and ftc != 'Overall':
        temp_df = fuel_df[(fuel_df['Fuel_System'] == fs) & (fuel_df['Fuel_Tank_Capacity'] == ftc) & (fuel_df['Fuel_Type'] == ft)]
        
    if lfw != 'Overall' and fs != 'Overall' and ft != 'Overall' and ftc != 'Overall':
        
        temp_df = fuel_df[(fuel_df['Low_Fuel_Warning'] == lfw) & (fuel_df['Fuel_Tank_Capacity'] == ftc) & (fuel_df['Fuel_Type'] == ft) & (fuel_df['Fuel_System'] == fs)]
        
    x = temp_df.groupby('Fuel_Type').mean()[['Low_Fuel_Warning',  'price', 'Fuel_Tank_Capacity']].sort_values('price',ascending=False).reset_index()
   
    x['Low_Fuel_Warning'] = x['Low_Fuel_Warning'].astype('int')
    x['price'] = x['price'].astype('int')
    x['Fuel_Tank_Capacity'] = x['Fuel_Tank_Capacity'].astype('int')
                                                                                   

    return x

#This function will define the columns to be taken for the respective analysis
def Family(df):
    fam_df = df.drop_duplicates(subset=['ISOFIX_(Child-Seat_Mount)', 'Child_Safety_Locks',  'Seating_Capacity', 'Boot_Space','price'])
    fam_df = fam_df.groupby('Body_Type').mean()[['ISOFIX_(Child-Seat_Mount)',  'price', 'Boot_Space','Child_Safety_Locks','Seating_Capacity']].sort_values('price',ascending=False).reset_index()
    return fam_df



def fam(df):
    cs = df['ISOFIX_(Child-Seat_Mount)'].unique().tolist()
    cs.sort()
    cs.insert(0,'Overall')
    
    body = df['Body_Type'].unique().tolist()
    body.sort()
    body.insert(0,'Overall')
    
    cl = df['Child_Safety_Locks'].unique().tolist()
    cl.sort()
    cl.insert(0,'Overall')
    
    seat = df['Seating_Capacity'].unique().tolist()
    seat.sort()
    seat.insert(0,'Overall')
    
    return cs,body,cl,seat


#It will fetch the input and display the related data
def fetch_fam_features(df, body, cs, seat, cl):
    fam_df = df.drop_duplicates(subset=['Seating_Capacity',  'price', 'ISOFIX_(Child-Seat_Mount)', 'Child_Safety_Locks'])
   
    if body == 'Overall' and cs == 'Overall' and seat == 'Overall' and cl == 'Overall':
        temp_df = fam_df
    if body == 'Overall' and cs == 'Overall' and seat == 'Overall' and cl != 'Overall':
       
        
        temp_df = fam_df[fam_df['Child_Safety_Locks'] == cl]
    if body == 'Overall' and cs == 'Overall' and seat != 'Overall' and cl == 'Overall':
        
        temp_df = fam_df[fam_df['Seating_Capacity'] == int(seat)]
    if body == 'Overall' and cs != 'Overall' and seat == 'Overall' and cl == 'Overall':
        
        temp_df = fam_df[fam_df['ISOFIX_(Child-Seat_Mount)'] == cs]
    if body != 'Overall' and cs == 'Overall' and seat == 'Overall' and cl == 'Overall':
        
        temp_df = fam_df[fam_df['Body_Type'] == body]
    
    if body != 'Overall' and cs != 'Overall' and seat == 'Overall' and cl == 'Overall':
        
        temp_df = fam_df[(fam_df['Body_Type'] == body) & (fam_df['ISOFIX_(Child-Seat_Mount)'] == cs)]
        
    if body != 'Overall' and cs == 'Overall' and seat != 'Overall' and cl == 'Overall':
        
        temp_df = fam_df[(fam_df['Body_Type'] == body) & (fam_df['Seating_Capacity'] == seat)]
        
    if body != 'Overall' and cs == 'Overall' and seat == 'Overall' and cl != 'Overall':
        
        temp_df = fam_df[(fam_df['Body_Type'] == body) & (fam_df['Child_Safety_Locks'] == cl)]
    if body != 'Overall' and cs != 'Overall' and seat == 'Overall' and cl == 'Overall':
        temp_df = fam_df[(fam_df['Body_Type'] == body) & (fam_df['ISOFIX_(Child-Seat_Mount)'] == cs)]
    if body == 'Overall' and cs != 'Overall' and seat != 'Overall' and cl == 'Overall':
        temp_df = fam_df[(fam_df['ISOFIX_(Child-Seat_Mount)'] == cs) & (fam_df['Seating_Capacity'] == seat)]
    if body == 'Overall' and cs != 'Overall' and seat == 'Overall' and cl != 'Overall':
        temp_df = fam_df[(fam_df['ISOFIX_(Child-Seat_Mount)'] == cs) & (fam_df['Child_Safety_Locks'] == cl)]
    if body != 'Overall' and cs == 'Overall' and seat != 'Overall' and cl == 'Overall':
        temp_df = fam_df[(fam_df['Seating_Capacity'] == seat) & (fam_df['Body_Type'] == body)]
    if body == 'Overall' and cs != 'Overall' and seat != 'Overall' and cl == 'Overall':
        
        temp_df = fam_df[(fam_df['Seating_Capacity'] == seat) & (fam_df['ISOFIX_(Child-Seat_Mount)'] == cs)]
    if body == 'Overall' and cs == 'Overall' and seat != 'Overall' and cl != 'Overall':
        
        temp_df = fam_df[(fam_df['Seating_Capacity'] == seat) & (fam_df['Child_Safety_Locks'] == cl)]
        
    if body == 'Overall' and cs != 'Overall' and seat == 'Overall' and cl != 'Overall':
        
        temp_df = fam_df[(fam_df['ISOFIX_(Child-Seat_Mount)'] == cs) & (fam_df['Child_Safety_Locks'] == cl)]
    if body != 'Overall' and cs == 'Overall' and seat == 'Overall' and cl != 'Overall':
        
        temp_df = fam_df[(fam_df['Body_Type'] == body) & (fam_df['Child_Safety_Locks'] == cl)]
        
    if body != 'Overall' and cs == 'Overall' and seat != 'Overall' and cl != 'Overall':
        temp_df = fam_df[(fam_df['Body_Type'] == body) & (fam_df['Child_Safety_Locks'] == cl) & (fam_df['Seating_Capacity'] == seat)]
        
    if body != 'Overall' and cs != 'Overall' and seat != 'Overall' and cl == 'Overall':
        temp_df = fam_df[(fam_df['Body_Type'] == body) & (fam_df['ISOFIX_(Child-Seat_Mount)'] == cs) & (fam_df['Seating_Capacity'] == seat)]
        
    if body != 'Overall' and cs != 'Overall' and seat == 'Overall' and cl != 'Overall':
        temp_df = fam_df[(fam_df['Body_Type'] == body) & (fam_df['Child_Safety_Locks'] == cl) & (fam_df['ISOFIX_(Child-Seat_Mount)'] == cs)]
        
    if body == 'Overall' and cs != 'Overall' and seat != 'Overall' and cl != 'Overall':
        temp_df = fam_df[(fam_df['ISOFIX_(Child-Seat_Mount)'] == cs) & (fam_df['Child_Safety_Locks'] == cl) & (fam_df['Seating_Capacity'] == seat)]
        
    if body != 'Overall' and cs != 'Overall' and seat != 'Overall' and cl != 'Overall':
        
        temp_df = fam_df[(fam_df['Body_Type'] == body) & (fam_df['Child_Safety_Locks'] == cl) & (fam_df['Seating_Capacity'] == seat) & (fam_df['ISOFIX_(Child-Seat_Mount)'] == cs)]
        
    x = temp_df.groupby('Body_Type').mean()[['ISOFIX_(Child-Seat_Mount)',  'price', 'Boot_Space','Child_Safety_Locks','Seating_Capacity']].sort_values('price',ascending=False).reset_index()
    
    x['ISOFIX_(Child-Seat_Mount)'] = x['ISOFIX_(Child-Seat_Mount)'].astype('int')
    x['price'] = x['price'].astype('int')
    x['Child_Safety_Locks'] = x['Child_Safety_Locks'].astype('int')
    x['Seating_Capacity'] = x['Seating_Capacity'].astype('int')                                                                                  

    return x

#This function will define the columns to be taken for the respective analysis
def Technology(df):
    tech_df = df.drop_duplicates(subset=['ESP_(Electronic_Stability_Program)', 'Engine_Immobilizer',  'Multifunction_Display', 'Infotainment_Screen','price','Paddle_Shifters'])
    tech_df = tech_df.groupby('Make').mean()[['Multifunction_Display',  'price', 'Engine_Immobilizer','ESP_(Electronic_Stability_Program)','Paddle_Shifters']].sort_values('price',ascending=False).reset_index()
    return tech_df



def tech(df):
    make = df['Make'].unique().tolist()
    make.sort()
    make.insert(0,'Overall')
    
    esp = df['ESP_(Electronic_Stability_Program)'].unique().tolist()
    esp.sort()
    esp.insert(0,'Overall')
    
    ps = df['Paddle_Shifters'].unique().tolist()
    ps.sort()
    ps.insert(0,'Overall')
    
    ei = df['Engine_Immobilizer'].unique().tolist()
    ei.sort()
    ei.insert(0,'Overall')
    
    return make,esp,ps,ei


#It will fetch the input and display the related data

def fetch_tech_features(df, make,esp,ps,ei):
    tech_df = df.drop_duplicates(subset=['ESP_(Electronic_Stability_Program)', 'Engine_Immobilizer',  'Multifunction_Display', 'Infotainment_Screen','price','Paddle_Shifters'])
   
    if make == 'Overall' and esp == 'Overall' and ps == 'Overall' and ei == 'Overall':
        temp_df = tech_df
    if make == 'Overall' and esp == 'Overall' and ps == 'Overall' and ei != 'Overall':
       
        
        temp_df = tech_df[tech_df['Engine_Immobilizer'] == ei]
    if make == 'Overall' and esp == 'Overall' and ps != 'Overall' and ei == 'Overall':
        
        temp_df = tech_df[tech_df['Paddle_Shifters'] == int(ps)]
    if make == 'Overall' and esp != 'Overall' and ps == 'Overall' and ei == 'Overall':
        
        temp_df = tech_df[tech_df['ESP_(Electronic_Stability_Program)'] == esp]
    if make != 'Overall' and esp == 'Overall' and ps == 'Overall' and ei == 'Overall':
        
        temp_df = tech_df[tech_df['Make'] == make]
    
    if make != 'Overall' and esp != 'Overall' and ps == 'Overall' and ei == 'Overall':
        
        temp_df = tech_df[(tech_df['Make'] == make) & (tech_df['ESP_(Electronic_Stability_Program)'] == esp)]
        
    if make != 'Overall' and esp == 'Overall' and ps != 'Overall' and ei == 'Overall':
        
        temp_df = tech_df[(tech_df['Make'] == make) & (tech_df['Paddle_Shifters'] == ps)]
        
    if make != 'Overall' and esp == 'Overall' and ps == 'Overall' and ei != 'Overall':
        
        temp_df = tech_df[(tech_df['Make'] == make) & (tech_df['Engine_Immobilizer'] == ei)]
    if make != 'Overall' and esp != 'Overall' and ps == 'Overall' and ei == 'Overall':
        temp_df = tech_df[(tech_df['Make'] == make) & (tech_df['ESP_(Electronic_Stability_Program)'] == esp)]
    if make == 'Overall' and esp != 'Overall' and ps != 'Overall' and ei == 'Overall':
        temp_df = tech_df[(tech_df['ESP_(Electronic_Stability_Program)'] == esp) & (tech_df['Paddle_Shifters'] == ps)]
    if make == 'Overall' and esp != 'Overall' and ps == 'Overall' and ei != 'Overall':
        temp_df = tech_df[(tech_df['ESP_(Electronic_Stability_Program)'] == esp) & (tech_df['Engine_Immobilizer'] == ei)]
    if make != 'Overall' and esp == 'Overall' and ps != 'Overall' and ei == 'Overall':
        temp_df = tech_df[(tech_df['Paddle_Shifters'] == ps) & (tech_df['Make'] == make)]
    if make == 'Overall' and esp != 'Overall' and ps != 'Overall' and ei == 'Overall':
        
        temp_df = tech_df[(tech_df['Paddle_Shifters'] == ps) & (tech_df['ESP_(Electronic_Stability_Program)'] == esp)]
    if make == 'Overall' and esp == 'Overall' and ps != 'Overall' and ei != 'Overall':
        
        temp_df = tech_df[(tech_df['Paddle_Shifters'] == ps) & (tech_df['Engine_Immobilizer'] == ei)]
        
    if make == 'Overall' and esp != 'Overall' and ps == 'Overall' and ei != 'Overall':
        
        temp_df = tech_df[(tech_df['ESP_(Electronic_Stability_Program)'] == esp) & (tech_df['Engine_Immobilizer'] == ei)]
    if make != 'Overall' and esp == 'Overall' and ps == 'Overall' and ei != 'Overall':
        
        temp_df = tech_df[(tech_df['Make'] == make) & (tech_df['Engine_Immobilizer'] == ei)]
        
    if make != 'Overall' and esp == 'Overall' and ps != 'Overall' and ei != 'Overall':
        temp_df = tech_df[(tech_df['Make'] == make) & (tech_df['Engine_Immobilizer'] == ei) & (tech_df['Paddle_Shifters'] == ps)]
        
    if make != 'Overall' and esp != 'Overall' and ps != 'Overall' and ei == 'Overall':
        temp_df = tech_df[(tech_df['Make'] == make) & (tech_df['ESP_(Electronic_Stability_Program)'] == esp) & (tech_df['Paddle_Shifters'] == ps)]
        
    if make != 'Overall' and esp != 'Overall' and ps == 'Overall' and ei != 'Overall':
        temp_df = tech_df[(tech_df['Make'] == make) & (tech_df['Engine_Immobilizer'] == ei) & (tech_df['ESP_(Electronic_Stability_Program)'] == esp)]
        
    if make == 'Overall' and esp != 'Overall' and ps != 'Overall' and ei != 'Overall':
        temp_df = tech_df[(tech_df['ESP_(Electronic_Stability_Program)'] == esp) & (tech_df['Engine_Immobilizer'] == ei) & (tech_df['Paddle_Shifters'] == ps)]
        
    if make != 'Overall' and esp != 'Overall' and ps != 'Overall' and ei != 'Overall':
        
        temp_df = tech_df[(tech_df['Make'] == make) & (tech_df['Engine_Immobilizer'] == ei) & (tech_df['Paddle_Shifters'] == ps) & (tech_df['ESP_(Electronic_Stability_Program)'] == esp)]
        
    x = temp_df.groupby('Make').mean()[['Multifunction_Display',  'price', 'Engine_Immobilizer','ESP_(Electronic_Stability_Program)','Paddle_Shifters']].sort_values('price',ascending=False).reset_index()
    
    
    x['ESP_(Electronic_Stability_Program)'] = x['ESP_(Electronic_Stability_Program)'].astype('int')
    x['price'] = x['price'].astype('int')
    x['Engine_Immobilizer'] = x['Engine_Immobilizer'].astype('int')
    x['Paddle_Shifters'] = x['Paddle_Shifters'].astype('int')
    x['Multifunction_Display'] = x['Multifunction_Display'].astype('int')

    return x

#This function will define the columns to be taken for the respective analysis
def cs(df1):
    cs_df1 = df1.drop_duplicates(subset=['Fuel_Tank_Capacity','Displacement','price','Power','ARAI_Certified_Mileage','cluster','Make','Model','Number_of_Airbags'])
    cs_df1 = cs_df1.groupby('Make').mean()[['Fuel_Tank_Capacity','Displacement','price','Power','ARAI_Certified_Mileage','cluster','Number_of_Airbags']].sort_values('price',ascending=False).reset_index()
    return cs_df1


def cus(df1):
    make = df1['Make'].unique().tolist()
    make.sort()
    make.insert(0,'Overall')
    
    cluster = df1['cluster'].unique().tolist()
    cluster.sort()
    cluster.insert(0,'Overall')
    
    airbag = df1['Number_of_Airbags'].unique().tolist()
    airbag.sort()
    airbag.insert(0,'Overall')
    
    fuel = df1['Fuel_Type'].unique().tolist()
    fuel.sort()
    fuel.insert(0,'Overall')
    
    return make,cluster,airbag,fuel

#It will fetch the input and display the related data
def fetch_cs_features(df1, make,cluster,airbag,fuel):
    cs_df1 = df1.drop_duplicates(subset=['Fuel_Tank_Capacity','Displacement','price','Power','ARAI_Certified_Mileage','cluster','Make','Model','Number_of_Airbags'])
   
    if make == 'Overall' and cluster == 'Overall' and airbag == 'Overall' and fuel == 'Overall':
        temp_df = cs_df1
    if make == 'Overall' and cluster == 'Overall' and airbag == 'Overall' and fuel != 'Overall':
       
        
        temp_df = cs_df1[cs_df1['Fuel_Type'] == fuel]
    if make == 'Overall' and cluster == 'Overall' and airbag != 'Overall' and fuel == 'Overall':
        
        temp_df = cs_df1[cs_df1['Number_of_Airbags'] == int(airbag)]
    if make == 'Overall' and cluster != 'Overall' and airbag == 'Overall' and fuel == 'Overall':
        
        temp_df = cs_df1[cs_df1['cluster'] == cluster]
    if make != 'Overall' and cluster == 'Overall' and airbag == 'Overall' and fuel == 'Overall':
        
        temp_df = cs_df1[cs_df1['Make'] == make]
    
    if make != 'Overall' and cluster != 'Overall' and airbag == 'Overall' and fuel == 'Overall':
        
        temp_df = cs_df1[(cs_df1['Make'] == make) & (cs_df1['cluster'] == cluster)]
        
    if make != 'Overall' and cluster == 'Overall' and airbag != 'Overall' and fuel == 'Overall':
        
        temp_df = cs_df1[(cs_df1['Make'] == make) & (cs_df1['Number_of_Airbags'] == airbag)]
        
    if make != 'Overall' and cluster == 'Overall' and airbag == 'Overall' and fuel != 'Overall':
        
        temp_df = cs_df1[(cs_df1['Make'] == make) & (cs_df1['Fuel_Type'] == fuel)]
    if make != 'Overall' and cluster != 'Overall' and airbag == 'Overall' and fuel == 'Overall':
        temp_df = cs_df1[(cs_df1['Make'] == make) & (cs_df1['cluster'] == cluster)]
    if make == 'Overall' and cluster != 'Overall' and airbag != 'Overall' and fuel == 'Overall':
        temp_df = cs_df1[(cs_df1['cluster'] == cluster) & (cs_df1['Number_of_Airbags'] == airbag)]
    if make == 'Overall' and cluster != 'Overall' and airbag == 'Overall' and fuel != 'Overall':
        temp_df = cs_df1[(cs_df1['cluster'] == cluster) & (cs_df1['Fuel_Type'] == fuel)]
    if make != 'Overall' and cluster == 'Overall' and airbag != 'Overall' and fuel == 'Overall':
        temp_df = cs_df1[(cs_df1['Number_of_Airbags'] == airbag) & (cs_df1['Make'] == make)]
    if make == 'Overall' and cluster != 'Overall' and airbag != 'Overall' and fuel == 'Overall':
        
        temp_df = cs_df1[(cs_df1['Number_of_Airbags'] == airbag) & (cs_df1['cluster'] == cluster)]
    if make == 'Overall' and cluster == 'Overall' and airbag != 'Overall' and fuel != 'Overall':
        
        temp_df = cs_df1[(cs_df1['Number_of_Airbags'] == airbag) & (cs_df1['Fuel_Type'] == fuel)]
        
    if make == 'Overall' and cluster != 'Overall' and airbag == 'Overall' and fuel != 'Overall':
        
        temp_df = cs_df1[(cs_df1['cluster'] == cluster) & (cs_df1['Fuel_Type'] == fuel)]
    if make != 'Overall' and cluster == 'Overall' and airbag == 'Overall' and fuel != 'Overall':
        
        temp_df = cs_df1[(cs_df1['Make'] == make) & (cs_df1['Fuel_Type'] == fuel)]
        
    if make != 'Overall' and cluster == 'Overall' and airbag != 'Overall' and fuel != 'Overall':
        temp_df = cs_df1[(cs_df1['Make'] == make) & (cs_df1['Fuel_Type'] == fuel) & (cs_df1['Number_of_Airbags'] == airbag)]
        
    if make != 'Overall' and cluster != 'Overall' and airbag != 'Overall' and fuel == 'Overall':
        temp_df = cs_df1[(cs_df1['Make'] == make) & (cs_df1['cluster'] == cluster) & (cs_df1['Number_of_Airbags'] == airbag)]
        
    if make != 'Overall' and cluster != 'Overall' and airbag == 'Overall' and fuel != 'Overall':
        temp_df = cs_df1[(cs_df1['Make'] == make) & (cs_df1['Fuel_Type'] == fuel) & (cs_df1['cluster'] == cluster)]
        
    if make == 'Overall' and cluster != 'Overall' and airbag != 'Overall' and fuel != 'Overall':
        temp_df = cs_df1[(cs_df1['cluster'] == cluster) & (cs_df1['Fuel_Type'] == fuel) & (cs_df1['Number_of_Airbags'] == airbag)]
        
    if make != 'Overall' and cluster != 'Overall' and airbag != 'Overall' and fuel != 'Overall':
        
        temp_df = cs_df1[(cs_df1['Make'] == make) & (cs_df1['Fuel_Type'] == fuel) & (cs_df1['Number_of_Airbags'] == airbag) & (cs_df1['cluster'] == cluster)]
        
    x = temp_df.groupby('Make').mean()[['Fuel_Tank_Capacity','Displacement','price','Power','ARAI_Certified_Mileage','cluster','Number_of_Airbags']].sort_values('price',ascending=False).reset_index()
    
    
    x['cluster'] = x['cluster'].astype('int')
    x['price'] = x['price'].astype('int')
    x['Displacement'] = x['Displacement'].astype('int')
    x['Fuel_Tank_Capacity'] = x['Fuel_Tank_Capacity'].astype('int')
    x['Number_of_Airbags'] = x['Number_of_Airbags'].astype('int')
    x['Power'] = x['Power'].astype('int')
    x['ARAI_Certified_Mileage'] = x['ARAI_Certified_Mileage'].astype('int')
    

    return x




# This fuinction predicts the price according to the given inputs
def predict_forest(model, ARAI_Certified_Mileage ,Displacement, Cylinders,Power,Torque,PGM_Fi,Fuel_Tank_Capacity,Doors,Seating_Capacity,Number_of_Airbags):
    input=np.array([[ARAI_Certified_Mileage ,Displacement, Cylinders,Power,Torque,PGM_Fi,Fuel_Tank_Capacity,Doors,Seating_Capacity,Number_of_Airbags]]).astype(np.int64)
    prediction=model.predict(input)
    #pred='{0:.{1}f}'.format(prediction[0][0], 2)
    prediction = prediction*78
    return int(prediction)









