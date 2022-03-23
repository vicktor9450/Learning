#!/bin/bash
#File: chapter01/run_on_boot.sh

# Absolute path to Virtual Environment python interpreter
# Mod
PYTHON=/home/pi/pyiot/chapter01/venv/bin/python

# Absolute path to Python script
# Mod
SCRIPT=/home/pi/pyiot/chapter01/gpio_pkg_check.py

# Absolute path to output log file
# Mod
LOG=/home/pi/pyiot/chapter01/gpio_pkg_check.log

echo -e "\n####### STARTUP $(date) ######\n" >> $LOG

$PYTHON $SCRIPT >> $LOG 2>&1
