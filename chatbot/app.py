# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

# sreamlit framework 

st.title("langchain Demo with GEMINI API")
input_text=st.text_input("search the topic you want")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash ", convert_system_message_to_human=True)
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text: 
    st.write(chain.invoke({'question':input_text})) 