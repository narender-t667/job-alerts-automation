import smtplib
from datetime import date
from email.mime.text import MIMEText
import os

JOBS = [
    "https://in.linkedin.com/jobs/entry-level-data-science-jobs",
    "https://www.indeed.com/q-entry-level-python-developer-jobs.html",
    "https://angel.co/jobs",
    "https://internshala.com/internships/machine-learning%2C-python-jobs",
]

def send_email():
    body = "📢 Job Links for Today:\n\n" + "\n".join(JOBS)
    msg = MIMEText(body)
    msg["Subject"] = f"{date.today()} – Entry-Level Tech Job Links"
    msg["From"] = "pavanrayanchu03@gmail.com"
    msg["To"] = "rayanchupavanrayanchu@gmail.com@gmail.com"

    email = os.environ["pavanrayanchu03@gmail.com"]
    app_password = os.environ["Rpavan@03"]

    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s.login(email, app_password)
    s.send_message(msg)
    s.quit()

if __name__ == "__main__":
    send_email()
