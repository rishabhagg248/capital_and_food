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
        st.error(f"API Error: {str(e)}")
        st.write("Using fallback data instead...")
        
        # Fallback data when API fails
        fallback_data = {
            "india": {"capital": "New Delhi", "food_item": "Butter Chicken, Chole Bhature, Paranthas, Kebabs, Biryani"},
            "france": {"capital": "Paris", "food_item": "Croissant, Escargot, Coq au Vin, Macarons, Baguette"},
            "japan": {"capital": "Tokyo", "food_item": "Sushi, Ramen, Tempura, Yakitori, Miso Soup"},
            "usa": {"capital": "Washington D.C.", "food_item": "Half-Smoke, Mumbo Sauce, Chesapeake Bay Crab, Cherry Blossom Cake, Ethiopian Cuisine"},
            "uk": {"capital": "London", "food_item": "Fish and Chips, Bangers and Mash, Shepherd's Pie, Afternoon Tea, Tikka Masala"},
            "germany": {"capital": "Berlin", "food_item": "Currywurst, Döner Kebab, Sauerbraten, Pretzels, Schnitzel"},
            "italy": {"capital": "Rome", "food_item": "Pasta Carbonara, Pizza al Taglio, Gelato, Supplì, Maritozzi"},
            "spain": {"capital": "Madrid", "food_item": "Paella, Jamón Ibérico, Churros, Gazpacho, Tortilla Española"},
            "china": {"capital": "Beijing", "food_item": "Peking Duck, Dumplings, Hot Pot, Zhajiangmian, Baozi"},
            "brazil": {"capital": "Brasília", "food_item": "Feijoada, Pão de Açúcar, Brigadeiro, Coxinha, Açaí"}
        }
        
        # Try to find the country in fallback data
        country_data = fallback_data.get(country.lower())
        if country_data:
            response = country_data
            
            # Display the fallback data
            st.header(response['capital'])
            food = response['food_item'].strip().split(",")
            st.write(f"Top 5 items of {response['capital']}:")
            
            for ct, item in enumerate(food, 1):
                st.write(f"{ct}. {item.strip()}")
        else:
            st.write(f"Sorry, no data available for '{country}'. Try: India, France, Japan, USA, UK, Germany, Italy, Spain, China, or Brazil.")
