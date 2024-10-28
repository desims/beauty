import streamlit as st
import pandas as pd

st.title('🎈 Dashboard Beauty Product')

st.write('This is interative dashboard beauty product')
df = pd.read_csv('https://raw.githubusercontent.com/desims/Chat-AI/refs/heads/main/data/data2.csv', delimiter=';')
df

