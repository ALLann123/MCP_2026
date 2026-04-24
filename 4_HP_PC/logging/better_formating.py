#!/usr/bin/python3
import logging

#detailed info to developers
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s - %(message)s"
)


logging.info("Info Message")

"""
    logging>python better_formating.py
2026-03-22 17:48:49,571 -INFO - Info Message

"""

