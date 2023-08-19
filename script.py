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
    time.sleep(3000)
    print("slept for 3000 seconds")
    time.sleep(3000)
    print("slept for 6000 seconds")
    time.sleep(3000)
    print("slept for 9000 seconds")
    time.sleep(3000)
    print("slept for 12000 seconds")
    time.sleep(3000)
    print("slept for 15000 seconds")
    time.sleep(3000)
    print("slept for 18000 seconds")

else:
    time.sleep(3300)
    print("slept for 3300 seconds")
    time.sleep(3300)
    print("slept for 6600 seconds")
    time.sleep(3300)
    print("slept for 9900 seconds")
    time.sleep(3300)
    print("slept for 13200 seconds")
    time.sleep(3300)
    print("slept for 16500 seconds")
    time.sleep(3300)
    print("slept for 19800 seconds")

print("task slept until 3:15")

filename = datetime.now().strftime("%Y-%m-%d.json")
with open(filename, "r") as file:
    data = json.loads(file.read())
    send_checked_out_students(data)
    print("Sign Out Email Sent")
