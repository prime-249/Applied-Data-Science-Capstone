# Applied-Data-Science-Capstone
Capstone project for IBM course "Applied Data Science Specialization with Python"

GOAL:
This project aims to predict if the Falcon 9 first stage will land successfully.
SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage; therefore, if we can determine if the first stage will land, we can determine the cost of a launch. 

STEPS:
  DATA COLLECTION
    Data has been collected via API - from SpaceX official API api.spacexdata.com - and Webscraping - from Wikipedia page 'List of Falcon 9       and Falcon Heavy launches'. (Documents 1 and 2)
  DATA WRANGLING AND EDA
    Data has been cleansed, the 'Class' column to identify the landing outcome easily during later analysis, and some EDA has been performed      using Pandas and SQL. (Documents 3, 4, and 4.2)
  VISUALIZATION
    The analysis has been visualized using Charts - using Seaborn - and Interactive Maps - using Folium. (Documents 5 and 6)
  DASHBOARD
    Generated an Interactive Dashboard using Plotly and Dash
  PREDICTIVE ANALYSIS
    Generated a Pipeline to fit models based on training and test data to understand whether the first stage of any launch will land             successfully or not.
    The models have been evaluated using Grid Search in Cross-Validation - using GridSearchCV from Scikit - and calculating the Coefficient       of Determination (R^2)
