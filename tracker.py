import requests
from bs4 import BeautifulSoup
import time
import winsound
import mail_send

# sample URL
# to get url for your site go to websoc -> search for your class via code, number etc 
# -> att the bottom of page click -> add bookmark -> now copt that URL here.
url = 'https://www.reg.uci.edu/perl/WebSoc?YearTerm=2024-92&ShowFinals=1&ShowComments=1&Dept=COGS&CourseNum=108'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
} # to prevent bot behavior


# function to check about the enrollment status 
def check_enrollment():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')
    
    enrollments = {}
    for row in rows[1:]:  # Skip the header row
        columns = row.find_all('td')
        if len(columns) >= 12:
            code = columns[0].text.strip()
            enroll_count = int(columns[10].text.strip())  # Get the current enrollment count (Enr)
            enrollments[code] = enroll_count
    
    return enrollments



start_subject = "Enrollment Monitoring Started"
start_body = "The enrollment monitoring program has started running."
# test mail send function
mail_send.send_email(subject=start_subject,body=start_body)

# set time in which t ocheck again
# NOTE : DONT use too small of time, I beleive 180 should be the min to use to prevent ban
check_interval = 240

while True:
    current_enrollments = check_enrollment()
    
    print("Current Enrollment Data:")
    for code, count in current_enrollments.items():
        print(f"{code}: Enrolled - {count}")
        #print(current_enrollments)
    

    print("\nChecking for changes...")
    change_detected = False
    for code, count in current_enrollments.items():
        if count != 75 and count != 300:
            print(f"Enrollment count for {code} is not 75 or 300:")
            print(f"Current: Enrolled - {count}")
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            
            subject = f"Enrollment Alert: {code}"
            body = f"The enrollment count for {code} is currently {count}, which is not 75 or 300."
            mail_send.send_email(subject=subject, body=body)
            change_detected = True
            break  # Exit the loop as we only want to send one email
    
    if change_detected:
        print("Change detected. Stopping the loop.")
        end_time = time.time() + 300  # 5 minutes
        while time.time() < end_time:
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        break  # Exit the main loop after the sound has played for 5 minutes
    
    print(f"Waiting for {check_interval / 60} minutes...\n")
    time.sleep(check_interval)


