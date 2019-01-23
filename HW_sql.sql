use sakila;



/* 1a */
SELECT first_name, last_name FROM actor;


/* 1b */
SELECT CONCAT(first_name, ' ' , last_name) AS Actor_Name
	FROM actor;


/* 2a */
SELECT * from actor 
	WHERE first_name = 'Joe';


/* 2b */
SELECT * FROM actor 
	WHERE last_name  LIKE '%GEN%';


/* 2c */

SELECT * FROM actor
	WHERE last_name LIKE '%LI%' ORDER BY last_name, first_name;


/* 2d */

SELECT * FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');


/*3a*/

ALTER TABLE actor
ADD description blob;


/*3b*/

ALTER TABLE actor
DROP COLUMN description;


/*4a*/

SELECT first_name, last_name
FROM actor;



/*4b*/

SELECT
	last_name, COUNT(*)
FROM
    actor
GROUP BY
	last_name
HAVING 
    COUNT(*) > 1;



/*4c*/

UPDATE actor
SET first_name = 'Harpo'
WHERE first_name = 'Groucho';


/*4d*/

UPDATE actor
SET first_name = 'Groucho'
WHERE first_name = 'Harpo';

/* 5a */



/* 6a*/

SELECT staff.first_name, staff.last_name, address.address
FROM staff
RIGHT JOIN address ON staff.address_id=address.address_id;

/*6b */

SELECT staff.first_name, staff.last_name, staff.staff_id, payment.amount, payment.staff_id
FROM staff
RIGHT JOIN payment ON staff.staff_id=payment.staff_id;



select * from filmtitlef;

/* 6c*/

SELECT film.title, film.film_id, film_actor.actor_id, film_actor.film_id
FROM film
INNER JOIN film_actor ON film.film_id = film.film_id;


/*6d */

SELECT COUNT(title)
FROM film
WHERE title = 'Hunchback Impossible';

/* 6e*/
select * FROM customer;

SELECT * FROM payment
RIGHT JOIN customer on payment.customer_id = customer.customer_id;

/* 7a*/

SELECT title, language_id
FROM film 
WHERE title LIKE 'K%' OR 'Q%' AND Language_id = 1;


/*7b*/

SELECT first_name, last_name 
FROM actor 
WHERE actor_id IN
(
	SELECT actor_id 
    FROM film_actor
    WHERE film_id IN
    (
		SELECT film_id 
        FROM film 
        WHERE title = 'Alone Trip'
        )
	);
    
/*7c*/

SELECT first_name, last_name, email 
FROM customer
WHERE address_id IN
(
	SELECT address_id 
    FROM address
    WHERE city_id IN
    (
		SELECT city_id
        FROM city
        WHERE country_id IN
		(
			SELECT country_id
			FROM country
			WHERE country = 'Canada'
		)
	)
);


/*7d*/
select * FROM rental;

SELECT title 
FROM film
WHERE film_id in
(
	SELECT film_id 
    FROM film_category
    WHERE category_id IN
    (
		SELECT category_id
        FROM category
        WHERE name = 'Family'
	)
);
	


/*7e*/

SELECT title 
FROM film 
WHERE film_id IN
(
	SELECT film_id
    FROM inventory 
    WHERE inventory_id IN
	(
		SELECT inventory_id
        FROM rental
        ORDER BY rental_date DESC
	)
);
        






