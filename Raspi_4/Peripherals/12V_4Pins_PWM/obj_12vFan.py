import RPi.GPIO as GPIO 
from time import sleep  
      
GPIO.setmode(GPIO.BCM)  
      
GPIO.setup(14, GPIO.OUT)

 

fan = GPIO.PWM(14, 100)  
print ("start")
fan.start(0)              
sleep (5)  
print ("Run 100%")   
fan.ChangeDutyCycle(100)
sleep(5)
speed = [15,25,50,75,100]
for sp in speed:
    print ("Run", sp,"%")
    fan.ChangeDutyCycle(sp)      
    sleep(10)
fan.ChangeDutyCycle(0) 
print ("Stop")
sleep (5)  
print ("Run 100%") 
fan.ChangeDutyCycle(100)
sleep(5)  
for sp in range(15,101,5):
    print ("Run", sp,"%")
    fan.ChangeDutyCycle(sp)      
    sleep(5)
sleep(5)
print ("Stop")
fan.stop()     
GPIO.cleanup()