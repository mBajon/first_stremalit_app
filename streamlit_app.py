import streamlit
import pandas


fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')



streamlit.title('my parenst new healthy diner')
streamlit.header('breakfast menu')
streamlit.text('🥣 omega 3 & blueberry omlet')
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard boiled free range egg')  
streamlit.text('🥑🍞 Avocado toast')  
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.multiselect('Pick some fruits',list(my_fruit_list.index))
streamlit.dataframe(fruit_list)