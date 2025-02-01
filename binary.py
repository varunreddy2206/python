import mysql.connector

#establish connection to database

connection=mysql.connector.connect(
    host="localhost",
    user='root',
    password="root",
    database="practice"
)

#Test connection

# if connection.is_connected():
#     print("connection successful")

# else:
#     print("error connecting")

cursor=connection.cursor()

with open("var.jpg","rb") as file:
    bindata=file.read()


#insert sql query

tcs="insert into xyz(image) values(%s)"
cursor.execute(tcs,(bindata,))
connection.commit()

cursor.close()
connection.close()


