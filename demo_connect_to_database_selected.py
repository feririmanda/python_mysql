import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_mysql"
)

mycursor = mydb.cursor()

# jika tidak ada  error maka koneksi berhasil
print("Koneksi berhasil ke database python_mysql")