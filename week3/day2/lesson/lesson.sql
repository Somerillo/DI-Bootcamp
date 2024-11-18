-- ALTER TABLE actors 
-- ADD COLUMN movie VARCHAR(50);

-- Select * From actors;

-- UPDATE actors
-- SET movie = CASE
--     WHEN actor_id = 1 THEN 'Good Will Hunting'
--     WHEN actor_id = 2 THEN 'Ocean''s Eleven'
--     WHEN actor_id = 3 THEN 'There''s Something About Mary'
--     WHEN actor_id = 4 THEN 'Mad Max: Fury Road'
--     WHEN actor_id = 6 THEN 'Movie 1'
--     WHEN actor_id = 7 THEN 'Movie 2'
--     WHEN actor_id = 8 THEN 'Movie 3'
-- END
-- WHERE actor_id IN (1, 2, 3, 4, 6, 7, 8);

-- Select * From actors;

-- CREATE TABLE countries (
--     country_id INT PRIMARY KEY,
--     country_name VARCHAR(100)
-- );

-- INSERT INTO countries (country_id, country_name) VALUES
-- (1, 'Estados Unidos'),
-- (2, 'Reino Unido'),
-- (3, 'Francia'),
-- (4, 'Australia'),
-- (5, 'Canadá');

-- SELECT a.actor_id, a.first_name, a.last_name, c.country_name
-- FROM actors a
-- INNER JOIN countries c ON a.actor_id = c.country_id;

-- SELECT a.actor_id, a.first_name, a.last_name, c.country_name
-- FROM actors a
-- LEFT OUTER JOIN countries c ON a.actor_id = c.country_id;

-- SELECT a.actor_id, a.first_name, a.last_name, c.country_name
-- FROM actors a
-- RIGHT OUTER JOIN countries c ON a.actor_id = c.country_id;

SELECT a.actor_id, a.first_name, a.last_name, c.country_name
FROM actors a
FULL OUTER JOIN countries c ON a.actor_id = c.country_id;
