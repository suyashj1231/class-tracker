# needs a gmail account 
# requirements email and pass word set up via https://support.google.com/accounts/answer/185833
# using this method get a app password so you dont need verification to 2FA while using it
# create a custom password

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "xxxx@gmail.com" # email via which email gets sent
sender_password = "xxx xx x x xx x " # pasword set via app password on site I gave above
recipient_email = "yyyyy@gmail.com" # you can use the same mail to prevent spam detection


def send_email(subject="", body="", sender_email=sender_email, sender_password = sender_password, recipient_email = recipient_email):
    try:
        print("Sending email...")
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Email notification sent successfully.")
    except Exception as e: # anything unknown
        print(f"An error occurred while sending the email: {str(e)}")

