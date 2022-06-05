# Stremlit demo webapp
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({"Corruption_INdex":[77, 53, 40, 47, 38, 75, 85, 81, 82, 81, 88, 90, 69, 74, 29, 62, 48,
       36, 44, 35]})
#st.dataframe(df)

#plot a line chart
st.line_chart(df)
st.title("Corruption Index by countries")

