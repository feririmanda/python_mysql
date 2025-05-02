import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_mysql"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name,address FROM customers")

# myresult = mycursor.fetchone() // fetch one row only
myresult = mycursor.fetchall() #fetch all rows

for x in myresult:
    print(x)