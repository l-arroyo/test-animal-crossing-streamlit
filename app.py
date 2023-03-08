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
st.header('¿Qué vecino de Animal Crossing eres?')
st.write('¡Descubrelo con este sencillo test!')
# Creamos un diccionario con los meses
months = {
    "Enero" : "Jan",
    "Febrero" : "Feb",
    "Marzo" : "Mar",
    "Abril" : "Apr",
    "Mayo" : "May",
    "Junio" : "Jun",
    "Julio" : "Jul",
    "Agosto" : "Aug",
    "Septiembre" : "Sep",
    "Octubre" : "Oct",
    "Noviembre" : "Nov",
    "Diciembre" : "Dec"
}

# Creamos un diccionario con las personalidades
personalities = {
    "Soy una persona perezosa": "Lazy",
    "Soy un Gymbro / Gymrat": "Jock",
    "Soy bastante gruñón / gruñona": "Cranky",
    "Soy una persona refinada": "Smug",
    "Mis amigos dicen que soy una persona muy intensa": "Peppy",
    "Me defino como una persona madura": "Snooty",
    "Soy como un hermano mayor / hermana mayor para mi grupo de amigos": "Big Sister",
    "Ninguna de las anteriores": "Normal",
}

# Creamos un diccionario con los hobbies
hobbies = {
    "Aprender cosas nuevas": "Education",
    "Hacer deporte": "Fitness",
    "Estar en contacto con la naturaleza": "Nature",
    "Jugar": "Play",
    "La música": "Music",
    "Estar a la última moda": "Fashion",
}

st.subheader('¿Cuál es tu mes de nacimiento?')
# Mostramos un selectbox con los meses (el texto que se muestra es el valor del texto de antes de los dos puntos)
month = st.selectbox('Selecciona un mes', list(months.keys()))
month = months[month]

# Filtramos los datos por el mes seleccionado
filtered_data = data[data["Birthday"].str.contains(month)]

# filtrar los hobbies
st.subheader('¿Cuál es tu hobby favorito?')
hobby = st.selectbox('Selecciona un hobby', list(hobbies.keys()))
hobby = hobbies[hobby]

# añadir el filtro a filtered_data
filtered_data = filtered_data[filtered_data["Hobby"].str.contains(hobby)]

# filtrar las personalidades
st.subheader('¿Cuál de estas frases te representa mejor?')
personality = st.selectbox('Selecciona una frase', list(personalities.keys()))
personality = personalities[personality]

# añadir el filtro a filtered_data
filtered_data = filtered_data[filtered_data["Personality"].str.contains(personality)]

# botón para mostrar los resultados	
if st.button('Mostrar resultados'):
    # si no hay resultados, mostrar un mensaje de error
    if len(filtered_data) == 0:
        st.error('Ups... Parece que no hay ningún vecino que coincida con tus preferencias. ¡Prueba a cambiar algún campo!')
    else:
        st.subheader('¡Estos son tus vecinos de Animal Crossing!')

        # Mostramos las imágenes de los vecinos con su nombre
        for index, row in filtered_data.iterrows():
            st.image(row['image'])
            st.write(row['Name'])
