#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st
import pandas as pd


# In[11]:


df = pd.read_csv('car_data.csv')

car_name = st.sidebar.text_input('Car_Name')
transmission_type = st.sidebar.multiselect('Transmission', ['Manual', 'Automatic'], default=['Manual', 'Automatic'])
selling_price_range = st.sidebar.slider('Selling_Price', 0, 20, (0, 20))
year_range = st.sidebar.slider('Year', 2000, 2024, (2000, 2024))
submit = st.sidebar.button('Submit')

if submit:
    if car_name:
        df = df[df['Car_Name'].str.contains(car_name, case=False)]
    if transmission_type:
        df = df[df['Transmission'].isin(transmission_type)]
    df = df[df['Selling_Price'].between(*selling_price_range)]
    df = df[df['Year'].between(*year_range)]

st.write(df)


# In[ ]:




