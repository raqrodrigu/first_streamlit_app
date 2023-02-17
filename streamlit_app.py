import streamlit
#importamos pandas para leer nuestro CSV de s3 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#importamos pandas para leer nuestro CSV de s3 
#import pandas

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

########## NEW SECTION
def get_fruityvice_data(this_fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
 #cogemos la version json yla normalizamos 
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized

#añadimos un requests
#import requests
streamlit.header("Fruityvice Fruit Advice!")
#nueva estructura para separar el codigo que se carga una vez del que se debe repetir
try:
   #añadimos un buscador de la fruta que queramos saber
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_chice:
         #streamlit.write('The user entered ', fruit_choice)
         streamlit.error("Please select a fruit to get information.")
   else:
        back_from_function = get_fruityvice_data(fruit_choice)
        # lo mostramos como tabla
        streamlit.dataframe(fruityvice_normalized)
     
except URLError as e:
   streamlit.error()
     
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())

streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
       my_cur.execute("SELECT * from fruit_load_list")
       return my_cur.fetchall()
 
 #Add a button to load the fruit
 if streamlit.button('Get Fruit Load List'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows=get_fruit_load_list()
     streamlit.dataframe(my_data_row)
  

#paramos la ejecucion
streamlit.stop()

#boton para que el usuario añada frutas a la lista
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding" + new_fruit
add_my_fruit = stramlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
 
