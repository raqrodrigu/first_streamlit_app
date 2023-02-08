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

#Agregaremos un widget interactivo para el usuario llamado Selección múltiple que permitirá a los usuarios 
#elegir las frutas que desean en sus batidos.
#hasta este paso el selector se ponía en forma de números
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#pedimos que nos muestre los datos en la pagina
streamlit.dataframe(my_fruit_list)
 
