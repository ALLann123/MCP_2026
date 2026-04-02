#!/usr/bin/python3
import logging

#detailed info to developers
logging.basicConfig(level=logging.DEBUG)


logging.debug("Debug Message")

#General events
logging.info("Info Message")

#something unexpected
logging.warning("Warning message")

#something failed
logging.error("Error Message")

#Serious failure
logging.critical("Critical Message")

