import smtplib
import os
from email.message import EmailMessage


class Notification:
    def __init__(self, title, price, url):
        self.product_title = title
        self.product_price = price
        self.url = url
        self.my_email = os.environ.get("my_email")
        self.password = os.environ.get("password")
        self.receiver_email = "alisadaintanvir@gmail.com"

    def send_notification(self):
        message = f"{self.product_title} is now {self.product_price}"
        try:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(self.my_email, self.password)
                email_msg = EmailMessage()
                email_msg.set_content(f"{message}\n{self.url}")
                email_msg["Subject"] = "Amazon Price Alert!"
                email_msg["From"] = self.my_email
                email_msg["To"] = self.receiver_email

                connection.send_message(email_msg)

        except smtplib.SMTPException as error:
            print(f"an error occur while sending the mail:{error}")
        else:
            print("Email has been sent successfully.")
