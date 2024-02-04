import mysql.connector
from queries import question_queries

DB_NAME = "sakila"
PASSWORD = "password"

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = PASSWORD,
  database = DB_NAME
)
cursor = mydb.cursor()

def execute_query(question_id):
    query = question_queries.get(question_id)
    if query:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            return result, columns
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None, None
    else:
        print("Error: Question ID not found in the dictionary")
        return None, None


