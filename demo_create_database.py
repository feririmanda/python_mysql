import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE python_mysql")
print("Database created successfully")

# database akan terbuat di localhost
# jika tidak ada error maka database berhasil dibuat
