#!/usr/bin/python3
from fastmcp import FastMCP
from fastmcp import Context

#create an object based on the class
mcp=FastMCP("Demo Server🚀")

#tool decorator---> LLM now knows its a tool and the format expected for inputs and the output
@mcp.tool
def add(a: int, b: int)-> int:
    #Docstring highlighting tool usage
    """Add two numbers and return the results"""
    return a+b

#Lets add another tool using MCP tool decorator--> multiplication
@mcp.tool
def multiply(a: float, b: float)-> float:
    """Multiply two numbers"""
    return a * b

#always returns the version number
@mcp.resource("config://version")
def get_version():
    return "1.0.0"

#dynamically fetches a user profile based on the ID provided--> normally in a db would have made a query request to the endpoint
@mcp.resource("user://{user_id}/profile")
def get_profile(user_id: int):
    return {"name":f"User {user_id}", "status":"active"}

#This tool logs a message, reads a resource and asks llm to summarise it.Context makes your MCP tools smarter and more interactive
@mcp.tool
async def summarize(uri: str, ctx: Context):
    await ctx.info(f"Reading resource from {uri}")
    data=await ctx.read_resource(uri)
    summary=await ctx.sample(f"Summarize this: {data.content [:500]}")
    return summary.text

if __name__=="__main__":
    #run the server--> use HTTP communication on IP will be 127.0.0.1 and port will be 8080
    mcp.run(transport="http", host="127.0.0.1", port=8080)

