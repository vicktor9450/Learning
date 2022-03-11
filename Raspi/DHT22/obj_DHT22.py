#!/usr/bin/env python3

# Prerequisites 
    # https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/

    # sudo apt-get update
    # sudo apt-get upgrade

    # sudo apt-get install python3-dev python3-pip

    # sudo python3 -m pip install --upgrade pip setuptools wheel

    # sudo pip3 install Adafruit_DHT


# import Adafruit_DHT

# DHT_SENSOR = Adafruit_DHT.DHT22
# DHT_PIN = 7

# while True:
#     humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

#     if humidity is not None and temperature is not None:
#         print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
#     else:
#         print("Failed to retrieve data from humidity sensor")



# new Lib applicant
# Prerequisites
    # https://www.piddlerintheroot.com/dht22/

    # sudo apt-get update

    # sudo apt-get install build-essential python-dev

    # sudo pip3 install adafruit-circuitpython-dht

    # https://github.com/adafruit/Adafruit_CircuitPython_DHT/blob/main/examples/dht_simpletest.py

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D17, use_pulseio=False)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

# def DHT22 init return object
# def DHT22 return data
while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)