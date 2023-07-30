from flask import Flask, render_template, request
from sign_in import free_period, register, unregistered_names
from school_schedule import registration_open, sign_out_open


app = Flask(__name__, static_url_path='', static_folder='static',)

# if the time is between 7:00 and 9:30 return sign-in page, if time is between 9:30 and 3:15 return campus sign-out page
def current_page():
    if registration_open():
        return render_template("sign-in.html", names=unregistered_names())
    elif sign_out_open():
        return render_template("sign-out.html", names=["nolan","also nolan"])
    else:
        return render_template("closed.html")

# home is only really necessary because it is the default I think. It just sends the user off to the correct page
@app.route('/', methods=["GET", "POST"])
def home():
    return current_page()

@app.route('/sign_in', methods=["GET","POST"])
def sign_in():
    # If this is a form submission, attempt to register the student
    if request.method == "POST":
        student = request.form["student"]
        register(student)
    return current_page()
    
# check out and check in are under the umbrella of sign out.
# Time by itself is not enough to tell whether check_out or check_in should be open
# When navigated to the page checks if it CAN be open based on time.
# On a post request it returns to the sign_out home screen
@app.route('/check_out',methods=["GET","POST"])
def check_out():
    if request.method == "POST":
        None
        #check_out(student)
    elif request.method == "GET" and sign_out_open():
        return render_template("check-out.html",names=["nolan good"," nolan great"])
    # on post request go back to the sign out homescreen, or if it is now closed go to the closed screen
    return current_page()
        

@app.route('/check_in',methods=["GET","POST"])
def check_in():
    if request.method == "POST":
        None
        #check_in(student)
    elif request.method == "GET" and sign_out_open():
        return render_template("check-in.html",names=["nolan","nolan2"])
        # on post request go back to the sign out homescreen, or if it is now closed go to the closed screen
    return current_page()

if __name__ == '__main__':
    app.run(debug=False, port=8000)
