
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

st.title("langchain Demo with Locallamma with Gemma3")
input_text=st.text_input("search the topic you want")

#ollama 

llm = Ollama(model="gemma3:12b")
#llm = Ollama(model="gemma3:3b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text: 
    st.write(chain.invoke({'question':input_text})) 