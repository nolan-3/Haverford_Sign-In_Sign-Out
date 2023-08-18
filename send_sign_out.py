import smtplib
import ssl
from email.message import EmailMessage
import time
from password import p
from school_schedule import free_period
# given a list of students, sends that list to a specified email address.

def send_checked_out_students(students):
    dayOfWeek = time.strftime("%A")
    #if dayOfWeek == "Saturday" or dayOfWeek == "Sunday":
        #return
    #else:
    checked_out_students = [name for name in students if students[name]["checked_out"] == True]
    sendAll(students,checked_out_students)

def sendAll(students,checked_out_students):

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "haverfordsignin@gmail.com"  # Enter your address
    # "lkolade@haverford.org"
    receiver_email = ["nolamccl@haverford.org"]  # Enter receiver address
    password = p

    content = 'Name, Checked Back In, Grade \n'
    for name in checked_out_students:
        content += name + ", " + students[name]["grade"] + ", " + students[name]["checked_in"] + '\n'
    month = time.strftime("%B")
    day = str(int(time.strftime("%d")))
    dayOfWeek = time.strftime("%A")

    msg = EmailMessage()
    msg.set_content(content)
    tagLine = "Students Who Went Off Campus " + dayOfWeek + " " + month + " " + day
    msg['Subject'] = tagLine
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email,
                            to_addrs=receiver_email)