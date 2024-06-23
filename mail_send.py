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

# sample URL

# to get url for your site go to websoc -> search for your class via code, number etc 
# -> att the bottom of page click -> add bookmark -> now copt that URL here.
url = 'https://www.reg.uci.edu/perl/WebSoc?YearTerm=2024-92&ShowFinals=1&ShowComments=1&Dept=COGS&CourseNum=108'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
} # to prevent bot behavior



