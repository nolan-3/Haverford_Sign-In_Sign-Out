from datetime import datetime
import json
from send import send

filename = datetime.now().strftime("%Y-%m-%d") + ".json"

with open(filename, "r") as file:
    data = json.loads(file.read())
    send(data)


