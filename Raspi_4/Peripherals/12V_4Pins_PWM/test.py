#!/usr/bin/env python3

import RPi.GPIO as GPIO 
from time import sleep  
      
GPIO.setmode(GPIO.BCM)  
GPIO.setup(14, GPIO.OUT)

fan = GPIO.PWM(14, 80)  