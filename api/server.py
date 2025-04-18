from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

app = FastAPI(
    title="langchain server",
    version="1.0",
    description= "A simple API server"
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", convert_system_message_to_human=True)
llm = Ollama(model="gemma3:12b")

prompt1 = ChatPromptTemplate.from_template("write me an essay about {topic} with 200 words")
prompt2 = ChatPromptTemplate.from_template("write me an poem about {topic} with 100 words")

add_routes(app,prompt1 | model, path="/essay")
add_routes(app,prompt2 | llm, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)