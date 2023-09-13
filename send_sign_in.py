import smtplib
import ssl
from email.message import EmailMessage
import time
from password import p
from school_schedule import free_period
# given a list of students, sends that list to a specified email address.

def send_not_signed_in_students(info):
    day_of_week = time.strftime("%A")
    unregistered_names = [name for name in info if info[name]["signed_in"] == False]
    sendAll(info,unregistered_names)
    sendGrades(info,unregistered_names)
    sendStudents(info,unregistered_names)






def sendAll(students,unregisteredNames):

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "haverfordsignin@gmail.com"  # Enter your address
    # "lkolade@haverford.org"
    receiver_email = ["nolamccl@haverford.org","lkolade@haverford.org"]  # Enter receiver address
    password = p

    content = 'Name, Grade \n'
    for name in unregisteredNames:
        content += name + ", " + students[name]["grade"] + '\n'
    freePeriod = free_period()
    month = time.strftime("%B")
    day = str(int(time.strftime("%d")))
    dayOfWeek = time.strftime("%A")

    msg = EmailMessage()
    msg.set_content(content)
    tagLine = "Students Who Didn't Sign In " + dayOfWeek + " " + month + " " + day + " " + freePeriod + " Period"
    msg['Subject'] = tagLine
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email,
                            to_addrs=receiver_email)
        




def sendGrades(students,unregisteredNames):
    # send emails to form deans
    for i in range(1,4):
    ################################### CHANGE TO FORM DEANS
        if i == 0:
            target = "III"
            dean = "nolamccl@haverford.org"
        elif i == 1:
            target = "IV"
            dean = "nolamccl@haverford.org"
        elif i == 2:
            target = "V"
            dean = "wleech@haverford.org"
        elif i == 3:
            target = "VI"
            dean = "bkenna@haverford.org"
        
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "haverfordsignin@gmail.com"  # Enter your address
        receiver_email = dean  # Enter receiver address
        password = p

        content = 'Missing Students from Form ' + target + '\n'

        for name in unregisteredNames:
            if(students[name]["grade"] == target):
                content += name + '\n'

        freePeriod = free_period()
        month = time.strftime("%B")
        day = str(int(time.strftime("%d")))
        dayOfWeek = time.strftime("%A")

        msg = EmailMessage()
        msg.set_content(content)
        tagLine = "Students Who Didn't Sign In " + dayOfWeek + " " + month + " " + day + " " + freePeriod + " Period"
        msg['Subject'] = tagLine
        msg['From'] = sender_email
        msg['To'] = receiver_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg, from_addr=sender_email,
                                to_addrs=receiver_email)
        
        




def sendStudents(students,unregisteredNames):
    recipients = []
    recipients.append("nolamccl@haverford.org")
    for name in unregisteredNames:
        recipients.append(students[name]["email"])

    print(f"sending emails to :{recipients}")

    #email = "agreattofutaxpayer@gmail.com"
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "haverfordsignin@gmail.com"  # Enter your address
    #receiver_email = email  # Enter receiver address
    password = p
    content = "You didn't sign in today. When you have free first period please sign in on the iPad at the front desk"
    freePeriod = free_period()
    month = time.strftime("%B")
    day = str(int(time.strftime("%d")))
    dayOfWeek = time.strftime("%A")
    msg = EmailMessage()
    msg.set_content(content)
    tagLine = "You didn't sign in  " + dayOfWeek + " " + month + " " + day + " " + freePeriod + " Period"
    msg['Subject'] = tagLine
    msg['From'] = sender_email
    msg["Bcc"] = recipients

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email,
                            to_addrs=recipients,)