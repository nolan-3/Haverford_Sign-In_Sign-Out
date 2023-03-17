from datetime import datetime
import json
from send import send
import time

print("Task Called")
dayOfWeek = time.strftime("%A")
if dayOfWeek == "Wednesday":
    time.sleep(1800)
    print("Task Slept For 1800 Seconds")

filename = datetime.now().strftime("%Y-%m-%d.json")
with open(filename, "r") as file:
    data = json.loads(file.read())
    send(data)


