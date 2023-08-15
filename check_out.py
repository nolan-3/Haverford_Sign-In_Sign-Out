"""
Uses the same tools as 'sign_in.py'
"""

from datetime import datetime
from custom_logging import _read_or_initialize_student_file
from custom_logging import _filename
from custom_logging import _write_student_file

def not_checked_out_names(grades=["V", "VI"]):
    date = datetime.now()
    students = _read_or_initialize_student_file(date)
    return [name for name, info in students.items() if info["grade"] in grades and not info["checked_out"]]


def check_out_student(name):
    date = datetime.now()
    students = _read_or_initialize_student_file(date)
    if name not in students:
        print(f"WARNING: Student '{name}' not found in {_filename(date)}.")

    if students[name]["checked_out"]:
        print(f"WARNING Student {name} is already checked out in {_filename(date)}.")
    if not students[name]["checked_out"]:
        print(f"Checked out: {name}")
        
    students[name]["checked_out"] = True
    _write_student_file(students, date)




