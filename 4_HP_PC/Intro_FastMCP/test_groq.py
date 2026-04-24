#!/usr/bin/python3
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()

#build our model
llm=ChatGroq(
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

result=llm.invoke("Hello?")

print(f"AI: {result.content}")
