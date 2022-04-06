#!/usr/bin/env python3

# Imports
import RPi.GPIO as GPIO #lib for GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

GPIO.setup(relayPin01, GPIO.OUT) # Init for Relay channel 1 of 4 at GPIO #???- Connect to ???
GPIO.setup(relayPin02, GPIO.OUT) # Init for Relay channel 2 of 4 at GPIO #??? - Connect to ???
GPIO.setup(relayPin03, GPIO.OUT) # Init for Relay channel 3 of 4 at GPIO #???- Connect to ???
GPIO.setup(relayPin04, GPIO.OUT) # Init for Relay channel 4 of 4 at GPIO #??? - Connect to ???

relayPin01 = ??? # pin for Relay controls ???
relayPin02 = ??? # pin for Relay controls ???
relayPin03 = ??? # pin for Relay controls ???
relayPin04 = ??? # pin for Relay controls ???

def destroy():
    GPIO.cleanup()
def hitHumidifier(relayPin): # Applied for LOW relay
    # Turn on for 0.5s then off
    GPIO.output(relayPin, 0) # ON
    sleep(0.5)
    GPIO.output(relayPin, 1) # OFF
def continueHumidify():
    # touch 1 lan neu dang tat
    # touch 2 lan neu dang o che do period
    pass
def periodHumidify():
    pass
# TODO: Need to tracking present status of humidifier
# why: 1 hit > ON(連続) > 1 hit > ON (periodly) > 1 hit > OFF
# Humidify se co 3 trang thai: off, on and blink tuong ung 0 - 1 - 2

def main():
    pass

if __name__ == '__main__': 
    main()