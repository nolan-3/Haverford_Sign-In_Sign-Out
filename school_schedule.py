"""Tools for working with the school schedule.
This module handles the internal representation of the school schedule,
handling vacations, registration times and the current free period.
"""
from pytz import timezone
from datetime import time, datetime
import numpy as np
from send_sign_out import send_checked_out_students
import json

# All times are localized and interpreted in this timezone.
TIMEZONE = timezone("America/New_York")

# Print a warning for dates outside this range:
VALID_START = datetime(2023, 9, 6, tzinfo=TIMEZONE)
VALID_END = datetime(2024, 6, 7, tzinfo=TIMEZONE)
# Holidays and schedule information
#   FREE_PATTERN[0] should correspond to FIRST_DAY
#   holiday format: "YYYY-MM-DD"
FIRST_DAY = datetime(2023, 9, 7, tzinfo=TIMEZONE)
FREE_PATTERN = ["A", "E", "B", "F", "C", "G", "D"]
HOLIDAYS = ['2023-09-25','2023-10-09','2023-10-20','2023-11-10','2023-11-13','2023-11-22','2023-11-23','2023-11-24','2023-12-18',
            '2023-12-19','2023-12-20','2023-12-21','2023-12-22','2023-12-25','2023-12-26','2023-12-27','2023-12-28',
            '2023-12-29','2024-01-01','2024-01-15','2024-02-16','2024-02-19','2024-03-15','2024-03-22','2024-03-25',
            '2024-03-26','2024-03-27','2024-03-28','2024-03-29','2024-04-26','2024-04-29','2023-05-27']

# Registration opening/closing times
REGISTRATION_OPEN_TIME = time(6, 59)
REGISTRATION_CLOSE_TIME = time(9, 31)
REGISTRATION_WEDNESDAY_CLOSE_TIME = time(10, 1)
SCHOOL_CLOSE_TIME = time(15, 16)

# Free version of python anywhere only allows one scheduled task 
def check_for_closing_email():
    timestamp=datetime.now(TIMEZONE)
    if timestamp.hour == 15 and timestamp.minute == 17:
        filename = datetime.now().strftime("%Y-%m-%d.json")
        with open(filename, "r") as file:
            data = json.loads(file.read())
            send_checked_out_students(data)



def registration_open():
    check_for_closing_email()
    """Check whether registration is open at a given datetime."""
    timestamp=datetime.now(TIMEZONE)
    print(f"Checking registration at {timestamp}.")
    _validate_datetime(timestamp)

    # check if it is a school day
    if not _open_day(timestamp):
        print("Today is not a school day")
        return False

    # Wednesday :|
    if timestamp.strftime("%A") == "Wednesday":
        return (REGISTRATION_OPEN_TIME <= timestamp.time()) and (timestamp.time() <= REGISTRATION_WEDNESDAY_CLOSE_TIME)
    
    # Otherwise
    return (REGISTRATION_OPEN_TIME <= timestamp.time()) and (timestamp.time() <= REGISTRATION_CLOSE_TIME)

def sign_out_open():
    check_for_closing_email()
    timestamp=datetime.now(TIMEZONE)
    _validate_datetime(timestamp)

    # check if it is a school day
    if not _open_day(timestamp):
        return False

    # Wednesday :|
    if timestamp.strftime("%A") == "Wednesday":
        return (REGISTRATION_WEDNESDAY_CLOSE_TIME <= timestamp.time()) and (timestamp.time() <= SCHOOL_CLOSE_TIME)
    
    # Otherwise
    return (REGISTRATION_CLOSE_TIME <= timestamp.time()) and (timestamp.time() <= SCHOOL_CLOSE_TIME)



def free_period():
    """Determine the element of FREE_PATTERN corresponding to the given day."""
    timestamp=datetime.now()
    print(f"Checking free period for {timestamp}.")

    # Free periods rotate according to FREE_PATTERN, but only on school days
    school_days = np.busday_count(FIRST_DAY.strftime(
        "%Y-%m-%d"), timestamp.strftime("%Y-%m-%d"), holidays=HOLIDAYS)
    return FREE_PATTERN[school_days % 7]


def _validate_datetime(timestamp):
    """Print a warning if the datetime is outside of the expected range."""
    if timestamp < VALID_START or timestamp > VALID_END:
        print(f"WARNING The given datetime '{timestamp}' is outside the valid"
              f" range ({VALID_START} to {VALID_END}), this may lead to unexpected behaviour.")


def _open_day(timestamp):
    """Check whether a given date is a holiday"""
    _validate_datetime(timestamp)
    return np.is_busday(timestamp.strftime("%Y-%m-%d"), holidays=HOLIDAYS)