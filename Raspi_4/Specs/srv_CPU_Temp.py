#!/usr/bin/env python3

# imports foundations
import os
import re

def raspi_CPU_temp() -> float:
    temp_str = os.popen("vcgencmd measure_temp").readline()
    CPUTemp =float(re.findall("\d+\.\d+", temp_str)[0])
    return CPUTemp

def destroy():
    pass

if __name__ == '__main__': 
    try:
        raspi_CPU_temp()
        # print(raspi_CPU_temp())
    except KeyboardInterrupt:
        destroy()