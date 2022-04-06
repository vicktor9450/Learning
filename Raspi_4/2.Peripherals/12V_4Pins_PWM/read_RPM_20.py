#!/usr/bin/env python

import time
import pigpio
import read_RPM

RPM_GPIO = 20
RUN_TIME = 1000.0
SAMPLE_TIME = 2.0

pi = pigpio.pi()

p = read_RPM.reader(pi, RPM_GPIO)

start = time.time()

while (time.time() - start) < RUN_TIME:

   time.sleep(SAMPLE_TIME)

   RPM = p.RPM()
   
   print("RPM={}".format(int(RPM+0.5)))

p.cancel()

pi.stop()

