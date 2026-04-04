#!/usr/bin/python3
from fastmcp import FastMCP
from dotenv import load_dotenv
from tavily import TavilyClient
from typing import Dict, List
import os

# Import environment variables
load_dotenv()

#set the API key
TAVILY_API_KEY = os.environ['TAVILY_API_KEY']

#initialize client
tavily_client = TavilyClient(TAVILY_API_KEY)

# Port we will connect to
PORT =  os.environ.get("PORT", 8000)

# Create an MCP Server
mcp=FastMCP('web-search')

# add the tool that uses Tavily
@mcp.tool()   # Python decorator for tool
def web_search(query: str) -> List[Dict]:
    """
    Use this tool to search the web for information

    Args:
        query: The Search query

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
    mcp.run(
        transport = "streamable-http",
        host="0.0.0.0",
        port = int(PORT)
    )

