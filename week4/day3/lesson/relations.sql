--ONE TO MANY

-- CREATE TABLE directors (
--   director_id SERIAL,
--   first_name VARCHAR(30) NOT NULL,
--   last_name VARCHAR(30) NOT NULL,
--   PRIMARY KEY (director_id)
-- );

-- INSERT INTO directors (first_name, last_name)
-- VALUES ('James', 'Cameron')

-- ALTER TABLE movies ADD COLUMN director_id INT;

-- ALTER TABLE movies ADD CONSTRAINT fk_director FOREIGN KEY (director_id) REFERENCES directors(director_id);

-- INSERT into movies(movie_title, movie_story, director_id) VALUES 
-- ('Good Will Hunting', 'lorem', (SELECT director_id FROM directors WHERE first_name = 'James')),
-- ('The Martian', 'lorem', (SELECT director_id FROM directors WHERE first_name = 'James') ),
-- ('Oceans Twelve', 'lorem', (SELECT director_id FROM directors WHERE first_name = 'James')),
-- ('Up in the Air', 'lorem', (SELECT director_id FROM directors WHERE first_name = 'James'));


-- SELECT * FROM movies

-- CREATE TABLE actors_movies (
--   actor_id INTEGER NOT NULL,
--   movie_id INTEGER NOT NULL,
--   actor_role VARCHAR(30) NOT NULL,
--   is_lead_role BOOLEAN NOT NULL,
--   PRIMARY KEY (actor_id, movie_id),
--   FOREIGN KEY (actor_id) REFERENCES actors(actor_id) ON UPDATE CASCADE,
--   FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON UPDATE CASCADE
-- );


-- INSERT into actors_movies(actor_id, movie_id, actor_role, is_lead_role) VALUES 
-- ((SELECT actor_id FROM actors where first_name = 'George' AND last_name = 'Clooney' LIMIT 1 ), 
-- (SELECT movie_id FROM movies where movie_title = 'Up in the Air' LIMIT 1), 'Ryan Bingham', TRUE),

-- ((SELECT actor_id FROM actors where first_name = 'George' AND last_name = 'Clooney' LIMIT 1 ), 
-- (SELECT movie_id FROM movies where movie_title = 'Oceans Twelve' LIMIT 1), 'Danny Ocean', FALSE),

-- ((SELECT actor_id FROM actors where first_name = 'Matt' AND last_name = 'Damon' LIMIT 1 ),
-- (SELECT movie_id FROM movies where movie_title = 'Good Will Hunting' LIMIT 1),'Will Hunting', TRUE);

SELECT * FROM actors_movies