import requests
import json
import random
from game import initGame
from api import *

while True:
    while not getData()["isActive"]:
        pass
    print("BEGIN")
    sampleLDR = random.sample(range(4),2)
    generateLDR = []

    for i in range(6):
        if i in sampleLDR:
            generateLDR.append(1)
        else:
            generateLDR.append(0)

    postData(True,0,generateLDR,5,0)

    initGame(generateLDR)
    
    setData("isActive",False)
    setData("activeLaser",[0,0,0,0,0,0])