#! /usr/bin/env python

import LCDdrivers
from time import sleep
from datetime import datetime
from subprocess import check_output

display = LCDdrivers.Lcd() # init the Instance

# Get IP 
def GetIP() -> str:
    IP = check_output(["hostname", "-I"]).split()[0]
    return IP.decode('utf-8')

# Send time to screen
def GetDateTime() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def GetTime() -> str:
    return datetime.now().strftime("%H:%M:%S")

def GetDate() -> str:
    return datetime.now().strftime("%Y-%m-%d")

# Control backlight
def TuronlCD():
    display.lcd_backlight(1)
def TurnoffLCD():
    display.lcd_backlight(0)

# display long string
def long_string(display, text='', num_line=1, num_cols=16):
    """ 
    Parameters: (driver, string to print, number of line to print, number of columns of your display)
    Return: This function send to display your scrolling string.
    """
    if len(text) > num_cols:
        display.lcd_display_string(text[:num_cols], num_line)
        sleep(1)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i+num_cols]
            display.lcd_display_string(text_to_print, num_line)
            sleep(0.2)
        sleep(1)
    else:
        display.lcd_display_string(text, num_line)

try:
    print("Writing to display")
    print(GetIP())
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    while True:
        # display.lcd_backlight()
        display.lcd_display_string(GetDate(), 1)
        display.lcd_display_string(GetTime(), 2)
        sleep(1)  
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
