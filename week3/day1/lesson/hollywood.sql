-- -- this is a comment
-- CREATE TABLE actors (
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(50) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL
-- )

-- SELECT * FROM actors;

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('matt', 'damon', '1970-10-08', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('george', 'cluni', '1961-05-06', 2);

-- SELECT * FROM actors;

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('cameron', 'dias', '1975-05-06', 2),
-- ('charlize', 'theron', '1980-05-06', 2),
-- ('lana', 'del rey', '2000-05-06', 2);

-- SELECT * FROM actors;

-- SELECT first_name FROM actors WHERE first_name = 'matt';

-- SELECT * FROM actors WHERE first_name = 'matt';

-- SELECT * FROM actors WHERE number_oscars > 3;

-- SELECT * FROM actors WHERE first_name ILIKE '%orge';

-- SELECT * FROM actors WHERE number_oscars < 3 OFFSET 2;

-- SELECT * FROM actors ORDER BY number_oscars;

-- UPDATE actors
-- SET first_name = 'Angelina',
-- last_name = 'Jolie'
-- WHERE first_name = 'lana';
-- SELECT * FROM actors;

-- DELETE FROM actors
-- WHERE first_name = 'Angelina';
-- SELECT * FROM actors;


