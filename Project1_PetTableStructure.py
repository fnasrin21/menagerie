import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mithy101!",
    database="menagerie"
)

mycursor = mydb.cursor()

mycursor.execute("DESCRIBE pet")

for row in mycursor.fetchall():
    print(row)
