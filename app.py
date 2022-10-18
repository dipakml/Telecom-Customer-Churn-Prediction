# -*- coding: utf-8 -*-
"""
Created on #### ##:##:## 2022

@author: DA
"""

# -*- coding: utf-8 -*-
"""

@Created by: DA
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2022/03/16/06/26/background-7071683__480.jpg");

         }}
         
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


pickle_in = open("xgb.pkl","rb")
xgb=pickle.load(pickle_in)  

pickle_sc = open("sc.pkl","rb")
sc=pickle.load(pickle_sc)  


def main():
    html_temp = """
    <div style="background-color:orange;padding:20px">
    <h2 style="color:blue;text-align:center;">Telecom Customer Churn Prediction </h2>
    </div>
    """
        
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.markdown('**This is a web application built using Machine Learning for prediction of customer churn for telecom industry. Enter the customer details, this web application will predict if the customer will leave or stay.**')

    gender = st.selectbox("Gender",("Male","Female"))
    if gender == 'Male':
        gender = 1
    else:
        gender = 0

    SeniorCitizen = st.selectbox("Senior Citizen",("Yes","No"))
    if SeniorCitizen == 'Yes':
        SeniorCitizen = 1
    else:
        SeniorCitizen = 0       

    #SeniorCitizen = st.number_input("Enter 1 if customer is Senior Citizen, else enter 0")

    tenure = st.number_input("Enter the tenure(Between 0 to 72)")

    Partner = st.selectbox("Partner",("Yes","No"))
    if Partner == 'Yes':
        Partner = 1
    else:
        Partner = 0
   
    Dependents = st.selectbox("Dependents",("Yes","No"))
    if Dependents == 'Yes':
        Dependents = 1
    else:
        Dependents = 0
  
    PhoneService = st.selectbox("Phone Service",("Yes","No"))
    if PhoneService == 'Yes':
        PhoneService = 1
    else:
        PhoneService = 0

    MultipleLines = st.sidebar.selectbox("Multiple Lines",("Yes","No"))
    if MultipleLines == 'Yes':
        MultipleLines = 1
    else:
        MultipleLines = 0

    OnlineSecurity = st.sidebar.selectbox("Online Security",("Yes","No"))
    if OnlineSecurity == 'Yes':
        OnlineSecurity = 1
    else:
        OnlineSecurity = 0

    OnlineBackup = st.sidebar.selectbox("Online Backup",("Yes","No"))
    if OnlineBackup == 'Yes':
        OnlineBackup = 1
    else:
        OnlineBackup = 0

    DeviceProtection = st.sidebar.selectbox("Device Protection",("Yes","No"))
    if DeviceProtection == 'Yes':
        DeviceProtection = 1
    else:
        DeviceProtection = 0


    TechSupport = st.sidebar.selectbox("Tech Support",("Yes","No"))
    if TechSupport == 'Yes':
        TechSupport = 1
    else:
        TechSupport = 0

    StreamingTV = st.sidebar.selectbox("Streaming TV",("Yes","No"))
    if StreamingTV == 'Yes':
        StreamingTV = 1
    else:
        StreamingTV = 0

    StreamingMovies = st.sidebar.selectbox("Streaming Movies",("Yes","No"))
    if StreamingMovies == 'Yes':
        StreamingMovies = 1
    else:
        StreamingMovies = 0

    Contract = st.sidebar.selectbox("Contract",("Month-to-month","One year","Two year"))
    if Contract == 'Month-to-month':
        Contract = 0
    elif Contract == 'One year':
        Contract = 1
    else:
        Contract = 2


    PaperlessBilling = st.sidebar.selectbox("Paperless Billing",("Yes","No"))
    if PaperlessBilling == 'Yes':
        PaperlessBilling = 1
    else:
        PaperlessBilling = 0


    InternetService = st.sidebar.selectbox("Internet Service",("DSL","Fiber Optic","No"))
    if InternetService == 'Fiber Optic':
        InternetService_Fiber_optic = 1
        InternetService_No = 0
    elif  InternetService == 'No':   
        InternetService_Fiber_optic = 0
        InternetService_No = 1
    else:
        InternetService_Fiber_optic = 0
        InternetService_No = 0

    PaymentMethod = st.sidebar.selectbox("Payment Method",('Electronic check', 'Mailed check', 'Bank transfer','Credit card automatic'))
    if PaymentMethod == 'Electronic check':
        PaymentMethod_Credit_card_automatic = 0
        PaymentMethod_Electronic_check = 1
        PaymentMethod_Mailed_check = 0
    elif  PaymentMethod == 'Credit card automatic':  
        PaymentMethod_Credit_card_automatic = 1
        PaymentMethod_Electronic_check = 0
        PaymentMethod_Mailed_check = 0
    elif  PaymentMethod == 'Mailed check':  
        PaymentMethod_Credit_card_automatic = 0
        PaymentMethod_Electronic_check = 0
        PaymentMethod_Mailed_check = 1      
    else:
        PaymentMethod_Credit_card_automatic = 0
        PaymentMethod_Electronic_check = 0
        PaymentMethod_Mailed_check = 0

    MonthlyCharges = st.number_input("Enter the monthly charges(Between 20 to 120)")

    TotalCharges = st.number_input("Enter the total charges(Between 20 to 9000)")

    result=""

    if st.button('Predict'):

        result=xgb.predict(sc.transform([[gender, SeniorCitizen, Partner, Dependents, tenure,
                                                PhoneService, MultipleLines, OnlineSecurity,OnlineBackup,
                                                 DeviceProtection, TechSupport, StreamingTV, StreamingMovies,
                                                Contract, PaperlessBilling, MonthlyCharges, TotalCharges,
                                                InternetService_Fiber_optic, InternetService_No,
                                                PaymentMethod_Credit_card_automatic, PaymentMethod_Electronic_check,
                                                PaymentMethod_Mailed_check]]))
        
        if result ==1:
            return st.header('Customer is going to leave')
        else:
            return st.header('Customer is going to stay')

        


  
if __name__=='__main__':
    main()
    
    
    
