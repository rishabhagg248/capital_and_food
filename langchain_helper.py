import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain, LLMChain
import streamlit as st

# Use Streamlit secrets - with fallback for local testing
api_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

os.environ["HUGGINGFACEHUB_API_TOKEN"] = api_token

# Use Hugging Face Inference API instead of local pipeline
llm = HuggingFaceEndpoint(
    repo_id="microsoft/DialoGPT-medium",  # This model is more reliable
    max_length=100,
    temperature=0.1,
    huggingfacehub_api_token=api_token
)

def cap_and_food(country):
    capital_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=['country'],
            template="What is the capital of {country}? Answer with just the capital city name."
        ),
        output_key="capital"
    )
    
    food_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=['capital'],
            template="Tell me 5 famous food items in {capital}. Answer with a comma separated list of food items."
        ),
        output_key="food_names"
    )
    
    seq_chain = SequentialChain(
        chains=[capital_chain, food_chain], 
        input_variables=['country'],
        output_variables=['capital', 'food_names']
    )
    
    response = seq_chain.invoke({"country": country})
    return response
