
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email):
    # Set up the email message
    sender_email = "your_email@gmail.com"  # Your Gmail address
    password = "your_password"  # Your Gmail password
    subject = "Test Email"
    message = "This is a test email sent from Python."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Log in to your Gmail account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, to_email, msg.as_string())

    # Quit the server
    server.quit()

# Example usage:
recipient_email = input("Enter recipient's email address: ")
send_email(recipient_email)
