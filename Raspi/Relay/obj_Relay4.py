#!/usr/bin/env python3

# Imports
import RPi.GPIO as GPIO #lib for GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(relayDHT22FanPin, GPIO.OUT) # Init for Relay channel 1 of 4 at GPIO #17- Connect to DHT22 cooling fan
GPIO.setup(relayCPUFanpin, GPIO.OUT) # Init for Relay channel 2 of 4 at GPIO #10 - Connect to CPU cooling fan

relayCPUFanpin = 10 # pin for Relay controls CPU fan
relayDHT22FanPin = 17 # pin for Relay control DHT22 Sensor fan

def destroy():
    GPIO.cleanup()

def main():
    GPIO.output(10, 0) #0 mean GDN - turn on the fan

if __name__ == '__main__': 
    main()