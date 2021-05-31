import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "xxx@gmail.com"
mesaj["To"] = "yyy@gmail.com"
mesaj["Subject"] = "Subject"

yazi = """
Your Message 

"""

mesaj_govdesi = MIMEText(yazi, "plain")
mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("xxx@gmail.com", "password")
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()