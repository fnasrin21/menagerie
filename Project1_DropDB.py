import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mithy101!"
)

mycursor = mydb.cursor()

sql = "DROP DATABASE IF EXISTS menagerie"

mycursor.execute(sql)
