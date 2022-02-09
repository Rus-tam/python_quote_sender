import datetime as dt
from reader import Reader
from mail_sender import MailSender

sender = ""
password = ""
recipiend = ""

reader = Reader()
quote = reader.get_single_quote("quotes.txt")

mail_sender = MailSender(sender, password, recipiend)

now = dt.datetime.now()
day_of_week = now.weekday()
hour = now.hour
minute = now.minute
if day_of_week == 3 and hour == 1 and minute == 15:
    mail_sender.send("New quote", quote)





