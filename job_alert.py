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
    msg["From"] = "narendergoud2004@gmail.com"
    msg["To"] = "rayanchupavanrayanchu@gmail.com, prasadvemula016@gmail.com"
    email = "narendergoud2004@gmail.com"
    app_password ="xwnzbboenwkinbuh"

    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s.login(email, app_password)
    s.send_message(msg)
    s.quit()

if __name__ == "__main__":
    send_email()
