from datetime import datetime
import json
from send import send
import time

# filename = datetime.now().strftime("%Y-%m-%d") + ".json"

# with open(filename, "r") as file:
#     data = json.loads(file.read())
#     send(data)
print("INSTANT!")
time.sleep(1800)
print("AFTER 1800 SECONDS!")


