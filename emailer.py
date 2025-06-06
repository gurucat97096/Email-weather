import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv

load_dotenv()
def send_weather_email(weather_info):
    sender = os.getenv("EMAIL_SENDER")
    receiver = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("weather_email.html")
    html_content = template.render(weather=weather_info)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"{weather_info['城市']} 今日天氣"
    msg["From"] = sender
    msg["To"] = receiver
    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
    print(" Email 已寄出")
