import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_mysql"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers ORDER BY name DESC")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    