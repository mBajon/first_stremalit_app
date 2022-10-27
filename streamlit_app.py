import streamlit
import pandas


fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_list = fruit_list.set_index('Fruit')


streamlit.title('my parenst new healthy diner')
streamlit.header('breakfast menu')
streamlit.text('🥣 omega 3 & blueberry omlet')
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard boiled free range egg')  
streamlit.text('🥑🍞 Avocado toast')  
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = streamlit.multiselect('Pick some fruits',list(fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)