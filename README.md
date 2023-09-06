# 📈 Cuadro de mandos utilizando la tecnología streamlit 📊

## Objetivo
He escogido hacer un test con los datos del videojuego Animal Crossing: New Horizons. En concreto, he escogido los datos de los vecinos que puedes tener, sus gustos, mes de nacimiento y sus personalidades.

## Búsqueda de los datos
Los datos han sido extraídos de [esta página](https://www.kaggle.com/datasets/jessicali9530/animal-crossing-new-horizons-nookplaza-dataset?select=villagers.csv), y he hecho un scrapping de [este datasheet](https://nookipedia.com/wiki/Community:ACNH_Spreadsheet) para añadir los links de las imágenes de cada vecino (el script puede verse en [scrapping.py](./scrapping.py)).

## Documentación de los datos
Los datos están en formato csv, y he hecho uso de las siguientes columnas: 
 - `name`: nombre del vecino
 - `personality`: personalidad del vecino
 - `birthday`: fecha de nacimiento del vecino
 - `hobby`: hobbies del vecino
 - `image`: link de la imagen del vecino que he extraído del scrapping

## Aplicación y dependencias.
La aplicación se llama `app.py`. Y las dependencias están registradas en el fichero `requirements.txt`.
