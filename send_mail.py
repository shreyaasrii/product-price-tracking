import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class EmailSender:
    def __init__(self, from_email='onlinedatateacker@gmail.com', from_password = 'pigqzuxmcrdefvap', smtp_server='smtp.gmail.com', smtp_port=587):
        self.from_email = from_email
        self.from_password = from_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_mail(self, subject, body, to_emails):
        message = MIMEMultipart()
        message["From"] = self.from_email
        message["To"] = to_emails
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.from_email, self.from_password)
            server.sendmail(self.from_email, to_emails, message.as_string())
