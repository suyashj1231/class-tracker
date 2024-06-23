import requests
from bs4 import BeautifulSoup
import time
import winsound
import mail_send

# sample URL
# to get url for your site go to websoc -> search for your class via code, number etc 
# -> att the bottom of page click -> add bookmark -> now copt that URL here.
url = 'https://www.reg.uci.edu/perl/WebSoc?YearTerm=2024-92&ShowFinals=1&ShowComments=1&Dept=COGS&CourseNum=108'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
} # to prevent bot behavior

# test mail send function
mail_send.send_email() 