## End-to-End Machine Learning Project- Telecom Customer Churn Prediction using Machine Learning

<img target="_blank" src="https://github.com/dipakml/Telecom-Customer-Churn-Prediction/blob/master/images/Telecom-Company-Customer-Churn-Prediction.jpg" width=1000>

### Table of Content
  * [Overview](#overview)
  * [Dataset Information](#dataset)
  * [Motivation](#motivation)
  * [Demo](#demo)
  * [Steps in the project execution](#Learning-Objective)
  * [Technical Aspect](#technical-aspect)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Note](#note)



### Overview 

Customer churn is defined as when customers or subscribers discontinue doing business with a firm or service.

Customers in the telecom industry can choose from a variety of service providers and actively switch from one to the next. The telecommunications business has an annual churn rate of 15-25 percent in this highly competitive market.

Individualized customer retention is tough because most firms have a large number of customers and can't afford to devote much time to each of them. The costs would be too great, outweighing the additional revenue. However, if a corporation could forecast which customers are likely to leave ahead of time, it could focus customer retention efforts only on these "high risk" clients. The ultimate goal is to expand its coverage area and retrieve more customers loyalty. The core to succeed in this market lies in the customer itself.

Customer churn is a critical metric because it is much less expensive to retain existing customers than it is to acquire new customers.

In this project, let's apply machine learning techniques and develop a web based application to predict whether the existing customer will leave or stay with the current telecom company.


### Dataset Information

Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

The data set includes information about:

Customers who left within the last month – the column is called Churn.

Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies.

Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges.

Demographic info about customers – gender, age range, and if they have partners and dependents.

Dataset used in this project can be found here : [Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn?datasetId=13996&sortBy=voteCount/)


### Motivation

Any oraganization's key focus for success is reducing client attrition and implementing effective retention strategy.
The motivation for working on this project was to use machine learning experiments to try help the organization to identify potential customers who are likely to discontinue their services. Company then can focus on these customers & offer them some promotional offers & try to retain them. 

Idea is to implement the end to end machine learning project while using free deployment platform like Heroku.



### Demo
[Visit this link for live demo](https://telecomchurn7.herokuapp.com/)

Web application Snapshot:

<img target="_blank" src="https://github.com/dipakml/Telecom-Customer-Churn-Prediction/blob/master/images/webapp_snapshot2.png" width=800>


### Steps in the project execution

<img target="_blank" src="https://github.com/dipakml/Telecom-Customer-Churn-Prediction/blob/master/images/0_V0GyOt3LoDVfY7y5.png" width=800>

### Technical Aspect 

- Training a machine learning model using scikit-learn. 
- Building and hosting a streamlit web app on Heroku. 
- A user has to input customer's key features.
- Once it gets all the fields information , the prediction is displayed. 


### Technologies Used  
![](https://forthebadge.com/images/badges/made-with-python.svg) 

<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/streamlit.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/heroku.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/numpy.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/pandas.jpeg" width=160>


### Installation 
- Clone this repository and unzip it.
- After downloading, cd into the working directory.
- Begin a new virtual environment with Python 3 and activate it.
- Install the required packages using pip install -r requirements.txt
- Execute the command: streamlit run app.py


### Note:
- Webapp can handle concurrency upto some extent but can be scaled.

