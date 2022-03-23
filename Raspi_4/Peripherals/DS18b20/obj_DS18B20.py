#!/usr/bin/env python

#https://forums.raspberrypi.com/viewtopic.php?t=128776
# Connect to GPIO#4

# TODO:
"""
Connect to data pipeline system
   - Lam sao de assign name of sensor > vi tri, >> create instance as defined class
   - Tham khao homeassistant connect protocol
   - Tham khao nodered ( sensors > kafka > cassandra)
"""
import glob
import time

# DS18B20.py
# 2016-04-25
# Public Domain

# Typical reading
# 73 01 4b 46 7f ff 0d 10 41 : crc=41 YES
# 73 01 4b 46 7f ff 0d 10 41 t=23187

while True:

   for sensor in glob.glob("/sys/bus/w1/devices/28-0*/w1_slave"):
      id = sensor.split("/")[5]

      try:
         f = open(sensor, "r")
         data = f.read()
         f.close()
         if "YES" in data:
            (discard, sep, reading) = data.partition(' t=')
            t = float(reading) / 1000.0
            print("{} {:.1f}".format(id, t))
         else:
            print("999.9")

      except:
         pass
   print("*****************")
   time.sleep(2.0)
   