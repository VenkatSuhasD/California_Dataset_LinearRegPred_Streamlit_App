import numpy as np 
import joblib
import streamlit as st

#-- Load the trained model
model1 = joblib.load('california.joblib')
model=model1['model']
cols=model1['columns']

#-- Define the Streamlit app
st.title("California Housing Price Prediction")
list=[]
for i in cols:
    v=st.number_input(f'enter the value of {i}:')
    list.append(v)

if st.button('Predict'):
    output=model.predict([list])
    st.success(output)