-- -- ----------------------------  Exercice 1: DVD Rental  -------------------------
-- -- Get a list of all the languages, from the language table.
-- SELECT * FROM language;


-- -- Get a list of all films joined with their languages – select the following details:
-- -- film title, description, and language name.
-- SELECT
-- 	f.title AS movie_title,
-- 	f.description AS movie_descript,
-- 	l.name AS language_name
-- FROM
-- 	film f
-- LEFT JOIN
-- 	language l ON f.language_id = l.language_id
-- ORDER BY
-- 	f.title;


-- -- Get all languages, even if there are no films in those languages –
-- -- select the following details : film title, description, and language name.
-- SELECT
-- 	f.title AS movie_title,
-- 	f.description AS movie_descript,
-- 	l.name AS language_name
-- FROM
-- 	film f
-- RIGHT JOIN -- the same as before but with right join
-- 	language l ON f.language_id = l.language_id
-- ORDER BY
-- 	f.title;


-- -- Create a new table called new_film with the 
-- -- following columns : id, name. Add some new films to the table.
-- CREATE TABLE new_film (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO new_film (name) VALUES
-- 	('name 1'),
-- 	('name 2'),
-- 	('name 3'),
-- 	('name 4'),
-- 	('name 5'),
-- 	('name 6'),
-- 	('name 7'),
-- 	('name 8');


-- -- Create a new table called customer_review, which will contain film reviews that customers 
-- -- will make.
-- -- Think about the DELETE constraint: if a film is deleted, its review should be automatically
-- -- deleted.
-- -- It should have the following columns:

-- --     review_id – a primary key, non null, auto-increment.
-- --     film_id – references the new_film table. The film that is being reviewed.
-- --     language_id – references the language table. What language the review is in.
-- --     title – the title of the review.
-- --     score – the rating of the review (1-10).
-- --     review_text – the text of the review. No limit on the length.
-- --     last_update – when the review was last updated.
-- CREATE TABLE customer_review (
-- 	review_id SERIAL PRIMARY KEY,
-- 	film_id INTEGER NOT NULL,
-- 	language_id INTEGER NOT NULL,
-- 	title VARCHAR(255),
-- 	score INTEGER CHECK (score >= 1 AND score <= 10),
-- 	review_text TEXT,
-- 	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
-- 	FOREIGN KEY (language_id) REFERENCES language(language_id)
-- );


-- -- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES
-- 	(1, 3, 'some invented title 1', 10, 'absolute cinema'),
-- 	(2, 1, 'some invented title 2', 8, 'some invented review 2');
-- SELECT * FROM customer_review;

-- -- Delete a film that has a review from the new_film table, 
-- -- what happens to the customer_review table?
-- SELECT * FROM new_film;
-- DELETE FROM new_film WHERE id = 1;
-- SELECT * FROM new_film;
-- SELECT * FROM customer_review; -- we removed that movie also from customer_review table




-- -- ----------------------------  Exercice 2: DVD Rental  -------------------------
-- -- Use UPDATE to change the language of some films. Make sure that you use valid languages.
-- SELECT * FROM language; -- the list goes from 1 to 6
-- SELECT * FROM film;
-- UPDATE film
-- SET language_id = 5 -- stablish new language
-- WHERE film_id IN (1, 2, 3); -- the films to change the language

-- SELECT f.film_id, f.title, f.language_id
-- FROM film f
-- WHERE film_id IN (1, 2, 3); -- language changed to 5


-- -- Which foreign keys (references) are defined for the customer table? 
-- -- How does this affect the way in which we INSERT into the customer table?
-- SELECT
--     tc.table_schema, 
--     tc.constraint_name, 
--     tc.table_name, 
--     kcu.column_name, 
--     ccu.table_schema AS foreign_table_schema,
--     ccu.table_name AS foreign_table_name,
--     ccu.column_name AS foreign_column_name 
-- FROM 
--     information_schema.table_constraints AS tc 
--     JOIN information_schema.key_column_usage AS kcu
--       ON tc.constraint_name = kcu.constraint_name
--       AND tc.table_schema = kcu.table_schema
--     JOIN information_schema.constraint_column_usage AS ccu
--       ON ccu.constraint_name = tc.constraint_name
--       AND ccu.table_schema = tc.table_schema
-- WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name='customer';
-- -- There is a FOREIGN KEY in 'customer' table for 'address_id' field, the foreign table is 'address'
-- -- and its field is 'address_id'
-- -- If we try to insert a non existent value, the insertion will fail



-- -- We created a new table called customer_review. 
-- -- Drop this table. Is this an easy step, or does it need extra checking?
-- DROP TABLE customer_review -- dropped without problem, we didnt bluild something deending on this table


-- -- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- SELECT COUNT(*)
-- FROM rental
-- WHERE return_date IS NULL; -- 183 not returned movies


-- -- Find the 30 most expensive movies which are outstanding
-- -- (ie. have not been returned to the store yet) (ಠ_ಠ)
-- SELECT DISTINCT -- shouldt repeat same film
-- 	f.film_id,
-- 	f.title AS film_title,
-- 	r.return_date, -- to verify visually hasnt been returned
-- 	p.amount AS rental_amount
-- FROM
-- 	rental r
-- JOIN
-- 	inventory i ON r.inventory_id = i.inventory_id
-- JOIN 
--     film f ON i.film_id = f.film_id
-- JOIN 
--     payment p ON r.rental_id = p.rental_id
-- WHERE
-- 	r.return_date IS NULL
-- ORDER BY
-- 	p.amount DESC
-- LIMIT 30;


-- -- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, 
-- -- but he can’t remember their names. Can you help him find which movies he wants to rent?

-- 	-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- SELECT
-- 	title,
-- 	description
-- FROM
-- 	film f
-- JOIN
-- 	film_actor fa ON f.film_id = fa.film_id
-- JOIN
-- 	actor a ON fa.actor_id = a.actor_id
-- WHERE
-- 	description ILIKE '%sumo wrestler%'
-- 	AND (a.first_name = 'Penelope' AND a.last_name = 'Monroe');


-- 	-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
-- SELECT
-- 	title,
-- 	special_features,
-- 	length,
-- 	rating
-- FROM
-- 	film
-- WHERE
-- 	'Documentary' = ANY(special_features) -- check if 'Documentary' is in the array
-- 	AND length <= 60
-- 	AND rating = 'R';


	-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental,
	-- and he returned it between the 28th of July and the 1st of August, 2005.
-- SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan';

-- SELECT
-- 	r.rental_id,
-- 	r.inventory_id,
-- 	r.rental_date,
-- 	r.return_date,
-- 	p.amount
-- FROM
-- 	rental r
-- JOIN
-- 	payment p ON r.rental_id = p.rental_id
-- WHERE
-- 	r.customer_id = (SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan')
-- 	AND p.amount > 4.
-- 	AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

	
-- 	-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” 
-- 	-- in the title or description, and it looked like it was a very expensive DVD to replace.
-- -- SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan';
-- -- SELECT film_id, title, description FROM film WHERE description ILIKE('%boat%');

-- SELECT
-- 	f.title,
-- 	f.description,
-- 	f.replacement_cost -- this one
-- FROM
-- 	film f
-- JOIN
-- 	inventory i ON f.film_id = i.film_id
-- JOIN
-- 	rental r ON r.inventory_id = i.inventory_id
-- JOIN
-- 	customer c ON c.customer_id = r.customer_id
-- WHERE
-- 	c.first_name = 'Matthew' AND c.last_name = 'Mahan'
-- AND
-- 	(f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
-- ORDER BY
-- 	f.replacement_cost DESC;