# ESTE SCRIPT NO ES PARTE DE LA APLICACIÓN, SÓLO SE EJECUTA UNA VEZ PARA EXTRAER LAS IMÁGENES DE LOS VILLAGERS Y GUARDARLAS EN EL CSV

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Cargamos los datos y los almacenamos en caché
@st.cache_data
def load_data():
    # Datos extraídos de https://www.kaggle.com/datasets/jessicali9530/animal-crossing-new-horizons-nookplaza-dataset?select=villagers.csv
    data = pd.read_csv('villagers.csv')
    return data

data = load_data()

# import beautifulsoup
from bs4 import BeautifulSoup

with open("Villagers.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    rows = soup.find_all('tr')
    for row in rows:
        name_td = row.find('td', class_='s7')
        if name_td:
            name = name_td.text.strip()
            img = row.find('img')
            if img:
                img_url = img['src']
                data.loc[data['Name'] == name, 'image'] = img_url
# overwrite the csv file
data.to_csv('villagers.csv', index=False)