import mysql.connector

dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'database'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE fauxco")

print("Database created!")