import streamlit
import pandas

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

# New section for API display
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response) # displays response time
# streamlit.text(fruityvice_response.json())

# displayes json version and normlaise it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Output as a table
streamlit.dataframe(fruityvice_normalized)
