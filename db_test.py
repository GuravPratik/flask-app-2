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

query = """SELECT
	*
FROM
	(
		SELECT
			s.store_id AS 'Store Id',
            a.address AS 'Store Address',
            a.phone AS 'Store Contact',
			f.title AS 'Film Title',
			COUNT(r.rental_id) AS 'Rent Count'
		FROM
			store AS s
		JOIN address AS a ON
			a.address_id = s.address_id
		JOIN inventory AS i ON
			i.store_id = s.store_id
		JOIN rental AS r ON
			r.inventory_id = i.inventory_id
		JOIN film AS f ON
			i.film_id = f.film_id
		GROUP BY
			s.store_id,
			f.film_id
		HAVING
			s.store_id = 1
		ORDER BY
			COUNT(r.rental_id) DESC
		LIMIT 5
	) AS store_1
UNION 
SELECT
	*
FROM
	(
		SELECT
			s.store_id AS 'Store Id',
            a.address AS 'Store Address',
            a.phone AS 'Store Contact',
			f.title AS 'Film Title',
			COUNT(r.rental_id) AS 'Rent Count'
		FROM
			store AS s
		JOIN address AS a ON
			a.address_id = s.address_id
		JOIN inventory AS i ON
			i.store_id = s.store_id
		JOIN rental AS r ON
			r.inventory_id = i.inventory_id
		JOIN film AS f ON
			i.film_id = f.film_id
		GROUP BY
			s.store_id,
			f.film_id
		HAVING
			s.store_id = 2
		ORDER BY
			COUNT(r.rental_id) DESC
		LIMIT 5
	) AS store_2;"""

cursor.execute(query)

result = cursor.fetchone()
columns = [column[0] for column in cursor.description]
print(columns)
print(result)