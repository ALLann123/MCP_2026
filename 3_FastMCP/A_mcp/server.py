#!/usr/bin/python3
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from tavily import TavilyClient
from typing import Dict, List
import os

load_dotenv()

# Tavily API Key
TAVILY_API_KEY = os.environ['TAVILY_API_KEY']

# Initialize Tavily Client
tavily_client=TavilyClient(TAVILY_API_KEY)

# The port we will connect to
PORT=os.environ.get("PORT", 10000)

# create an MCP server
mcp = FastMCP('web-search', host = "0.0.0.0", port=PORT)

# Add a tool that uses Tavily
@mcp.tool()         # Python decorator for tool
def web_search(query: str)-> List[Dict]:
    """
    Use this tool to search the web for information

    Args:
        query: The search query
    
    Returns:
        The search results
    """
    try:
        response = tavily_client.search(query)
        return response["results"]
    
    except Exception as e:
        return "Error" + str(e)
    
# Run the server
if __name__=="__main__":
    mcp.run(transport="streamable-http")
    