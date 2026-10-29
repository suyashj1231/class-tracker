# class-tracker

Watches a UCI course section on WebSoc and tells you when a seat opens. It polls the WebSoc page for your course codes, reads the enrollment column, and when a count changes from the full value it plays a sound and emails you.

## How it works

`tracker.py` fetches the WebSoc results page for the course codes in `url` every 3 minutes, parses the table with BeautifulSoup, and maps each section code to its current enrollment. When a section's count stops matching the full capacity, it sends an email through Gmail SMTP (`mail_send.py`), then plays a Windows system alert (`winsound`) on repeat for five minutes so you notice even away from your inbox, and exits.

The 3-minute interval keeps the request rate low enough that the registrar's site is unlikely to block you.

## Setup

```bash
pip install requests beautifulsoup4
export TRACKER_SENDER_EMAIL=you@gmail.com
export TRACKER_APP_PASSWORD="xxxx xxxx xxxx xxxx"   # a Gmail app password, not your login
export TRACKER_RECIPIENT=you@gmail.com              # optional, defaults to the sender
python tracker.py
```

Create the app password at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) (2-step verification has to be on).

To track a different class, search for it on [WebSoc](https://www.reg.uci.edu/perl/WebSoc), copy the results URL, paste it into `url` in `tracker.py`, and set the full capacity numbers the check compares against.

## Limits

- The alert sound uses `winsound`, so it only works on Windows. On macOS, swap it for `os.system("afplay /System/Library/Sounds/Glass.aiff")`.
- Capacity values are hardcoded to the class I was watching (75 and 300).
