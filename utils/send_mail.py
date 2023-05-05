from email.mime.text import MIMEText
from smtplib import SMTP
from os import getenv


def send_email(message) -> str:
    sender: str = "yaroslav@example.com"
    password: str = getenv("EMAIL_PASSWORD")
    server = SMTP("smtp.gmail.com", 587)

    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "CLICK ME PLEASE!"
        server.sendmail(sender, sender, msg.as_string())
        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")
        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


if __name__ == "__main__":
    mess: str = input("Type your message: ")
    print(send_email(message=mess))

