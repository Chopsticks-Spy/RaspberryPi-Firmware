import requests

IP = "http://localhost:8000/status"

def getData():
    resp = requests.get(IP).json()
    return resp

def postData(act,stage,arr,hp,tm):
    x = requests.patch(IP,json={
        "isActive": act,
        "isWin": stage,
        "activeLaser": arr,
        "hp": hp,
        "time": tm
    })
    print(x)

def setLaser(arr):
    resp = requests.get(IP).json()
    resp["activeLaser"] = arr
    requests.patch(IP,json=resp)

def setData(attribute,value):
    resp = getData()
    resp[attribute] = value
    requests.patch(IP,json=resp)
