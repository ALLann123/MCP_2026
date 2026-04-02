#!/usr/bin/python3
from fastmcp import Client
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

async def main():
    async with Client("http://127.0.0.1:8080/mcp") as client:
        
        # ✅ correct usage
        result = await client.call_tool("add", {"a": 10, "b": 5})
        mcp_result = result.content[0].text

        print("MCP Result:", mcp_result)
        print()

        llm = ChatGroq(
            temperature=0.3,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )

        response = llm.invoke(
            f"""
            You are an AI assistant using MCP tools.
            The sum of 10 and 5 is {mcp_result}.
            Explain how MCP helps with this integration.
            """
        )

        print("AI:", response.content)

asyncio.run(main())