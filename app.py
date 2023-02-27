import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    data = pd.read_csv('mascotas.json')
    return data

data = load_data()
st.write(data)