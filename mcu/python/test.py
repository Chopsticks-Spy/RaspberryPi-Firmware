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
    for i in range(6):
        mcu.usb_write(request=0,index=i,value=response["activeLaser"][i])
