# Stremlit demo webapp
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({"Data":np.array(np.logspace(0,2,20))})
st.line_chart(df)
