import requests
import json
import time
from datetime import datetime

def fhose():
    visited = []
    while True:
        cntent = requests.get("https://www.meneame.net/backend/sneaker2")
        data = json.loads(cntent.content.decode('utf-8')) 
        arr2 = data["events"]
        arr = reversed(arr2)
        for i in arr:
            if int(i["id"]) not in visited:
                visited.append(int(i["id"]))
                print("Time:",datetime.fromtimestamp(int(i["ts"])))
                print("Topic:", i["sub_name"])
                print("Type:", i["type"])
                print("Title:" , i["title"])
                print("--------------------------------")
print("Loading...")
fhose()