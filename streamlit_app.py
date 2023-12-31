import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') # Changing the index to have the Fruit coulmn name in the list index

# Multiselect Picklist
# streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index)) # or streamlit.multiselect("Pick some fruits:",list(my_fruit_list.Fruit))
fruit_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]
# Display the table on page
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruit_to_show)

# Create repeatable code block function
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
   

# New section for API display
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
   else:
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
  
except URLError as e:
    streamlit.error()


streamlit.header("The fruit load list contains:")
# snowflake related function to add a click button
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from fruit_load_list")
      return my_cur.fetchall()
      
# add a button
if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)

#Allow end user to add a fruit to the list

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
new_fruit = streamlit.text_input('Enter your new fruit to add')
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("INSERT into fruit_load_list VALUES('" + insert_row_snowflake + "')")
      return "Thanks for adding " + new_fruit
      my_cnx.close()






# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")



streamlit.stop()

add_my_fruit = streamlit.text_input('What Fruit would you like to add','kiwi')
streamlit.write('Thanks for Adding ', add_my_fruit)
my_cur.execute("INSERT INTO FRUIT_LOAD_LIST Values('from Streamlit')")
