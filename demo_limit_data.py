import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_mysql"
)

mycursor = mydb.cursor()

sql = "select * from customers limit 5"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)