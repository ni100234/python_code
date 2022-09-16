sn=int(input("enter the serial number= "))
name=input("enter the name= ")
grade=int(input("enter the class= "))
physic=int(input("enter the score of physic= "))
math=int(input("enter the score of math= "))
nepali=int(input("enter the score of nepali= "))
english=int(input("enter the score of english= "))
total=int(input("enter the total score= "))
percentage=int(input("enter the percentage= "))
import mysql.connector

#importing database
database = mysql.connector.connect(
host="localhost",
user="root",
password='',
database='student')
db = database.cursor()

sql=f"INSERT INTO detail  VALUES ('{sn}','{name}','{grade}','{physic}','{math}','{nepali}','{english}','{total}', '{percentage}')"
db.execute(sql)
db.execute("SELECT * FROM detail")
result =db.fetchall()
for i in result:
    print(i)

