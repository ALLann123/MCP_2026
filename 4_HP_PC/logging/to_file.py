#!/usr/bin/python3
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error Message")


"""
(2_Open-claw_Agents) \logging>python to_file.py

(2_Open-claw_Agents) \logging>more app.log
2026-03-22 17:53:21,517 - INFO - Info message
2026-03-22 17:53:21,517 - WARNING - Warning message
2026-03-22 17:53:21,517 - ERROR - Error Message

"""