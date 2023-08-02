"""Tools for working with the list of current students.
This module provides functions for working with a list of students
and storing the results to disk.
"""

from datetime import datetime
from logging import _read_or_initialize_student_file
from logging import _filename
from logging import _write_student_file

def unregistered_names(grades=["V", "VI"]):
    date = datetime.now()
    """Return the names of unregistered students matching `grades` for a given date.
    Looks for student data in "logs/YYYY-MM-DD.json". If necessary, a new file will be created
    with students populated from the school schedule.
    """
    # Look for the file, if it doesn't exist create it and populate it.
    students = _read_or_initialize_student_file(date)
    return [name for name, info in students.items() if info["grade"] in grades and not info["signedIn"]]


def register(name):
    date = datetime.now()
    """Mark a student as registered for a given date.
    Looks for student data in "logs/YYYY-MM-DD.json". If necessary, a new file will be created
    with students populated from the school schedule.
    """
    students = _read_or_initialize_student_file(date)
    if name not in students:
        print(f"WARNING: Student '{name}' not found in {_filename(date)}.")

    if students[name]["signedIn"]:
        print(f"WARNING Student {name} is already registered in {_filename(date)}.")
    if not students[name]["signedIn"]:
        print(f"Registered: {name}")
        
    students[name]["signedIn"] = True
    _write_student_file(students, date)




