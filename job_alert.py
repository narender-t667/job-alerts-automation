import smtplib
from datetime import date
from email.mime.text import MIMEText
import os

JOBS = {
    "LinkedIn": "https://www.linkedin.com/jobs/search/?keywords=entry%20level%20python%20developer-level",
    "Indeed": "https://in.indeed.com/jobs?q=entry+level+python+ml&l=India",
    "Naukri": "https://www.naukri.com/entry-level-data-scientist-jobs",
    "Foundit/Byte": "https://www.foundit.in/search/data-scientist-jobs-entry-level",
    "AngelList/Wellfound": "https://wellfound.com/jobs",
    "Instahyre": "https://www.instahyre.com/jobs/?q=data+scientist+entry+level",
    "Cutshort": "https://cutshort.io/jobs/entry-level-python-jobs",
    "Hirist": "https://www.hirist.com/jobs/search?query=entry+level+ml",
    "Internshala": "https://internshala.com/internships/machine-learning%2C-python-jobs",
}

def send_email():
    body = "📢 Job Links for Today:\n\n" + "\n".join([f"{k}: {v}" for k, v in JOBS.items()])
    msg = MIMEText(body)
    msg["Subject"] = f"{date.today()} – Entry-Level Tech Job Links"
    msg["From"] = "narendergoud2004@gmail.com"
    msg["To"] = "rayanchupavanrayanchu@gmail.com, prasadvemula016@gmail.com"
    email = "narendergoud2004@gmail.com"
    app_password = "xwnzbboenwkinbuh"

    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s.login(email, app_password)
    s.send_message(msg)
    s.quit()

if __name__ == "__main__":
    send_email()
