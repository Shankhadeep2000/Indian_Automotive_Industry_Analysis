# Indian_Automotive_Industry_Analysis
## Objective
The **Automotive Industry** continues to face a dynamic set of challenges. For those with right ambition it represents an exiting time with opportunities to differentiate and stand out from the crowd. One area that has the opportunity to deliver significant competitive advantage is analytics. 

The main objective of this report is to analyze the data of **Automotive Industry** and gather all the insights from it to understand the Indian market of cars from the given set of features. The topics of the analysis i.e. questions to answer from the analysis will be:-
- Customer Segmentation: It is one of the motive of this analysis. It is important for car makers to analyze the market and counter the opponent car makers. It has several steps:-
        1. Exploretory Data Analysis
        2. Clustering Analysis
- Engine Performance:How much power or performance is favourable for Indian market.
- Body Type: Which Body Type(s) is most favourable in Indian market. 
- Safety: Do Indian market look into safety field while buying a car. 
- Fuel: Which type of fuel is used in most of the cars in India with that we can even analyze co2 emmision.
- New Technology: Do Indian market moving towards automation and new technologies which are present in cars along with the world.
- Family Car: What type of cars prefered by Indian market i.e. now-a-days people attach child seats in cars for their children which tells us that the buyer has a family and children. 

**This type of insights will effect the market and the car makers will able to understand it to gain their profits and also help us to improve the features that new world requierd**

## Approach

This report will follow a mathematical approach using the concept of exploratory data analysis and using the concept of clustering analysis using machine learning algorithm. It also uses the machine learning algorithm for predictive analysis of the feature caleed "price".

## Challenge

The automotive industry is one of the largest industries out there it's a 2.6 trillion dollar industry!

But inside the industry there are too many categories and subcategories constructed by too many variables that it almost safe to say that every category is an industry of itself. for instance the car body variable is a vital one, as diffrernt body types are being used for very different reason here is a list of some car body type:
- SEDAN
- COUPE
- STATION WAGON
- HATCHBACK
- CONVERTIBLE
- SPORT-UTILITY VEHICLE (SUV)
- MINIVAN

And this just to name a few!, here is a **[Photo](http://carsonelove.com/car-body-types#prettyPhoto)** show some of car types in more details.

And all of the variety above is only regarding the car body type which is only one variable!, not to mention that there are grey areas where some car body types can be irrelevant to customer decision.

So for a car company it's really a challenge to identify its strategic group as it really takes a lot of effort to put all variable in consideration.

## Data
  The **[Dataset](https://acehacker.com/microsoft/engage2022/cars_engage_2022.csv)** used in this project is provided by Microsoft Engage Program.The dataset used in this report is having the latest information about cars in the Indian market. The dataset contains cars with their variants, In dataset there are 1200+ model/variants to study. There is a variety of Makes/Models which can be studied, All prices has been converted from indian rupee to USD.

## Web-app

### Libraries used in web-app
  ```
- matplotlib==3.5.2
- numpy==1.22.3
- pandas==1.4.2
- Pillow==9.1.1
- plotly==5.8.0
- seaborn==0.11.2
- streamlit==1.9.0
- streamlit_option_menu==0.3.2
- pickle-mixin==1.0.2
- sklearn<0.24.2
```
### About web app
  The web app is built with the help of **Streamlit library** is  a Python Library and use to create data web apps.It is deployed in **HEROKU** with the domain name of [Indian automotive analysis](https://indianautomotiveanalysis.herokuapp.com/). It can also run on the local server just by folowing stepes below:
- Open Command prompt in windows
- To create a virtual environment install virtualenv with pip ```pip install virtualenv```
- Create a folder Desktop and copy its path and go to the folder directory from command prompt by using ```cd <directory address>```
- Create a virtual environment with``` virtualenv <virtual environment name>```
- Now the virtual environment is created and to activate it run the folowing command in command prompt```<virtuel environment name>\Scripts\activate```
- Install all packages mentioned in requirment.txt with the help of ```pip install <package name>```
- download the zip file from github and paste the app.py , helper.py , preproceser.py , model.pkl , and all the images in the folder which you created earliear for creating the virtual environment.
- now open your command prompt where you have activated the virtual environment and run ```streamlit run app.py```
- It will create a local server and it will display the web application.

## Features
- It provides a dashboard based on engine performance, safety performance, and latest features of variants of various models of Automobile Manufacturers are provided. Along with this visualization, plots have been shown for __ understanding the market trends.
- It shows the analysis based on fuel hence a person can get insights on **co2 emission**.
- It provides dynamic features selections based on vehicle make and other preferences to analyze the market trend on folowing feature analysis.
- It also has the feature of price prediction with manual input system with R-squared value of 94% Random Forest model.


## Demo
Microsoft Engage Demo Yotube Video:- https://youtu.be/rMW3nKqQjEg

## ScreenShots

<img width="958" alt="me1" src="https://user-images.githubusercontent.com/75299574/171378022-d97fd768-7001-407e-9b5f-bb4418ade254.png">

<img width="959" alt="me2" src="https://user-images.githubusercontent.com/75299574/171378062-cb6481bc-5956-4f37-b8a3-2571520090d2.png">

<img width="959" alt="me3" src="https://user-images.githubusercontent.com/75299574/171378081-1053031e-4f15-48ab-b8bc-cb0f3ff2f102.png">


<img width="957" alt="me4" src="https://user-images.githubusercontent.com/75299574/171378221-6f3ef2c0-ae90-4b63-92bf-7563fb39a5c2.png">

<img width="958" alt="me5" src="https://user-images.githubusercontent.com/75299574/171378248-0f4798a1-2f77-427b-8e2b-7753a59ede0b.png">


<img width="955" alt="me6" src="https://user-images.githubusercontent.com/75299574/171378297-b8e4e47f-abe0-4e1c-8d3b-8602b91b3894.png">


## Future Scope

- Using Deep Neural Networks to make the price prediction to be more precise.
- Adding A feature of drag and drop other csv and get the analysis report with different graphs.
- Adding a feature of good Strategic Group feature which will help to create a good strategy absed on cluster analysis.

