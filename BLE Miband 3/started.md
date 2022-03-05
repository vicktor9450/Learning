https://medium.com/@yogeshojha/i-hacked-xiaomi-miband-3-and-here-is-how-i-did-it-43d68c272391

https://github.com/yogeshojha/MiBand3
- Install requirements.txt

## Manipulate with bluePy
https://elinux.org/RPi_Bluetooth_LE#Using_Bluetooth_LE_with_Python

### BluePy
https://github.com/IanHarvey/bluepy
https://ianharvey.github.io/bluepy-doc/index.html

### Codex
sudo apt-get install python-pip
sudo apt-get install libglib2.0-dev
sudo pip install bluepy

Test:
    sudo blescan



## REF
https://dontvacuum.me/talks/


## Fix bugs
### ImportError: No module named Crypto.Cipher when "from Crypto.Cipher import AES"
>> Using python2 venv and install -r requirements.txt

### Cant authenticate to Miband 3???


## Mi band 3
address: 
    ED:47:EC:6A:56:20

Firmware version
    2.4.0.32

Scan BLE devices
    sudo hcitool lescan

Get Company Identifier
https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers/

## BLE payload
*******************************************************************************************
BLE packet - Custom: A4:C1:38:6D:E8:3A 00 1312161a183ae86d38c1a4400aed0d7a0b528304 -69
Temperature:  26.24
Humidity:  35.65
Battery voltage: 2.938 V
RSSI: -69 dBm
Battery: 82 %
Exception when calling handler with a BLE advertising event: NameError("name 'humidity' is not defined")
*******************************************************************************************
