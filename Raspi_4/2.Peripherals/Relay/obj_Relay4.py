#!/usr/bin/env python3

# Imports
import RPi.GPIO as GPIO #lib for GPIO

relayPin = 10 # pin for Relay controls CPU fan

GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT, initial=0) # Init for Relay channel 2 of 4 at GPIO #10

def destroy():
    GPIO.cleanup()

def main():
    GPIO.output(10, 0) #0 mean GDN - turn on the fan

if __name__ == '__main__': 
    main()