import smtplib
from datetime import date
from email.mime.text import MIMEText

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
    msg["From"] = "you@gmail.com"
    msg["To"] = "you@gmail.com"

    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s.login("you@gmail.com", "YOUR_APP_PASSWORD")
    s.send_message(msg)
    s.quit()

if __name__ == "__main__":
    send_email()

