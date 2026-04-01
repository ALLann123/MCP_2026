#!/usr/bin/python3
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
import asyncio

# loading .env file in the code
load_dotenv()

# llm setup
llm = ChatGroq (
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",
                "command": "python",
                "args": [
                    "C:/Users/PC/Desktop/golang/2026/MCP_Adapter/mcp_server.py"
                ],
            }
        }
    )

    tools = await client.get_tools()
    agent = create_agent(
        llm,
        tools,
        system_prompt="""You are a careful math assistant.

    You MUST call one tool at a time.
    Do NOT nest tool calls.
    First compute intermediate results, then use them in the next step.
    """
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role":"user", "content" : "What's (3+5) x12"}]}
    )

    print(math_response)

    print("\n***************************************")

    for msg in math_response["messages"]:
        if msg.type == "ai" and msg.content:
            print("\n🤖 Answer:\n")
            print(msg.content)

if __name__=="__main__":
    asyncio.run(main())



"""
    cmd> >python client_mcp.py
{'messages': [HumanMessage(content="What's (3+5) x12", additional_kwargs={}, response_metadata={}, id='b7bfcd51-05ad-4f15-bdc9-304853c0633e'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': '8rw1rzvx1', 'function': {'arguments': '{"a":3,"b":5}', 'name': 'add'}, 'type': 'function'}, {'id': 'xnhea6777', 'function': {'arguments': '{"a":8,"b":12}', 'name': 'multiple'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 36, 'prompt_tokens': 320, 'total_tokens': 356, 'completion_time': 0.113944516, 'completion_tokens_details': None, 'prompt_time': 0.056229274, 'prompt_tokens_details': None, 'queue_time': 0.10741793, 'total_time': 0.17017379}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_68f543a7cc', 'service_tier': 'on_demand', 'finish_reason': 'tool_calls', 'logprobs': None, 'model_provider': 'groq'}, id='lc_run--019d43a8-be1e-7af3-a824-465aa86decb4-0', tool_calls=[{'name': 'add', 'args': {'a': 3, 'b': 5}, 'id': '8rw1rzvx1', 'type': 'tool_call'}, {'name': 'multiple', 'args': {'a': 8, 'b': 12}, 'id': 'xnhea6777', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 320, 'output_tokens': 36, 'total_tokens': 356}), ToolMessage(content=[{'type': 'text', 'text': '8', 'id': 'lc_a12b56b3-12e3-458b-b6f7-a1706e9b6b9f'}], name='add', id='99ac4930-798e-4efc-a59a-d0b5bb1565bc', tool_call_id='8rw1rzvx1', artifact={'structured_content': {'result': 8}}), ToolMessage(content=[{'type': 'text', 'text': '96', 'id': 'lc_f390d877-0d63-416b-b5d6-ea16e1d24eb0'}], name='multiple', id='51a447ab-c43a-42ee-a7a9-3130181af477', tool_call_id='xnhea6777', artifact={'structured_content': {'result': 96}}), AIMessage(content='The answer is 96.', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 7, 'prompt_tokens': 374, 'total_tokens': 381, 'completion_time': 0.025350145, 'completion_tokens_details': None, 'prompt_time': 0.06044387, 'prompt_tokens_details': None, 'queue_time': 0.180122809, 'total_time': 0.085794015}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_e65acd3773', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None, 'model_provider': 'groq'}, id='lc_run--019d43a8-e38d-7ea2-b0c1-01fb30c37f9a-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 374, 'output_tokens': 7, 'total_tokens': 381})]}

***************************************

🤖 Answer:

The answer is 96.

"""