# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:58:19 2024

@author: iamrs
"""

import smtplib
import webbrowser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipient_email, email_content):
    # Set up the email message
    sender_email = "your_email@gmail.com"  # Your Gmail address
    password = "your_password"  # Your Gmail password
    subject = "Test Email"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(email_content, 'plain'))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Log in to your Gmail account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Quit the server
    server.quit()

    # Open a new tab to confirm email sent
    webbrowser.open_new_tab('https://mail.google.com/mail/u/0/#sent')

# Example usage:
recipient_email = input("Enter recipient's email address: ")
email_content = input("Enter the content of the email: ")
send_email(recipient_email, email_content)
