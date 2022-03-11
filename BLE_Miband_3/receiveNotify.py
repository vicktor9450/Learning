from collections import deque
from dataclasses import dataclass
from bluepy import btle
import argparse # support args


@dataclass
class Measurement:
	temperature: float
	humidity: int
	voltage: float
	calibratedHumidity: int = 0
	battery: int = 0
	timestamp: int = 0
	sensorname: str	= ""
	rssi: int = 0 

	def __eq__(self, other): #rssi may be different, so exclude it from comparison
		if self.temperature == other.temperature and self.humidity == other.humidity and self.calibratedHumidity == other.calibratedHumidity and self.battery == other.battery and self.sensorname == other.sensorname:
			#in passive mode also exclude voltage as it changes often due to frequent measurements
			return True if args.passive else (self.voltage == other.voltage)
		else:
			return False

measurements = deque()

previousMeasurements={}
previousCallbacks={}
identicalCounters={}

class MyDelegate(btle.DefaultDelegate):
    def __init__(self, params):
        btle.DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
        # ... perhaps check cHandle
        # ... process 'data'
        global measurements
        try:
            measurement = Measurement(0,0,0)
            if args.


# Initialisation  -------

p = btle.Peripheral( address )
p.setDelegate( MyDelegate(params) )

# Setup to turn notifications on, e.g.
#   svc = p.getServiceByUUID( service_uuid )
#   ch = svc.getCharacteristics( char_uuid )[0]
#   ch.write( setup_data )


# Main loop --------
parser=argparse.ArgumentParser(allow_abbrev=False,epilog=readme)
parser.add_argument("--device","-d", help="Set the device MAC-Address in format AA:BB:CC:DD:EE:FF",metavar='AA:BB:CC:DD:EE:FF')
parser.add_argument("--battery","-b", help="Get estimated battery level, in passive mode: Get battery level from device", metavar='', type=int, nargs='?', const=1)
parser.add_argument("--count","-c", help="Read/Receive N measurements and then exit script", metavar='N', type=int)
parser.add_argument("--interface","-i", help="Specifiy the interface number to use, e.g. 1 for hci1", metavar='N', type=int, default=0)
parser.add_argument("--unreachable-count","-urc", help="Exit after N unsuccessful connection tries", metavar='N', type=int, default=0)
parser.add_argument("--mqttconfigfile","-mcf", help="specify a configurationfile for MQTT-Broker")


rounding = parser.add_argument_group("Rounding and debouncing")
rounding.add_argument("--round","-r", help="Round temperature to one decimal place (and in passive mode humidity to whole numbers)",action='store_true')
rounding.add_argument("--debounce","-deb", help="Enable this option to get more stable temperature values, requires -r option",action='store_true')

offsetgroup = parser.add_argument_group("Offset calibration mode")
offsetgroup.add_argument("--offset","-o", help="Enter an offset to the reported humidity value",type=int)

complexCalibrationGroup=parser.add_argument_group("2 Point Calibration")
complexCalibrationGroup.add_argument("--TwoPointCalibration","-2p", help="Use complex calibration mode. All arguments below are required",action='store_true')
complexCalibrationGroup.add_argument("--calpoint1","-p1", help="Enter the first calibration point",type=int)
complexCalibrationGroup.add_argument("--offset1","-o1", help="Enter the offset for the first calibration point",type=int)
complexCalibrationGroup.add_argument("--calpoint2","-p2", help="Enter the second calibration point",type=int)
complexCalibrationGroup.add_argument("--offset2","-o2", help="Enter the offset for the second calibration point",type=int)

callbackgroup = parser.add_argument_group("Callback related arguments")
callbackgroup.add_argument("--callback","-call", help="Pass the path to a program/script that will be called on each new measurement")
callbackgroup.add_argument("--httpcallback","-http", help="Pass the URL to a program/script that will be called on each new measurement")
callbackgroup.add_argument("--name","-n", help="Give this sensor a name reported to the callback script")
callbackgroup.add_argument("--skipidentical","-skip", help="N consecutive identical measurements won't be reported to callbackfunction",metavar='N', type=int, default=0)
callbackgroup.add_argument("--callback-interval","-int", help="Only invoke callbackfunction every N seconds, e.g. 600 = 10 minutes",type=int, default=0)
callbackgroup.add_argument("--influxdb","-infl", help="Optimize for writing data to influxdb,1 timestamp optimization, 2 integer optimization",metavar='N', type=int, default=0)

passivegroup = parser.add_argument_group("Passive mode related arguments")
passivegroup.add_argument("--passive","-p","--atc","-a", help="Read the data of devices based on BLE advertisements, use --battery to get battery level additionaly in percent",action='store_true')
passivegroup.add_argument("--watchdogtimer","-wdt",metavar='X', type=int, help="Re-enable scanning after not receiving any BLE packet after X seconds")
passivegroup.add_argument("--devicelistfile","-df",help="Specify a device list file giving further details to devices")
passivegroup.add_argument("--onlydevicelist","-odl", help="Only read devices which are in the device list file",action='store_true')
passivegroup.add_argument("--rssi","-rs", help="Report RSSI via callback",action='store_true')


args=parser.parse_args()

while True:
    if p.waitForNotifications(1.0):
        # handleNotification() was called
        continue

    print "Waiting..."
    # Perhaps do something else here


# Helpers