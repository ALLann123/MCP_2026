#!/usr/bin/python3
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os 
import asyncio

# Get APIs
load_dotenv()
api_key=os.getenv("GITHUB_TOKEN")

#create llm
llm=ChatOpenAI(
    model="gpt-4o",
    openai_api_key=api_key,
    base_url="https://models.inference.ai.azure.com"
)
async def main():
    client = MultiServerMCPClient({
        "math":{
            "command":"python",
            "args": ["J:\\2_Open-claw_Agents\\langchain_mcp_adapter\\server.py"],
            "transport":"stdio"
        },
        "web-search":{
            "url":"http://localhost:8000/mcp",
            "transport":"streamable_http"
        }
    })

    tools = await client.get_tools()
    
    def call_model(state: MessagesState):
        llm_with_tools = llm.bind_tools(tools)
        response = llm_with_tools.invoke(state["messages"])
        return {"messages": response}

    # ===Start building the graph====
    builder = StateGraph(MessagesState)

    # add node
    builder.add_node("call_model", call_model)
    builder.add_node("tools", ToolNode(tools))

    # connect nodes with edges
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges("call_model", tools_condition)
    builder.add_edge("tools", "call_model")
    builder.add_edge("call_model", END)

    app = builder.compile()
    return app

if __name__ == "__main__":
    app = asyncio.run(main())
    # Test with a math question first
    result = asyncio.run(app.ainvoke({"messages": [HumanMessage(content="What is the current price of XMR in dollars and multiply with 135 to convert to ksh.(Highlight tools used)")]}))
    print("AI:", result["messages"][-1].content)


"""
Tool Used both our tools available:
    cmd> >python client_langraph.py
AI: The current price of XMR in USD is approximately $328. When multiplied by 135 to convert to Ksh, the equivalent amount is 44,280 Ksh.

Tools used:
1. **Web Search**: To find the current price of XMR in USD.
2. **Multiply Function**: To calculate the conversion to Ksh
"""