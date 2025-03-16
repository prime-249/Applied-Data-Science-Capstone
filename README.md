# Applied-Data-Science-Capstone
Capstone project for IBM course "Applied Data Science Specialization with Python"

## GOAL:
This project aims to predict if the Falcon 9 first stage will land successfully.
SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage; therefore, if we can determine if the first stage will land, we can determine the cost of a launch. 


## STEPS:

  DATA COLLECTION
    Data has been collected via API - from SpaceX official API api.spacexdata.com - and Webscraping - from Wikipedia page 'List of Falcon 9       and Falcon Heavy launches'. (Documents 1 and 2)
  
  DATA WRANGLING AND EDA
    Data has been cleansed, the 'Class' column to identify the landing outcome easily during later analysis, and some EDA has been performed      using Pandas and SQL. (Documents 3, 4, and 4.2)
    
  VISUALIZATION
    The analysis has been visualized using Charts - using Seaborn - and Interactive Maps - using Folium. (Documents 5 and 6)
    
  DASHBOARD
    Generated an Interactive Dashboard using Plotly and Dash (Document 7)
 
  PREDICTIVE ANALYSIS
    Generated a Pipeline to fit models based on training and test data to understand whether the first stage of any launch will land             successfully or not.
    The models have been evaluated using Grid Search in Cross-Validation - using GridSearchCV from Scikit - and calculating the Coefficient       of Determination (R^2) (Document 8)


CONCLUSION:
The project has been presented in a PowerPoint presentation (Document 9)


## TABLE OF CONTENTS
1. Data Collection via API [https://github.com/prime-249/Applied-Data-Science-Capstone/blob/main/1.%20Data%20Collection%20via%20API.ipynb]
2. Data Collection via WebScraping [https://github.com/prime-249/Applied-Data-Science-Capstone/blob/main/2.%20Data%20Collection%20via%20WebScraping.ipynb]
3. Data Wrangling [https://github.com/prime-249/Applied-Data-Science-Capstone/blob/main/3.%20Data%20Wrangling.ipynb]
4. EDA with SQL and PANDAS [https://github.com/prime-249/Applied-Data-Science-Capstone/blob/main/4.%20EDA%20with%20SQL.ipynb] [https://github.com/prime-249/Applied-Data-Science-Capstone/blob/main/4.2%20EDA%20with%20SQL%20(but%20using%20Pandas).ipynb]
5. EDA with Visualization [https://github.com/prime-249/Applied-Data-Science-Capstone/blob/main/5.%20EDA%20with%20Visualization.ipynb]
6. Folium [https://github.com/prime-249/Applied-Data-Science-Capstone/blob/main/6%20Folium.ipynb]
7. spacex_dash_app [https://github.com/prime-249/Applied-Data-Science-Capstone/blob/main/7.%20spacex_dash_app.py]
8. Predictive Analysis [https://github.com/prime-249/Applied-Data-Science-Capstone/blob/main/8%20Predictive%20Analysis.ipynb]
