import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",    
    database="python_mysql"
)

mycursor = mydb.cursor()
#sql = "SELECT name,address FROM customers WHERE address LIKE '%ll%'" # pakai like untuk mencari data yang mirip
#sql = "SELECT name,address FROM customers WHERE address = 'Bekasi'" # pakai = untuk mencari data yang sama persis
sql = "SELECT * FROM customers WHERE address = %s" # pakai %s untuk parameter yang akan diisi oleh user
address = ("One way 98",)
mycursor.execute(sql, address)
myresult = mycursor.fetchall() #fetch all rows

for x in myresult:
    print(x)