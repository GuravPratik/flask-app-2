import mysql.connector

DB_NAME = "sakila"
PASSWORD = "your password"

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = PASSWORD,
  database = DB_NAME
)

cursor = mydb.cursor()

query = """SELECT * FROM store"""

cursor.execute(query)

result = cursor.fetchone()
columns = [column[0] for column in cursor.description]
print(columns)
print(result)