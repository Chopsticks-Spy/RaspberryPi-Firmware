import usb
import requests
from practicum import *
from time import sleep


devices = find_mcu_boards()
mcu = McuBoard(devices[0])

response = requests.get('http://localhost:8000/status').json()
print(response)

while True:
    response = requests.get('http://localhost:8000/status').json()
    mcu.usb_write(request=0,index=0,value=response["ls1"])
    mcu.usb_write(request=0,index=1,value=response["ls2"])
    mcu.usb_write(request=0,index=2,value=response["ls3"])
