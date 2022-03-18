#!/usr/bin/env python3

# Install pip3 libs
    # requirements.txt
    # pip install -r requirements.txt

# Try to import libs
    # Make sure that libs have been installed

# Imports
import signal
import json
import os
import sys
import logging
from time import sleep
from uuid import uuid1
import requests                                                                    # (1)

# Global varible
LED_GPIO_PIN = 21                   # GPIO Pin that LED is connected to
THING_NAME_FILE = 'thing_name.txt'  # The name of our "thing" is persisted into this file
URL = 'https://dweet.io'            # Dweet.io service API
last_led_state = None               # Current state of LED ("on", "off", "blinking")
thing_name = None                   # Thing name (as persisted in THING_NAME_FILE)
led = None  


# Initialize Logging

logging.basicConfig(level=logging.WARNING)  # Global logging configuration
logger = logging.getLogger('main')  # Logger for this module
logger.setLevel(logging.INFO)  # Debugging for this file. 

# Initialize GPIO

def abc():
    """Describe what to do with this func"""
    pass






