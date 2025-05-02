import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_mysql"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
address = ("One way 98",)
mycursor.execute(sql, address)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")