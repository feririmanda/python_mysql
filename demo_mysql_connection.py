import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)

# This is a test script to demonstrate how to connect to a MySQL database using Python.
# jika tidak ada error maka koneksi berhasil