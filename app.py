from flask import Flask, render_template, request, redirect
from getStudents import getStudents
from pytz import timezone
from getFreePeriod import getFreePeriod
from send import send
import datetime
import json


app = Flask(__name__, static_url_path='', static_folder='static',)

# All times are localized and interpreted in this timezone.
TIMEZONE = timezone("America/New_York")

OPEN_TIME = datetime.time(7, 0)
CLOSE_TIME = datetime.time(9, 46)


# Manage the school schedule, and keep track of registered students
class RegistrationManager():

    # Constructor
    def __init__(self):

        # Always refresh on startup
        self.read()

    # Destructor
    def __del__(self):
        # Shut down the recurring events when finished
        #self.cron.shutdown()
        None

    # Check whether registration is currently open
    def isOpen(self):
        timeNow = datetime.datetime.now(TIMEZONE).time()
        print(f"Refreshed at: '{timeNow}'")

        if self.isWednesday():
            return (OPEN_TIME <= timeNow) and (timeNow <= datetime.time(10, 15))
        else:
            return (OPEN_TIME <= timeNow) and (timeNow <= CLOSE_TIME)


    # Get the names of all currently unregistered students
    def unregisteredNames(self):
        return [name for name in self.data if self.data[name].signedIn == False]
    

    def read(self):
        filename = datetime.datetime.now().strftime("%Y-%m-%d.json")
        try:
            with open(filename, "r") as file:
                self.data = json.loads(file.read())

        except:
            self.refreshStudents()
            self.write()


    def write(self):
        print("write is called")
        filename = datetime.datetime.now().strftime("%Y-%m-%d.json")

        with open(filename,"w") as file:
            json.dump(self.data, file)


    # Actions
    # =========================
    # Refresh the list of students for the current day
    def refreshStudents(self):
        print("Refreshing student list.")
        self.freePeriod = getFreePeriod()
        self.data = getStudents(self.freePeriod)

    # Send mail containing the list of unregistered students
    def sendMail(self):
        print("Sending mail.")
        send(self.data, self.unregisteredNames())

    # Attempt to register a student name, returns false if there's an error
    def register(self, student):        
        if not self.isOpen():
            return "Error: Registration is not open"

        self.read()

        if student not in self.data:
            return "Error: Student not found"

        if self.data[student].signedIn:
            return "Warning: Student already signed in"

        self.data[student].signedIn = True
        self.write()
        return "Ok"


    def isWednesday(self):
        dayOfWeek = datetime.datetime.now(TIMEZONE).strftime("%A")
        return(dayOfWeek == "Wednesday")

registration = RegistrationManager()


@app.route('/', methods=["GET", "POST"])
def home():

    # If this is a form submission, attempt to register the student
    if request.method == "POST":
        student = request.form["student"]
        print(f"Registering '{student}': {registration.register(student)}")
    # if the time is between 7:00 and 9:30 return active page, if time is outside 7:00 - 9:30 return the inactive page
    # store the students who login between 7:00 and 9:30 and send an email at 9:30 with the list
    if registration.isOpen():
        return render_template("open.html", names=registration.unregisteredNames())

    return render_template("closed.html")


if __name__ == '__main__':
    app.run(debug=False, port=8000)


