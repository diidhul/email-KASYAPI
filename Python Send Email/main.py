import os
import pandas as pd
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Read email
df = pd.read_csv(
    "D:\\02_Projects\\Kasyapi\\email-KASYAPI\\Python Send Email\\Data Email\\data buyer until 25 feb.csv"
)
email_kirim = []
for email in df["Email"]:
    email_kirim.append(email)

sender_email = "business@kasyapi.com"

load_dotenv()
password = os.getenv("PASSWORD")

# Create the plain-text and HTML version of your message
html = open(
    "D:\\02_Projects\\Kasyapi\\email-KASYAPI\\Python Send Email\\Isi Email\\email_pinang-fix.html",
    "r",
    encoding="utf-8",
).read()

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("mail.kasyapi.com", 465, context=context) as server:
    server.login(sender_email, password)

    for receiver in email_kirim:
        # Create a new MIMEMultipart message for each receiver
        message_individual = MIMEMultipart("alternative")
        message_individual["Subject"] = "Test_V.1.0.3"
        message_individual["From"] = sender_email
        message_individual["To"] = receiver

        # Turn the HTML content into a MIMEText object
        part2 = MIMEText(html, "html")

        # Add HTML part to MIMEMultipart message
        message_individual.attach(part2)

        # Send email to the current receiver
        server.sendmail(sender_email, receiver, message_individual.as_string())
