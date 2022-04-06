#!/usr/bin/env python3

import RPi.GPIO as GPIO 
from time import sleep  

# Configuration
FAN_PIN = 26 # BCM pin used to drive transistor's base
PWM_FREQ = 25 # [Hz] Change this value if fan has strange behavior
WAIT_TIME = 1 # [s] Time to wait between each refresh

GPIO.setmode(GPIO.BCM)  
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)

fan = GPIO.PWM(FAN_PIN, PWM_FREQ)  

try:
    while 1:
        print ("start")  
        fan.start(0)              
        sleep(5)  

        print("Init testing!")
        sleep(3)
        print("Full speed")
        fan.ChangeDutyCycle(100)
        sleep(10)
        print("80%")

        fan.ChangeDutyCycle(80)
        sleep(10)
        print("60%")

        fan.ChangeDutyCycle(60)
        sleep(10)
        print("40%")

        fan.ChangeDutyCycle(40)
        sleep(10)
        print("20%")

        fan.ChangeDutyCycle(20)
        sleep(10)
        print(f"Repeate again in {WAIT_TIME} senconds")


        sleep(WAIT_TIME)



except KeyboardInterrupt:
    print("Fan ctrl interrupted by keyboard")
    GPIO.cleanup()



print ("Stop")
fan.stop()     
GPIO.cleanup()