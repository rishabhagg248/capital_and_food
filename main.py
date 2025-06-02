import streamlit as st
from langchain_helper import cap_and_food

st.title("Capital and Food!")
country = st.sidebar.text_input("Enter the name of the country: ")
st.write("Enter the name of a country and the program will give you the capital of that country and the top 5 famous foods of that city.")
st.write("(Success rate 90%)\n\n")

if country:
    response=cap_and_food(country)
    st.header(response['capital']).strip()
    food=response['food_item'].strip().split(",")
    st.write("Top 5 items of ", response['capital'].strip(), ":\n")
    ct=1
    for item in food:
        st.write(ct, " ", item)
        ct+=1
