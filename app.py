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

# Mostramos toda la tabla de datos
st.header('Animal Crossing Villagers')
st.write(data)

# Mostramos los aldeanos agrupados por especie
df = data[["Species", "Name"]]
chart_df = df.groupby(["Species"]).count()
chart_df["Species"] = chart_df.index

st.subheader('Villagers by Species')
st.bar_chart(chart_df, x="Species", y=["Name"])

# Mostramos los aldeanos agrupados por personalidad
st.subheader('Villagers by Personality')
personality = data.groupby('Personality').size()
fig, ax = plt.subplots()
ax.pie(personality, labels=personality.index, autopct='%1.1f%%')
st.pyplot(fig)

# Mostramos un gráfico de barras con los meses con más cumpleaños

# Creamos un diccionario con los meses
months = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

# Creamos una nueva columna con el nombre del mes (formato 00-Jan)
data["Birthday Month"] = data["Birthday"].str.split("-").str[1]

# Agrupamos los datos por mes y contamos el número de cumpleaños

df = data[["Birthday Month", "Name"]]
chart_df = df.groupby(["Birthday Month"]).count()
chart_df["Birthday Month"] = chart_df.index

# Cambiamos el nombre de las columnas
chart_df = chart_df.rename(columns={"Name": "Number of Birthdays"})
chart_df = chart_df.rename(columns={"Birthday Month": "Month"})
chart_df = chart_df.sort_values(by=['Month'])

st.subheader('Birthdays by Month')
st.bar_chart(chart_df, x="Month", y=["Number of Birthdays"])

# Mostramos las canciones más populares	
df = data[["Favorite Song", "Name"]]
chart_df = df.groupby(["Favorite Song"]).count()
chart_df["Favorite Song"] = chart_df.index

# Cambiamos el nombre de las columnas
chart_df = chart_df.rename(columns={"Name": "Popularity"})
chart_df = chart_df.rename(columns={"Favorite Song": "Song"})

st.subheader('Most Popular KK Songs')
st.bar_chart(chart_df, x="Song", y=["Popularity"])
