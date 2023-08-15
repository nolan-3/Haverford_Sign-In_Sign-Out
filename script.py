# Script is called at 9:46 each day to send emails, if the day is wednesday wait until 10:16
from datetime import datetime
import json
from send_sign_in import send_not_signed_in_students
import time

print("Closing Script Called")
dayOfWeek = time.strftime("%A")
if dayOfWeek == "Wednesday":
    time.sleep(1800)
    print("Wednesday: Task Slept For 1800 Seconds")
    

filename = datetime.now().strftime("%Y-%m-%d.json")
with open(filename, "r") as file:
    data = json.loads(file.read())
    send_not_signed_in_students(data)
    print("Emails Sent")
