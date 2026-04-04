#!/usr/bin/python3
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

def search_with_client(query):
    """Search using Tavily client directly"""
    client=TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

    #Basic search
    response=client.search(
        query=query,
        search_depth="basic",
        max_results=5,
        include_answer=True
    )
    return response

search_query="President Kenya"
result=search_with_client(search_query)

print(f"OUTPUT:\n {result}")

"""
    cmd>>python tavily_test.py
OUTPUT:
 {'query': 'President Kenya', 'follow_up_questions': None, 'answer': 'William Ruto is the current president of Kenya, having taken office in 2022. He previously served as deputy president from 2013 to 2022. His predecessor was Uhuru Kenyatta.', 'images': [], 'results': [{'url': 'https://en.wikipedia.org/wiki/President_of_Kenya', 'title': 'President of Kenya', 'content': '# President of Kenya. The **president of the Republic of Kenya** (Swahili: *Rais wa Jamhuri ya Kenya*) is the head of state and head of government of the Republic of Kenya. As with most other countries, the president of Kenya has a presidential standard to signify their status as the country\'s head of state and government. The presidential standards of Kenya\'s presidents since the country\'s independence have been as follows:. Qualifications and disqualifications for election as President – Kenya Law Reform Commission (KLRC)". Election of the President – Kenya Law Reform Commission (KLRC)". Term of office of President – Kenya Law Reform Commission (KLRC)". Functions of the President – Kenya Law Reform Commission (KLRC)". | Politics | |  | | --- | | * Constitution * Elections * Foreign relations * Government * Human rights   + Intersex   + LGBT rights * Judiciary * Law enforcement * Military * Parliament   + Building "Parliament Buildings (Kenya)") 
"""