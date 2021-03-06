# Stremlit demo webapp
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({"Corruption_INdex":[77, 53, 40, 47, 38, 75, 85, 81, 82, 81, 88, 90, 69, 74, 29, 62, 48,
       36, 44, 35]})

st.title("Corruption index WebApp")
st.write("This is the dataframe representing the below chart: ", pd.DataFrame({
     'country_name': ['Hong Kong', 'South Korea', 'China', 'Italy', 'Mongolia',
       'Austria', 'Norway', 'UK', 'Canada', 'Germany', 'Sweden',
       'Denmark', 'France', 'United States', 'Russia ', 'Portugal',
       'Romania', 'Argentina', 'Greece', 'Thailand '],
     'corruption index': [77, 53, 40, 47, 38, 75, 85, 81, 82, 81, 88, 90, 69, 74, 29, 62, 48,
       36, 44, 35],
 }))

#plot a line chart
st.title("Corruption Index by countries")
st.bar_chart(df)


       


