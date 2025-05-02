import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")


for x in mycursor:
    print(x)
    
# jika tidak ada error maka semua database berhasil ditampilkan