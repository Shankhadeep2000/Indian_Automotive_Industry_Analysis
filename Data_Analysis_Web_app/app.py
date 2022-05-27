# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:59:50 2022

@author: Shankhadeep Sarkar
"""
#Importing the python libraries

#for web app
import streamlit as st 
#for read csv file
import pandas as pd  
#additional pages with different functions
import preproceser,helper
#for graph creation
import plotly.express as px 
#For mathematical funtions
import numpy as np
#for importing ml model
import pickle
#For graph creation
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
#Fir creating navigation bar
from streamlit_option_menu import option_menu
#for image useage
from PIL import Image

#Customizing the icon of the web page

img = Image.open('da.png')

#Set the name of the web page and applying the icon  

st.set_page_config(page_title = "Indian Automotive Industry Analysis" , page_icon = img)

#Creating the navigation bar with option_menu library of streamlit

selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Analysis", "Price Prediction", "Links"],  # required
            icons=["house", "clipboard-data", "qr-code-scan","link"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="vertical",
            styles={
                "container": {"background-color": "#FDFEFE"},
                "icon": {"color": "Black", "font-size": "15px"},
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "Center",
                    "margin": "0px",
                    "--hover-color": "#e87e76",
                },
                "nav-link-selected": {"background-color": "#EA4228"},
            },
        )
   

#Creating the each nav-bar option i.e. what that option will show

if selected == "Home":
    st.title("How the Automotive Industry could harness data to take informed decisions?")
    st.write("The Automotive Industry continues to face a dynamic set of challenges. For those with right ambition it represents an exiting time with opportunities to differentiate and stand out from the crowd. One area that has the opportunity to deliver significant competitive advantage is analytics. At present, automotive companies are capable of collecting and analyzing an enormous amount of raw data. Advancements in data analytics and its fusion with the automotive industry has led to smarter, more connected vehicles, and drastic improvements in sales and marketing. ")
    st.write("IHS Automotive has estimated that an average car produces approximately 30 terabytes of data daily. The onus is then on manufacturers to effectively use the data for competitive advantage. Since so much data is produced, the automotive industry today has turned into a data-driven industry. Thus, automobile manufacturers can use data analytics software to glean new insights into their business and make better decisions, which can then be used to maintain and expand market position and profits.")
    # car image in the web app
    st.image("rm117-nap-08.jpg")
    '''
    * Designs and Productions:
        * Data science and Data analysis is now being used extensively by manufacturers to improve many aspects of their business processes. For example, once the proper sensors are installed in a vehicle, predictive analytics can easily be used by engineers to view and predict potential issues before they become problems. Therefore, they can advise the customer to go for an early service.
        * With regard to vehicle design, car manufacturing companies are now using data analytic tools to assist the design process by analyzing the performance models to determine the optimal aerodynamics for future models.
    * Sales and Marketing:
        * Another critical use for data analytics in the automotive industry is in personalizing and targeting marketing and sales. Automotive companies understand the value of their customer’s trust and loyalty, and effective usage of data allows an unparalleled customer experience.
        * Predictive analytics is very much in play in the aftermarket services such as maintenance and personalization services, all are being integrated with data analytics in order to provide customers with ever greater levels of service.
        * Additionally, predictive analytics can help the automotive companies to give real-time feedback to the customers, and use it as historical data which then help improve their services in the future.
        
    * Essential Takeaways:
        * We are now living in a time of automotive innovation. From fully electric cars to self-driving vehicles powered by A.I, innovation we could only imagine in the past is becoming part of our daily lives. This has changed our world, and we can thank data analytics for playing a key role in this shift. It has now become critical that all automotive businesses make full use of data analytics to optimise their manufacturing, customer service and other business areas.
        * Thanks to the data-driven age we are living in, data analytics software is now able to help the automotive industry to design and build better cars today, and help make the cars of the future a reality.
        
    '''
    st.title("Data")
    '''
    * The [Dataset](https://acehacker.com/microsoft/engage2022/cars_engage_2022.csv) used in this project is provided by Microsoft Engage Program.The dataset used in this report is having the latest information about cars in the Indian market. The dataset contains cars with their variants, In dataset there are 1200+ model/variants to study. There is a variety of Makes/Models which can be studied, All prices has been converted from indian rupee to USD.
    '''
 # starting the main block of the web page that is analysis which will show the exploretary analysis and cluster analysis
    
if selected == "Analysis":
    df = pd.read_csv('final_df3.csv') #importing the datset
    df = preproceser.preprocess(df)
    st.sidebar.image("rm117-nap-35.jpg")
    st.sidebar.title("Indian Car Market Analysis")

#Creating the sidebar menu for selecting the analysis basis

    user_menu = st.sidebar.radio(
        'Select an Option',
        ('Engine Performace Wise Analysis','Body Type Wise Analysis', 'Safety Wise Analysis','Fuel Wise Analysis','New Technology Wise Analysis','Family Features Wise Analysis','Customer Segmentation')
        )

#Creating the working statement Engine performance to show the respective analysis 

    if user_menu == 'Engine Performace Wise Analysis':
        st.sidebar.header("Engine Performance")
        body,cylinder = helper.Body_cylinder(df)
        
        selected_body = st.sidebar.selectbox("Select the body type",body)
        selected_cylinder = st.sidebar.selectbox("Select the number of Cylinder",cylinder)
        
        engine_performance = helper.fetch_medal_tally(df, selected_cylinder, selected_body)
 # statements based on different conditions       
        if selected_cylinder == 'Overall' and selected_body == 'Overall':
            st.title("Overall Engine Performance")
        if selected_cylinder != 'Overall' and selected_body == 'Overall':
            st.title("Engine performance with respect to " + str(selected_cylinder) + " Cylinders")
        if selected_cylinder == 'Overall' and selected_body != 'Overall':
            st.title(selected_body + " Engine Performance")
        if selected_cylinder != 'Overall' and selected_body != 'Overall':
            st.title("Engine Performance of "+ selected_body + " with " + str(selected_cylinder) + " Cylinders")
        st.table(engine_performance)
        
   #Creating Graphs for the analysis with the help of plotly     
        if selected_body == 'Overall':
            fig = px.scatter(df, x='price', y="Power", color= 'Body_Type' , hover_data=['price'])
            st.header("Graph between price and power with respect "+selected_body+"Body type")
            st.plotly_chart(fig)
        else:
            df = df[df['Body_Type'] == selected_body]
            fig = px.scatter(df, x='price', y="Power", color= 'Body_Type' , hover_data=['price'])
            st.header("Graph between price and power with respect "+selected_body+"Body type")
            st.plotly_chart(fig)
        
        if selected_cylinder == 'Overall':
            fig = px.scatter(df, x='price', y="Power", color= 'Cylinders' , hover_data=['price'])
            st.header("Graph between price and power with respect "+str(selected_cylinder)+"Number of cylinders")
            st.plotly_chart(fig)
        else:
            df = df[df['Cylinders'] == selected_cylinder]
            fig = px.scatter(df, x='price', y="Power", color= 'Cylinders' , hover_data=['price'])
            st.header("Graph between price and power with respect "+str(selected_cylinder)+"Number of cylinders")
            st.plotly_chart(fig)
            
        
        #st.dataframe(engine_performance)
        
 ##Creating the working statement for Body type  to show the respective analysis
       
    if user_menu == 'Body Type Wise Analysis':
        st.sidebar.header("Analysis Based On Body Type")
        body,make,fuel,seat = helper.body_make_fuel(df)
        
        selected_body = st.sidebar.selectbox("Select the Body Type",body)
        selected_make = st.sidebar.selectbox("Select the Manufacturer",make)
        selected_fuel = st.sidebar.selectbox("Select the Fuel Type",fuel)
        selected_seat = st.sidebar.selectbox("Select the Seat Capacity",seat)
        
        body_type = helper.fetch_body_type(df, selected_make, selected_body, selected_seat, selected_fuel)
        
        if selected_body == 'Overall' and selected_make == 'Overall' and selected_fuel == 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on Body Type")
            
        if selected_body != 'Overall' and selected_make == 'Overall' and selected_fuel == 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ selected_body+ " Body Type")
        
        if selected_body == 'Overall' and selected_make != 'Overall' and selected_fuel == 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ selected_make+ " maker ")
            
        if selected_body == 'Overall' and selected_make == 'Overall' and selected_fuel != 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ selected_fuel+ " fuel type ")

        if selected_body == 'Overall' and selected_make == 'Overall' and selected_fuel == 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_seat)+ " No of Seats ")

        if selected_body != 'Overall' and selected_make != 'Overall' and selected_fuel == 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ selected_make+ " maker and " + selected_body + " Body Type" )

        if selected_body != 'Overall' and selected_make == 'Overall' and selected_fuel != 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ selected_body+ " body type and " + selected_fuel + "fuel type")

        if selected_body != 'Overall' and selected_make == 'Overall' and selected_fuel == 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ selected_body+ " body type and " + str(selected_seat) + " No of Seats")
            
        if selected_body == 'Overall' and selected_make != 'Overall' and selected_fuel != 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ selected_make+ " maker and "+ selected_fuel + " Fuel type")        
        
        if selected_body == 'Overall' and selected_make != 'Overall' and selected_fuel != 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ selected_make+ " maker and "+ str(selected_seat) + " No of Seats and "+ selected_fuel +"fuel type.")
        
        if selected_body == 'Overall' and selected_make != 'Overall' and selected_fuel == 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ selected_make+ " maker and "+ str(selected_seat) + " No of Seats") 

        if selected_body == 'Overall' and selected_make == 'Overall' and selected_fuel != 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ selected_make+ " maker and "+ str(selected_seat) + " No of Seats ") 

        if selected_body != 'Overall' and selected_make != 'Overall' and selected_fuel != 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ selected_make+ " maker and "+ selected_fuel + " Fuel type and "+ selected_body + " Body Type" + str(selected_seat) + " No of Seats" )

        
  # Creating 3d graph to show the analysis based on different values        
        st.table(body_type)
        
        if selected_body == 'Overall':
            
            fig = px.scatter_3d(df, x='price', y='Power', z='Seating_Capacity', color='Body_Type',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Power Price and Seat Capacity "+str(selected_body)+" Body Type")
            
            st.plotly_chart(fig)
        else:
            df = df[df['Body_Type'] == selected_body]
            fig = px.scatter_3d(df, x='price', y='Power', z='Seating_Capacity', color='Body_Type',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Power Price and Seat Capacity "+str(selected_body)+" Body Type")
            st.plotly_chart(fig)
            
        
        if selected_make == 'Overall':
            
            fig = px.scatter_3d(df, x='price', y='Power', z='Seating_Capacity', color='Make',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Power Price and Seat Capacity "+str(selected_make)+" Manufacturer")
            st.plotly_chart(fig)
        else:
            df = df[df['Make'] == selected_make]
            fig = px.scatter_3d(df, x='price', y='Power', z='Seating_Capacity', color='Make',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Power Price and Seat Capacity "+str(selected_make)+" Manufacturer")
            st.plotly_chart(fig)
            
        
        if selected_fuel == 'Overall':
            
            fig = px.scatter_3d(df, x='price', y='Power', z='Seating_Capacity', color='Fuel_Type',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Power Price and Seat Capacity "+str(selected_fuel)+" FuelType")
            st.plotly_chart(fig)
        else:
            df = df[df['Fuel_Type'] == selected_fuel]
            fig = px.scatter_3d(df, x='price', y='Power', z='Seating_Capacity', color='Fuel_Type',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Power Price and Seat Capacity "+str(selected_fuel)+" Fuel Type")
            st.plotly_chart(fig)
            
            
        if selected_seat == 'Overall':
            
            fig = px.scatter_3d(df, x='price', y='Power', z='Seating_Capacity', color='Body_Type',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Power Price and Seat Capacity "+str(selected_seat)+" No of seats")
            st.plotly_chart(fig)
        else:
            df = df[df['Seating_Capacity'] == selected_seat]
            fig = px.scatter_3d(df, x='price', y='Power', z='Seating_Capacity', color='Body_Type',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Power Price and Seat Capacity "+str(selected_seat)+" No of seats")
            st.plotly_chart(fig)
            

    if user_menu == 'Safety Wise Analysis':
        st.sidebar.header("Analysis Based On Safety Precaution (where 1 means the feature is present and 0 means the feature is not present)")
        airbag,eba,ebd,abso = helper.safe(df)
        
        selected_airbag = st.sidebar.selectbox("Select the number of airbags",airbag)
        selected_eba = st.sidebar.selectbox("Select the Electronic Brake Assist",eba)
        selected_ebd = st.sidebar.selectbox("Select the Electronic Brake force Distribution",ebd)
        selected_abso = st.sidebar.selectbox("Select the Anti lock Braking System",abso)
        
        Safety = helper.fetch_safety_type(df, selected_eba, selected_airbag, selected_abso, selected_ebd)
        
        if selected_airbag == 'Overall' and selected_eba == 'Overall' and selected_ebd == 'Overall' and selected_abso == 'Overall':
            st.title(" Analysis Based on Overall Safety Feature")
            
        if selected_airbag != 'Overall' and selected_eba == 'Overall' and selected_ebd == 'Overall' and selected_abso == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_airbag)+ " No of Airbags ")
        
        if selected_airbag == 'Overall' and selected_eba != 'Overall' and selected_ebd == 'Overall' and selected_abso == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_eba)+ " Electronic Brake Assist ")
            
        if selected_airbag == 'Overall' and selected_eba == 'Overall' and selected_ebd != 'Overall' and selected_abso == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_ebd)+ " Electronic Brake force Distribution ")

        if selected_airbag == 'Overall' and selected_eba == 'Overall' and selected_ebd == 'Overall' and selected_abso != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_abso)+ " Anti-lock_Braking_System ")

        if selected_airbag != 'Overall' and selected_eba != 'Overall' and selected_ebd == 'Overall' and selected_abso == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_eba)+ " Electronic Brake Assist and " + str(selected_airbag) + " No of Airbags" )

        if selected_airbag != 'Overall' and selected_eba == 'Overall' and selected_ebd != 'Overall' and selected_abso == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_airbag)+ " No of Airbags and " + str(selected_ebd) + "Electronic Brake force Distribution")

        if selected_airbag != 'Overall' and selected_eba == 'Overall' and selected_ebd == 'Overall' and selected_abso != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_airbag)+ " No of Airbags and " + str(selected_abso) + " Anti-lock_Braking_System")
            
        if selected_airbag == 'Overall' and selected_eba != 'Overall' and selected_ebd != 'Overall' and selected_abso == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_eba)+ " Electronic Brake Assist and "+ str(selected_ebd) + " Electronic Brake force Distribution")        
        
        if selected_airbag == 'Overall' and selected_eba != 'Overall' and selected_ebd != 'Overall' and selected_abso != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_eba)+ " Electronic Brake Assist and "+ str(selected_abso) + " Anti-lock_Braking_System and "+ str(selected_ebd) +"Electronic Brake force Distribution.")
        
        if selected_airbag == 'Overall' and selected_eba != 'Overall' and selected_ebd == 'Overall' and selected_abso != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_eba)+ " Electronic Brake Assist and "+ str(selected_abso) + " Anti-lock_Braking_System") 

        if selected_airbag == 'Overall' and selected_eba == 'Overall' and selected_ebd != 'Overall' and selected_abso != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_eba)+ " Electronic Brake Assist and "+ str(selected_abso) + " Anti-lock_Braking_System ") 

        if selected_airbag != 'Overall' and selected_eba != 'Overall' and selected_ebd != 'Overall' and selected_abso != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_eba)+ " Electronic Brake Assist and "+ str(selected_ebd) + " Electronic Brake force Distribution and "+ str(selected_airbag) + " No of Airbags" + str(selected_abso) + " Anti-lock_Braking_System" )
        
       
        st.table(Safety)
        
        if selected_airbag == 'Overall':
            
            fig = px.bar(df, x='Number_of_Airbags',y='price',color='Body_Type')
            
            st.header("Analysis between number of Airbag  and price "+str(selected_airbag)+" No of airbags")
            st.plotly_chart(fig)
        else:
            df = df[df['Number_of_Airbags'] == selected_airbag]
            fig = px.bar(df, x='Number_of_Airbags',y='price',color='Body_Type')
            st.header("Analysis between price and  "+str(selected_airbag)+" No of airbags")
            st.plotly_chart(fig)
            
    # We are not filtering it with the basis of sidebar data input because it is a categorical values so ditribution is enough.

        fig = px.bar(df, x='EBA_(Electronic_Brake_Assist)',y='price',color='Body_Type')
        
        st.header("Analysis between price and Overall Electronic Brake Assist")
        st.plotly_chart(fig)
        
        fig = px.bar(df, x='EBD_(Electronic_Brake-force_Distribution)',y='price',color='Body_Type')
        
        st.header("Analysis between  price and Overall EBD_(Electronic Brake force Distribution)")
        st.plotly_chart(fig)
            
        fig = px.bar(df, x='ABS_(Anti-lock_Braking_System)',y='price',color='Body_Type')
        
        st.header("Analysis between price and Overall Anti lock Braking System")
        st.plotly_chart(fig)
        
                
                
        
        
    if user_menu == 'Fuel Wise Analysis':
        st.sidebar.header("Analysis Based On Fuel Features (where 1 means the feature is present and 0 means the feature is not present)")
        fs,lfw,ftc,ft = helper.fuel(df)
        
        selected_fs = st.sidebar.selectbox("Select the type of fuel system ",fs)
        selected_lfw = st.sidebar.selectbox("Select the availability of low fuel warning feature",lfw)
        selected_ftc = st.sidebar.selectbox("Select the fuel tank capacity",ftc)
        selected_ft = st.sidebar.selectbox("Select the fuel type",ft)
        
        f_uel = helper.fetch_fuel_features(df, selected_lfw, selected_fs, selected_ft, selected_ftc)
        
        if selected_fs == 'Overall' and selected_lfw == 'Overall' and selected_ftc == 'Overall' and selected_ft == 'Overall':
            st.title(" Analysis Based on Overall Fuel Feature")
            
        if selected_fs != 'Overall' and selected_lfw == 'Overall' and selected_ftc == 'Overall' and selected_ft == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_fs)+ " Fuel System ")
        
        if selected_fs == 'Overall' and selected_lfw != 'Overall' and selected_ftc == 'Overall' and selected_ft == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_lfw)+ " Low fuel warning ")
            
        if selected_fs == 'Overall' and selected_lfw == 'Overall' and selected_ftc != 'Overall' and selected_ft == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_ftc)+ " Fuel tank capacity ")

        if selected_fs == 'Overall' and selected_lfw == 'Overall' and selected_ftc == 'Overall' and selected_ft != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_ft)+ " Fuel type ")

        if selected_fs != 'Overall' and selected_lfw != 'Overall' and selected_ftc == 'Overall' and selected_ft == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_lfw)+ " Low fuel warning and " + str(selected_fs) + " Fuel System" )

        if selected_fs != 'Overall' and selected_lfw == 'Overall' and selected_ftc != 'Overall' and selected_ft == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_fs)+ " Fuel System and " + str(selected_ftc) + "Fuel tank capacity")

        if selected_fs != 'Overall' and selected_lfw == 'Overall' and selected_ftc == 'Overall' and selected_ft != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_fs)+ " Fuel System and " + str(selected_ft) + " Fuel type")
            
        if selected_fs == 'Overall' and selected_lfw != 'Overall' and selected_ftc != 'Overall' and selected_ft == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_lfw)+ " Low fuel warning and "+ str(selected_ftc) + " Fuel tank capacity")        
        
        if selected_fs == 'Overall' and selected_lfw != 'Overall' and selected_ftc != 'Overall' and selected_ft != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_lfw)+ " Low fuel warning and "+ str(selected_ft) + " Fuel type and "+ str(selected_ftc) +"Fuel tank capacity.")
        
        if selected_fs == 'Overall' and selected_lfw != 'Overall' and selected_ftc == 'Overall' and selected_ft != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_lfw)+ " Low fuel warning and "+ str(selected_ft) + " Fuel type") 

        if selected_fs == 'Overall' and selected_lfw == 'Overall' and selected_ftc != 'Overall' and selected_ft != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_lfw)+ " Low fuel warning and "+ str(selected_ft) + " Fuel type ") 

        if selected_fs != 'Overall' and selected_lfw != 'Overall' and selected_ftc != 'Overall' and selected_ft != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_lfw)+ " Low fuel warning and "+ str(selected_ftc) + " Fuel tank capacity and "+ str(selected_fs) + " Fuel System" + str(selected_ft) + " Fuel type" )
        
        
        st.table(f_uel)
        
        fig = px.bar(df, x='Fuel_System',y='price',color='Body_Type')
        st.header("Analysis between price and Overall Fuel System")
        st.plotly_chart(fig)
        
        fig = px.bar(df, x='Low_Fuel_Warning',y='price',color='Body_Type')
        st.header("Analysis between price and Overall Low Fuel Warning")
        st.plotly_chart(fig)
        
        if selected_ftc == 'Overall':
            fig = px.scatter(df, x='Fuel_Tank_Capacity', y="price", color= 'Body_Type' , hover_data=['price'])
            st.header("Graph between price and Fuel Tank Capacity with respect "+str(selected_ftc)+" Fuel Tank Capacity")
            st.plotly_chart(fig)
        else:
            df = df[df['Fuel_Tank_Capacity'] == selected_ftc]
            fig = px.scatter(df, x='Fuel_Tank_Capacity', y="price", color= 'Body_Type' , hover_data=['price'])
            st.header("Graph between price and Fuel Tank Capacity with respect "+str(selected_ftc)+" Fuel Tank Capacity")
            st.plotly_chart(fig)
            
        if selected_ft == 'Overall':
            fig = px.bar(df, x='Fuel_Type',y='price',color='Body_Type')
            st.header("Graph between price and  "+str(selected_ft)+" Fuel Type")
            st.plotly_chart(fig)
        else:
            df = df[df['Fuel_Type'] == selected_ft]
            fig = px.bar(df, x='Fuel_Type', y="price", color= 'Body_Type' , hover_data=['price'])
            st.header("Graph between price and  "+str(selected_ft)+" Fuel Type")
            st.plotly_chart(fig)
            
        
        
        

    if user_menu == 'Family Features Wise Analysis':
        st.sidebar.header("Analysis Based On Family Features (where 1 means the feature is present and 0 means the feature is not present)")
        cs,body,cl,seat = helper.fam(df)
        
        selected_cs = st.sidebar.selectbox("Select the availability of extra child seat ",cs)
        selected_body = st.sidebar.selectbox("Select the Body type",body)
        selected_cl = st.sidebar.selectbox("Select the availability of child lock ",cl)
        selected_seat = st.sidebar.selectbox("Select the number of seats ",seat)
        
        fami = helper.fetch_fam_features(df,selected_body,selected_cs,selected_seat,selected_cl)
        
        if selected_cs == 'Overall' and selected_body == 'Overall' and selected_cl == 'Overall' and selected_seat == 'Overall':
            st.title(" Analysis Based on Overall Family Feature")
            
        if selected_cs != 'Overall' and selected_body == 'Overall' and selected_cl == 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cs)+ " Child seat ")
        
        if selected_cs == 'Overall' and selected_body != 'Overall' and selected_cl == 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_body)+ " Body type ")
            
        if selected_cs == 'Overall' and selected_body == 'Overall' and selected_cl != 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cl)+ " child lock ")

        if selected_cs == 'Overall' and selected_body == 'Overall' and selected_cl == 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_seat)+ " number of seat ")

        if selected_cs != 'Overall' and selected_body != 'Overall' and selected_cl == 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_body)+ " Body type and " + str(selected_cs) + " Child seat" )

        if selected_cs != 'Overall' and selected_body == 'Overall' and selected_cl != 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cs)+ " Child seat and " + str(selected_cl) + "child lock")

        if selected_cs != 'Overall' and selected_body == 'Overall' and selected_cl == 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cs)+ " Child seat and " + str(selected_seat) + " number of seat")
            
        if selected_cs == 'Overall' and selected_body != 'Overall' and selected_cl != 'Overall' and selected_seat == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_body)+ " Body type and "+ str(selected_cl) + " child lock")        
        
        if selected_cs == 'Overall' and selected_body != 'Overall' and selected_cl != 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_body)+ " Body type and "+ str(selected_seat) + " number of seat and "+ str(selected_cl) +"child lock.")
        
        if selected_cs == 'Overall' and selected_body != 'Overall' and selected_cl == 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_body)+ " Body type and "+ str(selected_seat) + " number of seat") 

        if selected_cs == 'Overall' and selected_body == 'Overall' and selected_cl != 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_body)+ " Body type and "+ str(selected_seat) + " number of seat ") 

        if selected_cs != 'Overall' and selected_body != 'Overall' and selected_cl != 'Overall' and selected_seat != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_body)+ " Body type and "+ str(selected_cl) + " child lock and "+ str(selected_cs) + " Child seat" + str(selected_seat) + " number of seat" )
        
       
        st.table(fami)
        
        if selected_seat == 'Overall' and selected_body == 'Overall':
           fig = px.scatter_3d(df, x='Seating_Capacity', y="Boot_Space", z="price", color= 'Body_Type' , hover_data=['price'])
           fig.update_layout(scene_zaxis_type="log")
           st.header("Graph between price , Boot Space with  "+str(selected_seat)+" Number of seats and "+selected_body+ " Body Type")
           st.plotly_chart(fig)
        if selected_seat != 'Overall' and selected_body == 'Overall':
           df = df[df['Seating_Capacity'] == selected_seat]
           fig = px.scatter_3d(df, x='Seating_Capacity', y="Boot_Space", z="price", color= 'Body_Type' , hover_data=['price'])
           fig.update_layout(scene_zaxis_type="log")
           st.header("Graph between price , Boot Space with  "+str(selected_seat)+" Number of seats"+selected_body+ " Body Type")
           st.plotly_chart(fig)
           
        if selected_seat == 'Overall' and selected_body != 'Overall':
            df = df[df['Body_Type'] == selected_body]
            fig = px.scatter_3d(df, x='Seating_Capacity', y="Boot_Space", z="price", color= 'Body_Type' , hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Graph between price , Boot Space with  "+str(selected_seat)+" Number of seats"+selected_body+ " Body Type")
            st.plotly_chart(fig)
            
        if selected_seat != 'Overall' and selected_body != 'Overall':
            df = df[df['Body_Type'] == selected_body]
            df = df[df['Seating_Capacity'] == selected_seat]
            fig = px.scatter_3d(df, x='Seating_Capacity', y="Boot_Space", z="price", color= 'Body_Type' , hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Graph between price , Boot Space with  "+str(selected_seat)+" Number of seats"+selected_body+ " Body Type")
            st.plotly_chart(fig)
            
        fig = px.bar(df, x='ISOFIX_(Child-Seat_Mount)', y="price", color= 'Body_Type' , hover_data=['price'])
        st.header("Graph between price and  "+str(selected_cs)+" Child seat")
        st.plotly_chart(fig)
        
        fig = px.bar(df, x='Child_Safety_Locks', y="price", color= 'Body_Type' , hover_data=['price'])
        st.header("Graph between price and  "+str(selected_cs)+" Child Lock")
        st.plotly_chart(fig)
        
        st.title("Summary of above analaysis")
        '''
        * Based on Following:
            * Engine Performace Wise Analysis 
            * Body Type Wise Analysis , Safety Wise Analysis 
            * Fuel Wise Analysis , New Technology Wise Analysis 
            * Family Features Wise Analysis 
            * Customer Segmentation 
        '''
        st.write("we can say that indian Market has many varients of cars with different type of body type and different features.The Top 5 companies with more than car variants in India are Maruti Suzuki, Hyundai, Mahindra, Tata, and Toyota. Though we can say that most favourable body type in indian market is Hatchbacks and SUV. Most of the cars are having petrol and diesel as their fuel type. Power is an importent feature price increase with the power but mileage decrease whith increasing power.Torque is directly propostional to power hence it is also propostion to price.From the above data we also get to know that cars in Indian market has decent horsepower. Indian market loves car with decent values of power and performence of the engine. Ex-Showroom price is positively correlated to Displacement.Ex-Showroom Price is Positively Correlated to the number of Cylinders. This means, more the number of cylinders, more the ex-showroom price.The more the number of cylinders in a car, the more will be its displacement. Generally speaking, the higher an engine’s displacement the more power it can create.The number of doors is highly negatively correlated with Displacement. That makes sense, right since sports car has less number of doors and its mileage is very less and the power is very high including price. Now lets look into features like new technologies and safety and other features. Indian market is catching up to most of new technology. Most of the cars are having power steering with electric or hydraulic power.Almost all cars have power window. Keyless entry is also present in most of the cars.Indian also prefer audio system and bluetooth in their car Most of the cars have 4-10 number of seats which means Indian buyer loves big cars which makes sense since most favourables cars in indian market are SUV and Hatchbacks. Buyers do like leather as their seat fabric. Most of the cars are automatic and hence tells us that Indian market is moving towards automation. Indain market has also uses advanced feature for brake system, theft proof system , Multifunction Display etc. For aadvanced brake system:-EBA_(Electronic_Brake_Assist),EBD_(Electronic_Brake-force_Distribution) these technologies are present in most of the cars which is also good for safety purpose. But on the same hand It is does not have ESP,EBA which is also new technologies hence we can say Indian market has decsnt or average amount of cars with new technology. For theft system:- most of the cars are having Engine Immobilizer which only activates engine if the correct key is being inserted.We can say that half of the Indian buyers are having family since 40 % of indian buyers are having ISOFIX_(Child-Seat_Mount) feature which is an extra seat attached on the back seat for kids and having Child Safety Locks. In the field of safety most of the cars has decent or average safety since Indian buyers are fond of budget cars and hence most of the cars has 1 air bag and cars with 5 airbags are less in numbers which has high price.")
            
    if user_menu == 'Customer Segmentation':
        df1 = pd.read_csv('df_cluster.csv')
        
        col1,col2 = st.columns(2)
        with col1:
            st.header("Number of Cluster")
            st.title('4 Clusters')
        with col2:
            st.header("cluster with high count")
            st.title('2')
        
    
        
        fig = px.histogram(df1, x='cluster' , hover_data=['price'])
        st.header("Graph of cluster count[which cluster is more in Indian market]")
        st.plotly_chart(fig)
        
       
        
        fig = px.bar(df1, x='cluster',y= 'price' , hover_data=['price'])
        st.header("Graph of cluster vs price")
        st.plotly_chart(fig)
        
        st.sidebar.header("Customer Segmentation with the help of Cluster Analysis")
        make,cluster,airbag,fuel = helper.cus(df1)
        
        
        selected_make = st.sidebar.selectbox("Select the manufacturer ",make)
        selected_cluster = st.sidebar.selectbox("Select the Cluster",cluster)
        selected_airbag = st.sidebar.selectbox("Select the Number of airbags ", airbag)
        selected_fuel = st.sidebar.selectbox("Select the type of fuel ",fuel)
        
        cusi = helper.fetch_cs_features(df1, selected_make, selected_cluster, selected_airbag, selected_fuel)
        
        if selected_make == 'Overall' and selected_cluster == 'Overall' and selected_airbag == 'Overall' and selected_fuel == 'Overall':
            st.title(" Analysis Based on Overall Customer Segmentation Features")
            
        if selected_make != 'Overall' and selected_cluster == 'Overall' and selected_airbag == 'Overall' and selected_fuel == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_make)+ " Manufacturer ")
        
        if selected_make == 'Overall' and selected_cluster != 'Overall' and selected_airbag == 'Overall' and selected_fuel == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cluster)+ " Cluster ")
            
        if selected_make == 'Overall' and selected_cluster == 'Overall' and selected_airbag != 'Overall' and selected_fuel == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_airbag)+ " number of airbag ")

        if selected_make == 'Overall' and selected_cluster == 'Overall' and selected_airbag == 'Overall' and selected_fuel != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_fuel)+ " Fuel type ")

        if selected_make != 'Overall' and selected_cluster != 'Overall' and selected_airbag == 'Overall' and selected_fuel == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cluster)+ " Cluster and " + str(selected_make) + " Manufacturer" )

        if selected_make != 'Overall' and selected_cluster == 'Overall' and selected_airbag != 'Overall' and selected_fuel == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_make)+ " Manufacturer and " + str(selected_airbag) + "number of airbag")

        if selected_make != 'Overall' and selected_cluster == 'Overall' and selected_airbag == 'Overall' and selected_fuel != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_make)+ " Manufacturer and " + str(selected_fuel) + " Fuel type")
            
        if selected_make == 'Overall' and selected_cluster != 'Overall' and selected_airbag != 'Overall' and selected_fuel == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cluster)+ " Cluster and "+ str(selected_airbag) + " number of airbag")        
        
        if selected_make == 'Overall' and selected_cluster != 'Overall' and selected_airbag != 'Overall' and selected_fuel != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cluster)+ " Cluster and "+ str(selected_fuel) + " Fuel type and "+ str(selected_airbag) +"number of airbag.")
        
        if selected_make == 'Overall' and selected_cluster != 'Overall' and selected_airbag == 'Overall' and selected_fuel != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cluster)+ " Cluster and "+ str(selected_fuel) + " Fuel type") 

        if selected_make == 'Overall' and selected_cluster == 'Overall' and selected_airbag != 'Overall' and selected_fuel != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cluster)+ " Cluster and "+ str(selected_fuel) + " Fuel type ") 

        if selected_make != 'Overall' and selected_cluster != 'Overall' and selected_airbag != 'Overall' and selected_fuel != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_cluster)+ " Cluster and "+ str(selected_airbag) + " number of airbag and "+ str(selected_make) + " Manufacturer" + str(selected_fuel) + " Fuel type" )
            
        st.table(cusi)
        
        if selected_cluster == 'Overall':
            fig = px.scatter(df1, x='price', y="Power", color= 'cluster' , hover_data=['cluster'])
            st.header("Graph between price and Power with respect "+str(selected_cluster)+" cluster")
            st.plotly_chart(fig)
        else:
            df = df1[df1['cluster'] == selected_cluster]
            fig = px.scatter(df, x='price', y="Power", color= 'cluster' , hover_data=['cluster'])
            st.header("Graph between price and Power with respect "+str(selected_cluster)+" cluster")
            st.plotly_chart(fig)
            
        if selected_cluster == 'Overall':
            fig = px.scatter(df1, x='Power', y="ARAI_Certified_Mileage", color= 'cluster' , hover_data=['cluster'])
            st.header("Graph between Mileage and Power with respect "+str(selected_cluster)+" cluster")
            st.plotly_chart(fig)
        else:
            df = df1[df1['cluster'] == selected_cluster]
            fig = px.scatter(df, x='Power', y="ARAI_Certified_Mileage", color= 'cluster' , hover_data=['cluster'])
            st.header("Graph between Mileage and Power with respect "+str(selected_cluster)+" cluster")
            st.plotly_chart(fig)
            
        if selected_fuel == 'Overall':
            fig = px.scatter(df1, x='Fuel_Tank_Capacity', y="Displacement", color= 'cluster' , hover_data=['cluster'])
            st.header("Graph between Fuel_Tank_Capacity and Displacement with respect "+str(selected_cluster)+" cluster")
            st.plotly_chart(fig)
        else:
            df = df1[df1['Fuel_Tank_Capacity'] == selected_fuel]
            fig = px.scatter(df, x='Fuel_Tank_Capacity', y="Displacement", color= 'cluster' , hover_data=['cluster'])
            st.header("Graph between Fuel_Tank_Capacity and Displacement with respect "+str(selected_cluster)+" cluster")
            st.plotly_chart(fig)
            
        if selected_cluster == 'Overall':
            
            fig = px.scatter_3d(df1, x='price', y='Power', z='ARAI_Certified_Mileage', color='cluster',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Power Price and Mileage "+str(selected_cluster)+" clusters")
            st.plotly_chart(fig)
        else:
            df = df1[df1['cluster'] == selected_cluster]
            fig = px.scatter_3d(df, x='price', y='Power', z='ARAI_Certified_Mileage', color='cluster',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Power Price and Mileage "+str(selected_cluster)+" clusters")
            st.plotly_chart(fig)
            
        if selected_cluster == 'Overall' and selected_make == 'Overall':
            
            fig = px.scatter_3d(df1, x='price', y='Make', z='Power', color='cluster',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Makers Price and Power "+str(selected_cluster)+" clusters")
            st.plotly_chart(fig)
        if selected_cluster != 'Overall' and selected_make == 'Overall':
            df = df1[df1['cluster'] == selected_cluster]
            fig = px.scatter_3d(df, x='price', y='Make', z='Power', color='cluster',hover_data=['price'])
            fig.update_layout(scene_zaxis_type="log")
            st.header("Analysis between Makers Price and Power "+str(selected_cluster)+" clusters")
            st.plotly_chart(fig)
        if selected_cluster == 'Overall' and selected_make != 'Overall':
             df = df1[df1['Make'] == selected_make]
             fig = px.scatter_3d(df, x='price', y='Make', z='Power', color='cluster',hover_data=['price'])
             fig.update_layout(scene_zaxis_type="log")
             st.header("Analysis between Makers Price and Power "+str(selected_cluster)+" clusters")
             st.plotly_chart(fig)
             
        if selected_cluster != 'Overall' and selected_make != 'Overall':
             df = df1[df1['Make'] == selected_make]
             df = df1[df1['cluster'] == selected_cluster]
             fig = px.scatter_3d(df, x='price', y='Make', z='Power', color='cluster',hover_data=['price'])
             fig.update_layout(scene_zaxis_type="log")
             st.header("Analysis between Makers Price and Power "+str(selected_cluster)+" clusters")
             st.plotly_chart(fig)
             
        
        
        if selected_airbag == 'Overall':
            
            fig = px.bar(df1, x='cluster',y= 'Number_of_Airbags' , hover_data=['price'])
            st.header("Graph of cluster vs Number of airbags")
            st.plotly_chart(fig)
        else:
            df = df1[df1['Number_of_Airbags'] == selected_airbag]
            fig = px.bar(df, x='cluster',y= 'Number_of_Airbags' , hover_data=['price'])
            st.header("Graph of cluster vs Number of airbags")
            st.plotly_chart(fig)
            
        if selected_fuel == 'Overall':
            
            fig = px.bar(df1, x='cluster',y= 'Fuel_Type' , hover_data=['price'])
            st.header("Graph of cluster vs Type of Fuel")
            st.plotly_chart(fig)
        else:
            df = df1[df1['Fuel_Type'] == selected_fuel]
            fig = px.bar(df, x='cluster',y= 'Fuel_Type' , hover_data=['price'])
            st.header("Graph of cluster vs Type of Fuel")
            st.plotly_chart(fig)
            
        st.markdown("Based on the above analysis we can analyze the Indian market more efficiently and thoroughly. We can see that all the cars are now seperated with clusters some cars may have same cluster which will help us to make a strategy to counter the compititon as a company. Companies can use cluster analysis to generate good strategy to lead the market.As we took an example of Tata nexon a car model manufactured by Tata one of the leading automobile company. We looked into the cluster it belongs to and analyzed it we saw that most varients are of the car makers in those clusters are Maruti Suzuki , Hyndai, Mahindra. With clustring there are too many variable taken in considration which are hard to be traced by normal methods. The clusters generated by the KMeans model can be used to identify what is the strategic group that form a strong competition to the company products in the market it also show the close clusters to this group which also can be put in considration in some cases.Though as tempting as it's to use clustring to produce strategic groups it worth mentioning that the clustring process itself is a little bit ambigous and features contribution to the clustering process can't be easily explained so the overall interpretability of the model forms a challenge.Clustring may be not determinant but it can be used to augment the management decision by using it side by side with human intuition to come out with the right strategic group.")
        
        

    if user_menu == 'New Technology Wise Analysis':
        st.sidebar.header("Analysis Based On Technology Features (where 1 means the feature is present and 0 means the feature is not present)")
        make,esp,ps,ei = helper.tech(df)
        
        selected_make = st.sidebar.selectbox("Select the manufacturer ",make)
        selected_esp = st.sidebar.selectbox("Select the availability of Electronic Stability Program",esp)
        selected_ps = st.sidebar.selectbox("Select the availability of Paddle Shifter ", ps)
        selected_ei = st.sidebar.selectbox("Select the availability of Engine Immobilizer ",ei)
        
        techi = helper.fetch_tech_features(df, selected_make, selected_esp, selected_ps, selected_ei)
        
        if selected_make == 'Overall' and selected_esp == 'Overall' and selected_ps == 'Overall' and selected_ei == 'Overall':
            st.title(" Analysis Based on Overall Tech Features")
            
        if selected_make != 'Overall' and selected_esp == 'Overall' and selected_ps == 'Overall' and selected_ei == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_make)+ " Manufacturer ")
        
        if selected_make == 'Overall' and selected_esp != 'Overall' and selected_ps == 'Overall' and selected_ei == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_esp)+ " Electronic Stability Program ")
            
        if selected_make == 'Overall' and selected_esp == 'Overall' and selected_ps != 'Overall' and selected_ei == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_ps)+ " Paddle Shifter ")

        if selected_make == 'Overall' and selected_esp == 'Overall' and selected_ps == 'Overall' and selected_ei != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_ei)+ " Engine Immobilizer ")

        if selected_make != 'Overall' and selected_esp != 'Overall' and selected_ps == 'Overall' and selected_ei == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_esp)+ " Electronic Stability Program and " + str(selected_make) + " Manufacturer" )

        if selected_make != 'Overall' and selected_esp == 'Overall' and selected_ps != 'Overall' and selected_ei == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_make)+ " Manufacturer and " + str(selected_ps) + "Paddle Shifter")

        if selected_make != 'Overall' and selected_esp == 'Overall' and selected_ps == 'Overall' and selected_ei != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_make)+ " Manufacturer and " + str(selected_ei) + " Engine Immobilizer")
            
        if selected_make == 'Overall' and selected_esp != 'Overall' and selected_ps != 'Overall' and selected_ei == 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_esp)+ " Electronic Stability Program and "+ str(selected_ps) + " Paddle Shifter")        
        
        if selected_make == 'Overall' and selected_esp != 'Overall' and selected_ps != 'Overall' and selected_ei != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_esp)+ " Electronic Stability Program and "+ str(selected_ei) + " Engine Immobilizer and "+ str(selected_ps) +"Paddle Shifter.")
        
        if selected_make == 'Overall' and selected_esp != 'Overall' and selected_ps == 'Overall' and selected_ei != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_esp)+ " Electronic Stability Program and "+ str(selected_ei) + " Engine Immobilizer") 

        if selected_make == 'Overall' and selected_esp == 'Overall' and selected_ps != 'Overall' and selected_ei != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_esp)+ " Electronic Stability Program and "+ str(selected_ei) + " Engine Immobilizer ") 

        if selected_make != 'Overall' and selected_esp != 'Overall' and selected_ps != 'Overall' and selected_ei != 'Overall':
            st.title("Overall Analysis Based on "+ str(selected_esp)+ " Electronic Stability Program and "+ str(selected_ps) + " Paddle Shifter and "+ str(selected_make) + " Manufacturer" + str(selected_ei) + " Engine Immobilizer" )
        
          
        st.table(techi)
        
        
        
        
        if selected_make == 'Overall':
            fig = px.bar(df, x='ESP_(Electronic_Stability_Program)',y='price',color='Make')
            st.header("Analysis between price and Overall Electronic Stability Program with Overall Manufacturers")
            st.plotly_chart(fig)
            
            fig = px.bar(df, x='Paddle_Shifters',y='price',color='Make')
            st.header("Analysis between price and Overall Paddle Shifters with Overall Manufacturers")
            st.plotly_chart(fig)
            
            fig = px.bar(df, x='Engine_Immobilizer',y='price',color='Make')
            st.header("Analysis between price and Overall Engine Immobilizer with Overall Manufacturers")
            st.plotly_chart(fig)
            
            fig = px.bar(df, x='Multifunction_Display',y='price',color='Make')
            st.header("Analysis between price and Overall Multifunction Display with Overall Manufacturers")
            st.plotly_chart(fig)
            
        else:
            df = df[df['Make'] == selected_make]
            fig = px.bar(df, x='ESP_(Electronic_Stability_Program)',y='price',color='Make')
            st.header("Analysis between price and Overall Electronic Stability Program " +str(selected_make)+" Manufacturers")
            st.plotly_chart(fig)
            
            fig = px.bar(df, x='Paddle_Shifters',y='price',color='Make')
            st.header("Analysis between price and Overall Paddle Shifters " +str(selected_make)+" Manufacturers")
            st.plotly_chart(fig)
            
            fig = px.bar(df, x='Engine_Immobilizer',y='price',color='Make')
            st.header("Analysis between price and Overall Engine Immobilizer " +str(selected_make)+" Manufacturers")
            st.plotly_chart(fig)
            
            fig = px.bar(df, x='Multifunction_Display',y='price',color='Make')
            st.header("Analysis between price and Overall Multifunction Display " +str(selected_make)+" Manufacturers")
            st.plotly_chart(fig)
    
if selected == "Price Prediction":
    
    st.title("Price Prediction Using Random Forest Regressor")
    
    st.markdown('In this price prediction model the price of the car is predicted based on the inputs which will be provied by clint(in the real world scenario clint can be a maneger,stakeholder or the customer). The features which are included as an input feature are:-')
    '''
    * Mileage
    * Diplacement
    * Cylinders
    * Power
    * Fuel System
    * Fuel Tank Capacity
    * Doors
    * Seating Capacity
    * Airbags'''
    
    st.markdown('In this model the prediction is being made with the help of Random Forest Regression which is a machine learning algorithm.')
    st.header("why to use Random Forest Regression ? ")
    '''
    * Random forest algorithm can be used for both classifications and regression task.
    * It provides higher accuracy through cross validation.
    * Random forest classifier will handle the missing values and maintain the accuracy of a large proportion of data.
    * If there are more trees, it won’t allow over-fitting trees in the model.
    * It has the power to handle a large data set with higher dimensionality.
    '''
    
    
    model=pickle.load(open('model.pkl','rb'))
    
   
    
    html_temp = """
    <div style="background-color:#D8AF2E ;padding:10px">
    <h2 style="color:white;text-align:center;">Car Price Prediction </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    ARAI_Certified_Mileage = st.text_input("Mileage [for eg:- 23 ,21, 25, 15]","0")
    Displacement = st.text_input("Displacement of engine in cc [for eg:- 624, 799, 999, 1196]","0")
    Cylinders = st.text_input("Number of Cylinders [for eg:- 2, 3, 4, 5]","0")
    Power = st.text_input("Power [for eg:- 37, 53, 67, 72]","0")
    Torque = st.text_input("Torque [for eg:- 51,72,91,101,85]","0")
    PGM_Fi = st.text_input("Fuel System []for eg: 0 for injection type fuel system and 1 for PGM-Fi fuel system","0")
    Fuel_Tank_Capacity = st.text_input("Fuel_Tank_Capacity [for eg:- 24,15,28,40]","0")
    Doors = st.text_input("Number of Doors [for eg:- 2,4,5]","0")
    Seating_Capacity = st.text_input("Number of seats [for eg:- 2,7,5]","0")
    Number_of_Airbags = st.text_input("Number_of_Airbags [for eg:- 1,2,3,4,5]","0")
    

    if st.button("Predict Price"):
        if ARAI_Certified_Mileage == '0' and Displacement == '0' and Cylinders == '0' and Power == '0' and Torque == '0' and PGM_Fi == '0' and Fuel_Tank_Capacity == '0' and Doors == '0' and Seating_Capacity == '0' and Number_of_Airbags == '0':
            output = 0
            st.success('According to the given input which is provided by you the Price of the car is Rs {} and $0 .Since you did not gave any input. Please try using the model again with some inputs. '.format(output))
            
        else :
            output=helper.predict_forest(model, ARAI_Certified_Mileage,Displacement, Cylinders,Power,Torque,PGM_Fi,Fuel_Tank_Capacity,Doors,Seating_Capacity,Number_of_Airbags)
            output1 = int(output/78)
            st.success('According to the given input which is provided by you the Price of the car is Rs {} and $'.format(output)+ str(output1)+'.Thanks for Using this prediction model.')
    
   
    
    
