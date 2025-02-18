/*
we we'll work with the Sakila Database 'sqlite-sakila.db' which is about dvd rental
*/


/*
Exercise 1 : DVD Rentals
Instructions
*/

-- -- 1. Get a list of all rentals which are out (have not been returned). 
-- -- How do we identify these films in the database?
-- SELECT
-- 	rental_id, rental_date, inventory_id, customer_id
-- FROM
-- 	rental
-- WHERE
-- 	return_date IS NULL;



-- -- 2. Get a list of all customers who have not returned their rentals. 
-- -- Make sure to group your results.
-- SELECT
-- 	c.customer_id,
-- 	C.first_name,
-- 	c.last_name,
-- 	COUNT(r.rental_id) AS outstanding_rentals
-- FROM
-- 	customer c
-- JOIN
-- 	rental r ON c.customer_id = r.customer_id
-- WHERE
-- 	return_date IS NULL
-- GROUP BY
-- 	c.customer_id
-- ORDER BY
-- 	outstanding_rentals DESC;



-- -- Get a list of all the Action films with Joe Swank.
-- -- Before you start, could there be a shortcut to getting 
-- -- this information? Maybe a view?
-- SELECT f.title
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- JOIN film_category fc ON f.film_id = fc.film_id
-- JOIN category c ON fc.category_id = c.category_id
-- WHERE
-- 	a.first_name = 'Joe' AND a.last_name = 'Swank'
-- 	AND c.name = 'Action';

-- -- another way is making a VIEW:
-- CREATE VIEW film_actor_category_view AS
-- SELECT
-- 	f.film_id,
-- 	f.title,
-- 	a.first_name,
-- 	a.last_name,
-- 	c.name AS category_name
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- JOIN film_category fc ON f.film_id = fc.film_id
-- JOIN category c ON fc.category_id = c.category_id;

-- SELECT
-- 	title
-- FROM
-- 	film_actor_category_view
-- WHERE
-- 	first_name = 'Joe' AND last_name = 'Swank' AND category_name = 'Action';


-- #########################################################################
-- Exercise 2 – Happy Halloween

-- -- 1. How many stores there are, and in which city and country they are located.
-- SELECT
-- 	COUNT(DISTINCT s.store_id) AS total_stores,
-- 	c.city,
-- 	co.country
-- FROM
-- 	store s
-- JOIN
-- 	address a ON s.address_id = a.address_id
-- JOIN
-- 	city c ON a.city_id = c.city_id
-- JOIN
-- 	country co ON c.country_id = co.country_id
-- GROUP BY
-- 	c.city, co.country;



-- -- 2. How many hours of viewing time there are in total in each store – in 
-- -- other words, the sum of the length of every inventory item in each store.
-- SELECT
-- 	s.store_id,
-- 	SUM(f.length) / 60. AS total_viewing_hours
-- FROM store s
-- JOIN inventory i ON s.store_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- GROUP BY s.store_id
-- ORDER BY s.store_id;



-- -- 3. Make sure to exclude any inventory items which are not yet returned.
-- SELECT
-- 	s.store_id,
-- 	SUM(f.length) / 60. AS total_viewing_hours
-- FROM store s
-- JOIN inventory i ON s.store_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- LEFT JOIN rental r ON i.inventory_id = r.inventory_id
-- WHERE r.return_date IS NOT NULL
-- GROUP BY s.store_id
-- ORDER BY s.store_id;



-- -- 4. A list of all customers in the cities where the stores are located.
-- WITH StoreCities AS (
--     SELECT DISTINCT c.city_id
--     FROM store s
--     JOIN address a ON s.address_id = a.address_id
--     JOIN city c ON a.city_id = c.city_id
-- )
-- SELECT cu.customer_id, cu.first_name, cu.last_name, ci.city
-- FROM customer cu
-- JOIN address ad ON cu.address_id = ad.address_id
-- JOIN city ci ON ad.city_id = ci.city_id
-- JOIN StoreCities sc ON ci.city_id = sc.city_id
-- ORDER BY cu.customer_id;



