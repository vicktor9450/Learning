#!/usr/bin/env python3

# Imports
from msilib.schema import Error
import RPi.GPIO as GPIO #lib for GPIO

redLEDPin = 4  # setup for RGB led #color RED
blueLEDPin = 27 # setup for RGB led #color GREEN


# LED control
def turnLedOn(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnLedOff(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def destroy():
    GPIO.cleanup()

def main():
    turnLedOn(blueLEDPin) # sensor hot > blue on

if __name__ == '__main__': 
    try:
        main()
    except Error:
        print("Errorr..? how to trace them")
    except KeyboardInterrupt:
        destroy()

