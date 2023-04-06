"""Tools for working with the school schedule.
This module handles the internal representation of the school schedule,
handling vacations, registration times and the current free period.
"""
from pytz import timezone
from datetime import time, datetime
import numpy as np

# All times are localized and interpreted in this timezone.
TIMEZONE = timezone("America/New_York")

# Print a warning for dates outside this range:
VALID_START = datetime(2022, 9, 8, tzinfo=TIMEZONE)
VALID_END = datetime(2023, 6, 6, tzinfo=TIMEZONE)
# Holidays and schedule information
#   FREE_PATTERN[0] should correspond to FIRST_DAY
#   holiday format: "YYYY-MM-DD"
FIRST_DAY = datetime(2022, 9, 8, tzinfo=TIMEZONE)
FREE_PATTERN = ["A", "E", "B", "F", "C", "G", "D"]
# It seems we had a day off in November represented by the non-factual holiday 2022-22-28
HOLIDAYS = ['2022-09-23', '2022-09-26', '2022-10-05', '2022-10-21', '2022-11-14', '2022-11-23', '2022-11-24', '2022-11-25',
            '2022-11-28',
            '2022-12-19', '2022-12-20', '2022-12-21', '2022-12-22', '2022-12-23', '2022-12-26', '2022-12-27',
            '2022-12-28', '2022-12-29', '2022-12-30', '2023-01-02', '2023-01-16', '2023-02-17', '2023-02-20',
            '2023-03-17', '2023-03-24', '2023-03-27', '2023-03-28', '2023-03-29', '2023-03-30', '2023-03-31',
            '2023-04-07', '2023-05-01', '2023-05-29']


# Registration opening/closing times
OPEN_TIME = time(7, 0)
CLOSE_TIME = time(9, 46)
WEDNESDAY_CLOSE_TIME = time(10, 16)


def registration_open():
    """Check whether registration is open at a given datetime."""
    timestamp=datetime.now(TIMEZONE)
    print(f"Checking registration at {timestamp}.")
    _validate_datetime(timestamp)

    # check if it is a school day
    # # # # # # if not _open_day(timestamp):
    # # # # # #     return False

    # Wednesday :|
    if timestamp.strftime("%A") == "Wednesday":
        return (OPEN_TIME <= timestamp.time()) and (timestamp.time() <= WEDNESDAY_CLOSE_TIME)
    
    # Otherwise
    return (OPEN_TIME <= timestamp.time()) and (timestamp.time() <= CLOSE_TIME)


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

print(datetime.now(TIMEZONE))