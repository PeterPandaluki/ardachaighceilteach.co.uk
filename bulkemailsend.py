#!/usr/bin/env python
# coding: utf-8


import smtplib
import ssl
import csv
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# read in data
addressfile = sys.argv[3]
messagefile = sys.argv[2]
message_subject = sys.argv[1]
with open(messagefile) as file:
    message = file.read()


# Login information

port = 465
serverlogin = "karl.jones@blueyonder.co.uk"
password = 'CathM009'
# compose message
# Add header to message
message_text = """  + message
From: {} <{}>
To: <{}>
Subject: {}


Dear Sir/Madam,

""" + message

from_address = "karl.jones@blueyonder.co.uk"
# to_address = "karl.jones@blueyonder.co.uk"


# Send message funtion
# Loop through address file and send message to each address
def send_messages():
    my_name = "Karl Jones"
    with open(addressfile) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for to_address in reader:
            # message = MIMEMultipart('alternative')
            # message['From'] = from_address
            # message['To'] = to_address
            # message['Subject'] = message_subject
            # message.attach(MIMEText(message_text, 'text'))
            message_to_send = message_text.format(my_name,
                                                  from_address,
                                                  to_address,
                                                  message_subject)
            server.sendmail(from_address,
                            to_address,
                            message_to_send)


# Create ssl context
context = ssl.create_default_context()

# Open server connection, send messages and close connection
with smtplib.SMTP_SSL("smtp.virginmedia.com", port, context=context) as server:
    server.login(serverlogin, password)
    send_messages()
    server.quit()
