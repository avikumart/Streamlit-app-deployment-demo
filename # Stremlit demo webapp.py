# Stremlit demo webapp
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("country.csv")

st.line_chart(df['Corruption_Index'])