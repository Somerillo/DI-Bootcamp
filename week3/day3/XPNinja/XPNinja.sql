-- -- 1. Retrieve all films with a rating of G or PG, which are are not 
-- -- currently rented (they have been returned/have never been borrowed).
-- SELECT DISTINCT f.film_id, f.title, f.rating
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- LEFT JOIN rental r ON i.inventory_id = r.inventory_id
-- WHERE
-- 	f.rating IN ('G', 'PG')
-- 	AND (r.return_date IS NOT NULL OR r.rental_id IS NULL)
-- ORDER BY f.title;



-- -- 2. Create a new table which will represent a waiting list for children’s 
-- -- movies. This will allow a child to add their name to the list until the 
-- -- DVD is available (has been returned). Once the child takes the DVD, their 
-- -- name should be removed from the waiting list (ideally using triggers, but 
-- -- we have not learned about them yet. Let’s assume that our Python program 
-- -- will manage this). Which table references should be included?
-- DROP TABLE IF EXISTS children_movie_waitlist;

-- CREATE TABLE children_movie_waitlist (
-- 	waitlist_id SERIAL PRIMARY KEY,
-- 	film_id INTEGER NOT NULL,
-- 	customer_id INTEGER NOT NULL,
-- 	date_added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
-- 	FOREIGN KEY (film_id) REFERENCES film(film_id),
-- 	FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
-- );



-- -- 3. Retrieve the number of people waiting for each children’s DVD. Test this
-- -- by adding rows to the table that you created in question 2 above.
-- SELECT f.title, f.rating, COUNT(w.waitlist_id) AS waiting_count
-- FROM film f
-- LEFT JOIN children_movie_waitlist w ON f.film_id = w.film_id
-- WHERE f.rating IN ('G', 'PG')
-- GROUP BY f.film_id, f.title, f.rating
-- ORDER BY waiting_count DESC, f.title;

-- INSERT INTO children_movie_waitlist (film_id, customer_id) VALUES
-- (1, 5), (1, 10), (1, 15),  -- 3 people waiting for film_id 1
-- (2, 7), (2, 12),           -- 2 people waiting for film_id 2
-- (3, 20),                   -- 1 person waiting for film_id 3
-- (4, 8), (4, 9), (4, 11), (4, 13);  -- 4 people waiting for film_id 4