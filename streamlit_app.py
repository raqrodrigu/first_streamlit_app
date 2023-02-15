import streamlit

streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#importamos pandas para leer nuestro CSV de s3 
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#añadimos el indice con el nombre de la fruta
my_fruit_list= my_fruit_list.set_index('Fruit')

#Agregaremos un widget interactivo para el usuario llamado Selección múltiple que permitirá a los usuarios 
#elegir las frutas que desean en sus batidos.
#hasta este paso el selector se ponía en forma de números (pero al añadir la fila 19 se soluciona)
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#dejamos un ejemplo por defecto para el cliente
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#pedimos que nos muestre los datos en la pagina
#streamlit.dataframe(my_fruit_list)
 
#añadimos la mejora de que cuando has seleccionado un/as frutas solo aparezca esa seleccion en la tabla
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#mostramos la tabla en la pagina
streamlit.dataframe(fruits_to_show)

#añadimos un requests
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
