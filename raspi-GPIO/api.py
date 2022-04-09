import requests

IP = "http://localhost:8000/status"

def postData(act,stage,arr):
    requests.patch(IP,json={
        "isActive": act,
        "isWin": stage,
        "activeLaser": arr
    })

def setLaser(arr):
    resp = requests.get(IP).json()
    resp["activeLaser"] = arr
    requests.patch(IP,json=resp)
