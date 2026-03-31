#!/usr/bin/python3
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# llm setup
llm = ChatGroq (
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

# trigger llm
response = llm.invoke("Hello")
print(f" AI: {response.content}")
