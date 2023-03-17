"""Tools for working with the list of current students.

This module provides functions for working with a list of students
and storing the results to disk.
"""

from school_schedule import free_period

import os
import csv
import json
import logging
from datetime import datetime

ALL_STUDENTS = "students.csv"
LOG_FORMAT = "logs/%Y-%m-%d.json"

def all_students():
    """Read the list of all students, and construct a dictionary indexed by name."""
    with open(ALL_STUDENTS, "r") as file:
        csv_rows = csv.DictReader(file)
        return {row["name"] : row for row in csv_rows}


def unregistered_names(date=datetime.now(), grades=["III", "IV", "V", "VI"]):
    """Return the names of unregistered students matching `grades` for a given date.

    Looks for student data in "logs/YYYY-MM-DD.json". If necessary, a new file will be created
    with students populated from the school schedule.
    """
    # Look for the file, if it doesn't exist create it and populate it.
    students = _read_or_initialize_student_file(date)

    return [name for name, info in students.items() if info["grade"] in grades and not info["signedIn"]]


def register(name, date=datetime.now()):
    """Mark a student as registered for a given date.

    Looks for student data in "logs/YYYY-MM-DD.json". If necessary, a new file will be created
    with students populated from the school schedule.
    """
    students = _read_or_initialize_student_file(date)
    if name not in students:
        logging.error(f"Student '{name}' not found in {_filename(date)}.")

    if students[name]["signedIn"]:
        logging.warn(f"Student {name} is already registered in {_filename(date)}.")

    students[name]["signedIn"] = True
    _write_student_file(students, date)

def _filename(date):
    """Construct a filename corresponding to a given date. Returns "logs/YYYY-MM-DD.json" """
    return date.strftime(LOG_FORMAT)

def _write_student_file(students, date):
    """Write student information to "logs/YYYY-MM-DD.json", overwriting any existing contents."""
    with open(_filename(date), "w+") as file:
        json.dump(students, file)

def _initialize_students(date):
    """Initialize a list of students with free period on a given date."""
    free_students = {name : info for name, info in all_students().items() if info["free"] == free_period(date) }
    return {name: {**info, "signedIn": False} for name, info in free_students.items()}


def _read_or_initialize_student_file(date):
    """Open a student file for reading, initializing a new file if necessary.
    
    Looks for student data in "logs/YYYY-MM-DD.json".
    New files will be initialized from the school school schedule.
    """
    if not os.path.exists(_filename(date)):
        _write_student_file(_initialize_students(date), date)

    with open(_filename(date), "r") as file:
        return json.load(file)