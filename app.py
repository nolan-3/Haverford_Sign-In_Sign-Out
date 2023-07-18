from flask import Flask, render_template, request
from registration import free_period, register, unregistered_names
from school_schedule import registration_open


app = Flask(__name__, static_url_path='', static_folder='static',)


@app.route('/', methods=["GET", "POST"])
def home():

    # If this is a form submission, attempt to register the student
    if request.method == "POST":
        student = request.form["student"]
        register(student)
    # if the time is between 7:00 and 9:30 return active page, if time is outside 7:00 - 9:30 return the inactive page
    # store the students who login between 7:00 and 9:30 and send an email at 9:30 with the list
    if registration_open():
        return render_template("check-in.html", names=unregistered_names())

    return render_template("closed.html")


if __name__ == '__main__':
    app.run(debug=False, port=8000)
