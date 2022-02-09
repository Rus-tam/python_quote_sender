import smtplib

# Отправка писем в данном случае работает только для гуглопочты


class MailSender:
    def __init__(self, sender, password, recipiend):
        self.sender = sender
        self.password = password
        self.recipiend = recipiend

    def send(self, subject, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.sender, password=self.password)
            connection.sendmail(
                from_addr=self.sender,
                to_addrs=self.recipiend,
                msg=f"Subject: {subject}\n\n{message}"
            )

