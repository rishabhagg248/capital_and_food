import os
from langchain_huggingface import HuggingFacePipeline
import torch
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
import key.txt

os.environ["HUGGINGFACEHUB_API_TOKEN"]=secret_key
local_llm = HuggingFacePipeline.from_model_id(
    model_id="google/flan-t5-large",
    task="text2text-generation",
    model_kwargs={
        "temperature": 0,
        "max_length": 100
    }
)

def cap_and_food(country):

    capital_chain = LLMChain(
        llm=local_llm,
        prompt=PromptTemplate(
            input_variables=['country'],
            template="What is the capital of {country}? answer with just the capital city name."
        ),
        output_key="capital"
    )

    food_chain = LLMChain(
        llm=local_llm,
        prompt=PromptTemplate(
            input_variables=['capital'],
            template="Tell me 5 famous food items in {capital}. answer with a comma separated list of food items."
        ),
        output_key="food_item"
    )

    seq_chain = SequentialChain(chains=[capital_chain, food_chain], input_variables=['country'],
                                output_variables=['capital', 'food_item'])
    response = seq_chain.invoke({"country": country})
    return response