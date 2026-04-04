#!/usr/bin/python3
from mcp.server.fastmcp import FastMCP

# make an MCP object
mcp = FastMCP("Math")

# make a tool decorater
@mcp.tool()
def add(a: int, b: int)-> int:
    """Add two numbers"""
    return a+b

@mcp.tool()
def multiply(a: int, b: int)-> int:
    """Multiply two numbers"""
    return a * b

if __name__=="__main__":
    mcp.run(transport = "stdio")
    