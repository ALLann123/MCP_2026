#!/usr/bin/python3
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from tavily import AsyncTavilyClient
from typing import Dict, List
import os
import asyncio

load_dotenv()

# Tavily API Key
TAVILY_API_KEY = os.environ['TAVILY_API_KEY']


# Initalize Async Tavily Client
tavily_client=AsyncTavilyClient(TAVILY_API_KEY)

# Port clients to connect to
PORT = os.environ.get("PORT", 10000)

# Create the MCP instance
mcp=FastMCP('web-search', host="0.0.0.0", port=PORT)

# Add a tool that uses Tavily
@mcp.tool()    #Python decorator for tool
async def web_search(query: str) -> List[Dict]:
    """
    Use this tool to search the web for information

    Args:
        query: The search query
    
    Returns:
        The search results
    """
    try:
        response = await tavily_client.search(query)
        return response["results"]
    
    except Exception as e:
        return "Error" + str(e)
    
# Run the server
if __name__=="__main__":
    mcp.run(transport="streamable-http")