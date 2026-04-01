#!/usr/bin/python3
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
import asyncio

# Loading .env file in the code
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
            "web-search":{
                "transport":"http",  #HTTP-based remote server
                "url":"http://localhost:8000/mcp",  # Ensure you start your weather server on port 8000
            }
        }
    )

    tools = await client.get_tools()
    agent = create_agent(        
        llm,
        tools,
        system_prompt="""You are a careful Online Research assistant.

    You MUST call one tool at a time.
    Do NOT nest tool calls.
    First compute intermediate results, then use them in the next step.
    """)
    web_search= await agent.ainvoke(
        {"messages":[{"role":"user", "content":" What is the current price of XMR in dollars?"}]}
    )

    print(web_search)

    print("\n*******************AI Response No debug**********************")
    
    for msg in web_search["messages"]:
        if msg.type == "ai" and msg.content:
            print("\n🤖 Answer:\n")
            print(msg.content)

if __name__=="__main__":
    asyncio.run(main())


"""
    cmd>>python client.py
{'messages': [HumanMessage(content=' What is the current price of XMR in dollars?', additional_kwargs={}, response_metadata={}, id='0d58690f-3196-4f51-bc19-64b5b8b5e550'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'bhgp678k2', 'function': {'arguments': '{"query":"current price of XMR in dollars"}', 'name': 'web_search'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 21, 'prompt_tokens': 311, 'total_tokens': 332, 'completion_time': 0.04551932, 'completion_tokens_details': None, 'prompt_time': 0.023359219, 'prompt_tokens_details': None, 'queue_time': 0.061465273, 'total_time': 0.068878539}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_f8b414701e', 'service_tier': 'on_demand', 'finish_reason': 'tool_calls', 'logprobs': None, 'model_provider': 'groq'}, id='lc_run--019d43d8-654b-7632-ae78-0bc77e3b0c16-0', tool_calls=[{'name': 'web_search', 'args': {'query': 'current price of XMR in dollars'}, 'id': 'bhgp678k2', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 311, 'output_tokens': 21, 'total_tokens': 332}), ToolMessage(content=[{'type': 'text', 'text': '[{"url":"https://www.tradingview.com/symbols/XMRUSD/","title":"Monero Price and Chart — XMR to USD - TradingView","content":"The current price of Monero (XMR) is 327.27 USD — it has risen 2.03% in the past 24 hours. Try placing this info into the context by checking out what coins are","score":0.91901255,"raw_content":null},{"url":"https://paybis.com/xmr-to-usd/","title":"XMR to USD - Monero to United States dollar - Paybis","content":"The current value of 1 XMR in United States dollar is 329.21. In the last 24 hours, Monero has changed by -1.2%. The current Monero market cap is 6.1B USD.","score":0.91490877,"raw_content":null},{"url":"https://www.coinbase.com/en-ca/converter/xmr/usd","title":"Convert Monero (XMR) to US Dollar (USD) | Coinbase Canada","content":"The exchange rate of Monero is decreasing. The current value of 1 XMR is $328.75 USD. In other words, to buy 5 Monero, it would cost you $1,643.77 USD.","score":0.8877607,"raw_content":null},{"url":"https://finance.yahoo.com/quote/XMR-USD/","title":"Monero XMR (XMR-USD) Live Price, News, Chart & Price History","content":"The last known price of Monero is 335.1362132 USD and is up 3.98 over the last 24 hours. It is currently trading on 366 active market(s) with $82,248,971.35","score":0.8812988,"raw_content":null},{"url":"https://coinmarketcap.com/currencies/monero/","title":"Monero price today, XMR to USD live price, marketcap and chart","content":"The live Monero price today is $327.94 USD with a 24-hour trading volume of $85,862,892 USD. We update our XMR to USD price in real-time. Monero is down 2.24%","score":0.87605256,"raw_content":null}]', 'id': 'lc_d95e0c90-1b66-45b4-991d-2180e0082cfb'}], name='web_search', id='2e1958f2-9005-4fff-b7f9-3a49bb1a6c08', tool_call_id='bhgp678k2', artifact={'structured_content': {'result': [{'url': 'https://www.tradingview.com/symbols/XMRUSD/', 'title': 'Monero Price and Chart — XMR to USD - TradingView', 'content': 'The current price of Monero (XMR) is 327.27 USD — it has risen 2.03% in the past 24 hours. Try placing this info into the context by checking out what coins are', 'score': 0.91901255, 'raw_content': None}, {'url': 'https://paybis.com/xmr-to-usd/', 'title': 'XMR to USD - Monero to United States dollar - Paybis', 'content': 'The current value of 1 XMR in United States dollar is 329.21. In the last 24 hours, Monero has changed by -1.2%. The current Monero market cap is 6.1B USD.', 'score': 0.91490877, 'raw_content': None}, {'url': 'https://www.coinbase.com/en-ca/converter/xmr/usd', 'title': 'Convert Monero (XMR) to US Dollar (USD) | Coinbase Canada', 'content': 'The exchange rate of Monero is decreasing. The current value of 1 XMR is $328.75 USD. In other words, to buy 5 Monero, it would cost you $1,643.77 USD.', 'score': 0.8877607, 'raw_content': None}, {'url': 'https://finance.yahoo.com/quote/XMR-USD/', 'title': 'Monero XMR (XMR-USD) Live Price, News, Chart & Price History', 'content': 'The last known price of Monero is 335.1362132 USD and is up 3.98 over the last 24 hours. It is currently trading on 366 active market(s) with $82,248,971.35', 'score': 0.8812988, 'raw_content': None}, {'url': 'https://coinmarketcap.com/currencies/monero/', 'title': 'Monero price today, XMR to USD live price, marketcap and chart', 'content': 'The live Monero price today is $327.94 USD with a 24-hour trading volume of $85,862,892 USD. We update our XMR to USD price in real-time. Monero is down 2.24%', 'score': 0.87605256, 'raw_content': None}]}}), AIMessage(content='The current price of XMR in dollars is approximately $327.94 USD.', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 831, 'total_tokens': 848, 'completion_time': 0.047523048, 'completion_tokens_details': None, 'prompt_time': 0.044903169, 'prompt_tokens_details': None, 'queue_time': 0.09113869, 'total_time': 0.092426217}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_dae98b5ecb', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None, 'model_provider': 'groq'}, id='lc_run--019d43d8-7658-7260-a29d-33a9fa9724fa-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 831, 'output_tokens': 17, 'total_tokens': 848})]}

*******************AI Response No debug**********************

🤖 Answer:

The current price of XMR in dollars is approximately $327.94 USD.

"""