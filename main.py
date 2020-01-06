import requests
import json
import time
from datetime import datetime
import db

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
                print("Id:", i["id"])
                print("Topic:", i["sub_name"])
                print("Type:", i["type"])
                print("Title:" , i["title"])
                print("User:" , i["who"])
                print("--------------------------------")
                if i["type"] == "problem":
                    db.addproblem(i["id"], i["who"], i["title"], i["sub_name"])
                elif i["type"] == "new":
                    db.addposts(i["id"], i["who"], i["title"], i["sub_name"])
                elif i["type"] == "comment":
                    db.addcomment(i["id"], i["who"], i["title"], i["sub_name"])
                elif i["type"] == "vote":
                    db.addvote(i["id"], i["who"], i["title"], i["sub_name"])
print("Loading...")
fhose()