from datetime import datetime
from email.mime.text import MIMEText
import mysql.connector
from celery import password, email_pass
from smtplib import SMTP
from email_template import birthday_template
from email.mime.multipart import MIMEMultipart

mydb = mysql.connector.connect(
    host="localhost", user="root", password=password, database="user_details"
)

cursor = mydb.cursor()

month = str(datetime.now().month)
day = str(datetime.now().day)
sql = "SELECT * from user_details where DATE_FORMAT(dob,'%m-%d') = DATE_FORMAT(NOW(),'%m-%d')"

cursor.execute(sql)

result = cursor.fetchall()

s = SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("sudhan13270@gmail.com", email_pass)
for x in result:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Happy Birthday {0}".format(x[1])
    template = birthday_template(x[1])
    html = MIMEText(template, "html")
    msg.attach(html)
    s.sendmail(
        "sudhan13270@gmail.com",
        x[2],
        msg.as_string(),
    )
    print(x)
s.quit()