-- -- 5. A list of all customers in the countries where the stores are located.
-- WITH StoreCountries AS (
-- 	SELECT DISTINCT co.country_id
-- 	FROM store s
-- 	JOIN address a ON s.address_id = a.address_id
-- 	JOIN city ci ON a.city_id = ci.city_id
-- 	JOIN country co ON ci.country_id = co.country_id
-- )
-- SELECT c.customer_id, c.first_name, c.last_name, co.country
-- FROM customer c
-- JOIN address a ON c.address_id = a.address_id
-- JOIN city ci ON a.city_id = ci.city_id
-- JOIN country co ON ci.country_id = co.country_id
-- JOIN StoreCountries sc ON co.country_id = sc.country_id
-- ORDER BY c.customer_id;




-- -- 6. Create a ‘safe list’ of all movies which do not include the ‘Horror’ 
-- -- category, or contain the words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, 
-- -- ‘zombie’, or ‘undead’ in their titles or descriptions… Get the sum 
-- -- of their viewing time (length).
-- -- Hint : use the CHECK contraint
-- WITH SafeMovies AS (
--     SELECT f.film_id, f.title, f.description, f.length
--     FROM film f
--     LEFT JOIN film_category fc ON f.film_id = fc.film_id
--     LEFT JOIN category c ON fc.category_id = c.category_id
--     WHERE (c.name IS NULL OR c.name <> 'Horror')  -- Exclude Horror category
--     AND LOWER(f.title) NOT LIKE '%beast%'
--     AND LOWER(f.title) NOT LIKE '%monster%'
--     AND LOWER(f.title) NOT LIKE '%ghost%'
--     AND LOWER(f.title) NOT LIKE '%dead%'
--     AND LOWER(f.title) NOT LIKE '%zombie%'
--     AND LOWER(f.title) NOT LIKE '%undead%'
--     AND LOWER(f.description) NOT LIKE '%beast%'
--     AND LOWER(f.description) NOT LIKE '%monster%'
--     AND LOWER(f.description) NOT LIKE '%ghost%'
--     AND LOWER(f.description) NOT LIKE '%dead%'
--     AND LOWER(f.description) NOT LIKE '%zombie%'
--     AND LOWER(f.description) NOT LIKE '%undead%'
-- )
-- -- SELECT * FROM SafeMovies;
-- SELECT SUM(length) AS total_safe_viewing_time FROM SafeMovies;



-- -- 7. For both the ‘general’ and the ‘safe’ lists above, also calculate the time 
-- -- in hours and days (not just minutes).
-- WITH SafeMovies AS (
--     SELECT f.film_id, f.title, f.description, f.length
--     FROM film f
--     LEFT JOIN film_category fc ON f.film_id = fc.film_id
--     LEFT JOIN category c ON fc.category_id = c.category_id
--     WHERE (c.name IS NULL OR c.name <> 'Horror')  -- Exclude Horror category
--     AND LOWER(f.title) NOT LIKE '%beast%'
--     AND LOWER(f.title) NOT LIKE '%monster%'
--     AND LOWER(f.title) NOT LIKE '%ghost%'
--     AND LOWER(f.title) NOT LIKE '%dead%'
--     AND LOWER(f.title) NOT LIKE '%zombie%'
--     AND LOWER(f.title) NOT LIKE '%undead%'
--     AND LOWER(f.description) NOT LIKE '%beast%'
--     AND LOWER(f.description) NOT LIKE '%monster%'
--     AND LOWER(f.description) NOT LIKE '%ghost%'
--     AND LOWER(f.description) NOT LIKE '%dead%'
--     AND LOWER(f.description) NOT LIKE '%zombie%'
--     AND LOWER(f.description) NOT LIKE '%undead%'
-- ),
-- GeneralTotal AS (
--     SELECT SUM(length) AS total_minutes FROM film
-- ),
-- SafeTotal AS (
--     SELECT SUM(length) AS total_minutes FROM SafeMovies
-- )
-- SELECT 
--     'General List' AS list_type, 
--     total_minutes AS total_minutes,
--     ROUND(total_minutes / 60.0, 2) AS total_hours,
--     ROUND(total_minutes / 1440.0, 2) AS total_days
-- FROM GeneralTotal
-- UNION ALL
-- SELECT 
--     'Safe List' AS list_type, 
--     total_minutes AS total_minutes,
--     ROUND(total_minutes / 60.0, 2) AS total_hours,
--     ROUND(total_minutes / 1440.0, 2) AS total_days
-- FROM SafeTotal;