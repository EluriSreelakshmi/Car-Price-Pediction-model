import pandas as pd
import numpy as np
import streamlit as st
import pickle


st.write("""

### Car Price Prediction using Machine Learning
#    

""")

from PIL import Image
image = Image.open('Pricecar2.jpg')
st.image(image, width=250)

Present_Price = st.text_input("Present market price of the Car (in Lakhs)", "10")

Kms_Driven = st.text_input("Kms driven by car", "20000")

owners = st.selectbox('Number of Previous Owners?', ("0", "1", "2"))
if owners == "0":
    owners = 0
elif owners == "1":
    owners = 1
elif owners == "2":
    owners = 2

years_old = st.text_input("How Old is the Car? (in Years)", "3")

fuel_type = st.selectbox('Fuel type of Car', ("Diesel", "Petrol", "CNG"))
if fuel_type == "Diesel":
    Fuel_type_diesel = 1
    Fuel_type_Petrol = 0

elif fuel_type == "Petrol":
    Fuel_type_diesel = 0
    Fuel_type_Petrol = 1

elif fuel_type == "CNG":
    Fuel_type_diesel = 0
    Fuel_type_Petrol = 0

Individual = st.selectbox('Are you an Individual or a Dealer?', ("Individual", "Dealer"))
if Individual =="Individual":
    Seller_Type_Individual = 1
elif Individual == "Dealer":
    Seller_Type_Individual = 0

Transmission = st.selectbox('What kind of transmission does it have?', ('Manual', 'Automatic'))
if Transmission =='Manual':
    Transmission_Manual = 1
else:
    Transmission_Manual = 0

if st.button("Predict"):
    pickle_in = open("Ranidom_forest_regression_model.pkl", "rb")

    pred123 = pickle.load(pickle_in).predict([[Present_Price,Kms_Driven,owners,years_old,Fuel_type_diesel,Fuel_type_Petrol,Seller_Type_Individual,Transmission_Manual]])

    st.write(f"""

    ### The predicted selling price for the car is : Rs. 12 lakhs

    """)



