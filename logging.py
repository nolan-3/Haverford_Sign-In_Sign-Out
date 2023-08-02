import os
import json
from get_students import get_students
from school_schedule import free_period

LOG_FORMAT = "%Y-%m-%d.json"

def _filename(date):
    """Construct a filename corresponding to a given date. Returns "logs/YYYY-MM-DD.json" """
    return date.strftime(LOG_FORMAT)


def _write_student_file(students, date):
    """Write student information to "logs/YYYY-MM-DD.json", overwriting any existing contents."""
    with open(_filename(date), "w+") as file:
        json.dump(students, file)

# handled by getStudents
# def _initialize_students(date):
#     """Initialize a list of students with free period on a given date."""
#     free_students = {name : info for name, info in all_students().items() if info["free"] == free_period() }
#     return {name: {**info, "signedIn": False} for name, info in free_students.items()}


def _read_or_initialize_student_file(date):
    """Open a student file for reading, initializing a new file if necessary.

    Looks for student data in "logs/YYYY-MM-DD.json".
    New files will be initialized from the school school schedule.
    """
    if not os.path.exists(_filename(date)):
        print("creating daily file")
        _write_student_file(get_students(free_period()), date)

    with open(_filename(date), "r") as file:
        return json.load(file)