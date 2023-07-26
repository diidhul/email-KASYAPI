import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "business@kasyapi.com"
receiver_email = "sianakkepo@gmail.com"
password = input("Masukan Password : ")

message = MIMEMultipart("alternative")
message["Subject"] = "Test_V.1.0.0"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
html = open

# Turn these into plain/html MIMEText objects
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("mail.kasyapi.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
