# Script is called at 9:46 each day to send emails, if the day is wednesday wait until 10:16
from datetime import datetime
import json
from send_sign_in import send_not_signed_in_students
from send_sign_out import send_checked_out_students
import time

day_of_week = time.strftime("%A")
print(f"Closing Script Called On '{day_of_week}'")
if day_of_week == "Wednesday":
    time.sleep(1800)
    print("Wednesday: Task Slept For 1800 Seconds")
    

filename = datetime.now().strftime("%Y-%m-%d.json")
# with open(filename, "r") as file:
#     data = json.loads(file.read())
#     send_not_signed_in_students(data)
print("Sign In Email Sent")

if day_of_week == "Wednesday":
    time.sleep(1800)

filename = datetime.now().strftime("%Y-%m-%d.json")
with open(filename, "r") as file:
    data = json.loads(file.read())
    send_checked_out_students(data)
    print("Sign Out Email Sent")
