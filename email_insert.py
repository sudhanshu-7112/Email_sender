from datetime import datetime
import mysql.connector
from celery import password

mydb = mysql.connector.connect(
    host="localhost", user="root", password=password, database="user_details"
)

cursor = mydb.cursor()

sql = "INSERT INTO user_details(name, email, dob) VALUES(%s,%s,%s)"

name = input("Enter Name:")
email = input("Enter Email:")
dob = input("Enter DOB:")
dob = datetime.strptime(dob, "%d/%m/%Y")
dob = dob.strftime("%Y-%m-%d")

val = (name, email, dob)

cursor.execute(sql, val)

mydb.commit()
