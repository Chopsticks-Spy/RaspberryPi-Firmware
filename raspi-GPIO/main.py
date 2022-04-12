import requests
import json
import random
from game import initGame
from api import *

#sampleLDR = [1,2,3,4,5,0]
#sampleLDR = [int(i) for i in input().split()] #random.sample(range(6),3)

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
#print(sampleLDR,generateLDR)

    initGame(generateLDR)
    
    setData("isActive",False)
    setLaser([0,0,0,0,0,0])
    #postData(False,0,[0,0,0,0,0,0],0,0)
#setData('isWin',-1)

