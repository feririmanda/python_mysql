import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_mysql"
)

mycusor = mydb.cursor()
mycusor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("Tobi", "Bekasi"))
mydb.commit()
print(mycusor.rowcount, "record inserted.")

#insert multiple records
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('John', 'Highway 21'),
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),    
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633'),
]

mycusor.executemany(sql, val)
mydb.commit()
print(mycusor.rowcount, "was inserted.")