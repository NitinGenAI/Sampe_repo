import mysql.connector

mydb = mysql.connector.connect(
   host = "localhost",
    user = "root",
    password = "welcome",
    database = "Nitin_Python"
)
my_cursor = mydb.cursor()
# query = "CREATE DATABASE Nitin_Python"
# my_cursor.execute(query)

# query = "CREATE TABLE Employee (name VARCHAR(255), email VARCHAR(255), salary INTEGER(255)," \
#         "emp_code INTEGER(255))"
# my_cursor.execute(query)
query = "INSERT INTO Employee (name,email,salary,emp_code) VALUES (%s, %s, %s, %s)"
records = [('nitin', 'nitin@gmail.com', 50, 111),
           ('sharma','sharma@gmail.com', 60, 222),
           ('nitin1', 'nitin1@gmail.com', 70, 333),
           ]
my_cursor.executemany(query,records)
mydb.commit()
