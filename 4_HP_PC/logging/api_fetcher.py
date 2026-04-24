#!/usr/bin/python3
import logging
import requests


logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_data():
    url="https://jsonplaceholder.typicode.com/posts"

    try:
        logging.info("Sending request to API")
        response=requests.get(url)

        if response.status_code==200:
            logging.info("Data Fetched successfully")
            return response.json()
        else:
            logging.warning(f"Unexpected status code: {response.status_code}")

    except Exception:
        logging.error("API request failed", exc_info=True)

def main():
    data=fetch_data()
    if data:
        print(f"Fetched {len(data)} records")

if __name__=="__main__":
    main()

"""
(2_Open-claw_Agents) logging>python api_fetcher.py
Fetched 100 records

(2_Open-claw_Agents)logging>more api.log
2026-03-22 18:23:49,617 - INFO - Sending request to API
2026-03-22 18:23:50,358 - INFO - Data Fetched successfully

"""
