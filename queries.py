question_queries = {
    1: """SELECT
    f.title AS 'Film Title',
    COUNT(*) AS 'Inventory Count'
FROM
    store AS s
JOIN inventory AS i ON 
	i.store_id = s.store_id
JOIN film AS f ON 
	i.film_id = f.film_id
GROUP BY
    s.store_id,
    f.film_id;""",


    2: """SELECT
	s.store_id AS 'Store Id',
    a.address AS 'Store Location',
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
ORDER BY
	s.store_id,
	f.film_id;""",


    3: """SELECT
	s.store_id AS 'Store Id',
    a.address AS 'Store Address',
    a.phone AS 'Store Contact',
    f.title AS 'Film Title',
    COUNT(r.rental_id) AS 'Rent Count'
FROM
	store AS s
JOIN address as a ON
	a.address_id = s.address_id
JOIN inventory AS i ON
	s.store_id = i.store_id
JOIN rental AS r ON
	r.inventory_id = i.inventory_id
JOIN film AS f ON
	f.film_id = i.film_id
GROUP BY
	s.store_id,
    f.film_id
HAVING
	COUNT(r.rental_id) > 5
ORDER BY
	COUNT(r.rental_id);""",


    4: """SELECT
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
	) AS store_2;""",
    

    5: """SELECT
	c.country AS 'Country', 
    a.address AS 'Store Location',
    a.phone AS 'Store Contact',
    COUNT(i.inventory_id) AS 'Inventory Count'
FROM
	country AS c
JOIN city ON
	c.country_id = city.country_id
JOIN address AS a ON
	a.city_id = city.city_id
JOIN store AS s ON
	s.address_id = a.address_id
JOIN inventory AS i ON
	i.store_id = s.store_id
GROUP BY
	c.country,
	a.address,
    a.phone;
""",


    6: """SELECT
	*
FROM
	(
		SELECT
			c.country AS 'Country',
			f.title AS 'Film Title',
			COUNT(r.rental_id) AS 'Rent Count'
		FROM
			country AS c
		JOIN city ON
			c.country_id = city.country_id
		JOIN address AS a ON
			a.city_id = city.city_id
		JOIN store AS s ON
			s.address_id = a.address_id
		JOIN inventory AS i ON
			i.store_id = s.store_id
		JOIN film AS f ON
			f.film_id = i.film_id
		JOIN rental AS r ON
			r.inventory_id = i.inventory_id
		GROUP BY
			c.country_id,
			c.country,
			f.film_id,
			s.store_id
		HAVING
			store_id = 1
		ORDER BY
			'Rent Count' DESC
		LIMIT
			1
) AS store_1
UNION
SELECT
	*
FROM
	(
		SELECT
			c.country AS 'Country',
			f.title AS 'Film Title',
			COUNT(r.rental_id) AS 'Rent Count'
		FROM country AS c 
        JOIN city ON
			c.country_id = city.country_id
		JOIN address AS a ON
			a.city_id = city.city_id
		JOIN store AS s ON
			s.address_id = a.address_id
		JOIN inventory AS i ON
			i.store_id = s.store_id
		JOIN film AS f ON
			f.film_id = i.film_id
		JOIN rental AS r ON
			r.inventory_id = i.inventory_id
		GROUP BY
			c.country_id,
			c.country,
			f.film_id,
			s.store_id
		HAVING
			store_id = 2
		ORDER BY
			'Rent Count' DESC
		LIMIT
			1
) AS store_2
ORDER BY
	country;""",
}
