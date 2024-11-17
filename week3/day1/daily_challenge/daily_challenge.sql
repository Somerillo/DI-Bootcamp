-- here i create agauin an actors table
-- CREATE TABLE actors (
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(50) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL
-- );

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('matt', 'damon', '1970-10-08', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('george', 'cluni', '1961-05-06', 2);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('cameron', 'dias', '1975-05-06', 20),
-- ('charlize', 'theron', '1980-05-06', 4),
-- ('lana', 'del rey', '2000-05-06', 2);




SELECT COUNT (*) FROM actors; --Count how many actors are in the table.

INSERT INTO actors (first_name, last_name, age, number_oscars) --add a new actor with some blank fields.
VALUES ('empty', '', '1970-10-08', );
-- Cant add empty fields because they were defined as 'NOT NULL'
