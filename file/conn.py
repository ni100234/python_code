import mysql.connector

#importing database
database = mysql.connector.connect(
host="localhost",
user="root",
password='',
database='student')
db = database.cursor()