if selected == "Links":
    
    st.title('Important Links related to this Indian Automotive Industry Analysis:-')
    '''
    * Tableau Dashbords:
        * [Engine Performance](https://public.tableau.com/app/profile/shankhadeep.sarkar7325/viz/CarEnginePerformance/Engineperformence)
        * [Body Type](https://public.tableau.com/app/profile/shankhadeep.sarkar7325/viz/Caranalysisbasedonbodytype/BasedonbodyType)
        * [Safety](https://public.tableau.com/app/profile/shankhadeep.sarkar7325/viz/Caranalysisbasedonsafety/basedonSafety)
        * [Fuel](https://public.tableau.com/app/profile/shankhadeep.sarkar7325/viz/CaranalysisbasedonFuel/basedonFuel)
        * [New Technology](https://public.tableau.com/app/profile/shankhadeep.sarkar7325/viz/CaranalysisbasedonnewTechnology/NewTechnology)
        * [Family Car](https://public.tableau.com/app/profile/shankhadeep.sarkar7325/viz/Caranalysisbasedonfamilycaranalysis/basedonfamilycaranalysis)
        **Please Visualize It in "Full Screen"**
        
    * [Github Repository](https://github.com/Shankhadeep2000/Indian_Automotive_Industry_Analysis)
    
    * [Dataset](https://acehacker.com/microsoft/engage2022/cars_engage_2022.csv)
    
    '''
            

            
   

    

    

    
    
    
    
    
    
    
        
    
    
