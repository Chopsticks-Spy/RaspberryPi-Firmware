import requests
import json
import random
from game import initGame
from api import *

#sampleLDR = [int(i) for i in input().split()]#random.sample(range(6),3)
sampleLDR = random.sample(range(4),2)
generateLDR = []

for i in range(6):
    if i in sampleLDR:
        generateLDR.append(1)
    else:
        generateLDR.append(0)

postData(True,0,generateLDR)
print(sampleLDR,generateLDR)

initGame(generateLDR)

postData(False,0,[0,0,0,0,0,0])

