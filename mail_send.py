# needs a gmail account 
# requirements email and pass word set up via https://support.google.com/accounts/answer/185833
# using this method get a app password so you dont need verification to 2FA while using it
# create a custom password

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "xyz@gmail.com" # email via which email gets sent
sender_password = "vksy giop ssry xlxz" # pasword set via app password on site I gave above
recipient_email = "xyz@gmail.com"# you can use the same mail to prevent spam detection


