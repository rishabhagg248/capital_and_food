import streamlit as st
from langchain_helper import cap_and_food

st.title("Capital and Food!")
country = st.sidebar.text_input("Enter the name of the country: ")
st.write("Enter the name of a country and the program will give you the capital of that country and the top 5 famous foods of that city.")
st.write("(Success rate 90%)\n\n")

if country:
    try:
        # Show loading spinner
        with st.spinner('Getting information...'):
            response = cap_and_food(country)
        
        # Display capital (fixed st.header usage)
        st.header(response['capital'])
        
        # Display foods (fixed key access and method call)
        if 'food_item' in response and response['food_item']:
            food = response['food_item'].strip().split(",")
            st.write(f"Top 5 items of {response['capital']}:")
            
            for ct, item in enumerate(food, 1):
                st.write(f"{ct}. {item.strip()}")
        else:
            st.write("No food information available.")
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.write("Please try again with a different country name.")
