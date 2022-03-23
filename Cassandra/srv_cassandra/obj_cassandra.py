#!/usr/bin/env python3

# TODO:
"""
- Support more security authentication
    - Start from cassandra cluster containers
    - Generate login protocol here
"""
# Imports
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# some useful funcs writting data to cassandra 
def writeCPUdata_to_cassandra(sensor, location, temp):
    session.execute(
    """
    INSERT INTO sensor_data_by_location (sensor_name , location , date , temp) VALUES (%s, %s, %s, %s)
    """,
    (sensor, location, datetime.utcnow(), temp))
    print("inserted raspi thermal data")
    
def writeDHT22data_to_cassandra(sensor, location, temp, humid):
    session.execute(
    """
    INSERT INTO sensor_data_by_location (sensor_name , location , date , temp, humid) VALUES (%s, %s, %s, %s, %s)
    """,
    (sensor, location, datetime.utcnow(), temp, humid))
    print("inserted system thermal humid data")

