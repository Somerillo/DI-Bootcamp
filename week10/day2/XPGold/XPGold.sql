-- -- First we review the tables in the schema
-- SELECT table_name 
-- FROM information_schema.tables 
-- WHERE table_schema = 'movies' 
-- AND table_type = 'BASE TABLE';

/*
Exercise 1: Comprehensive Movie Revenue and Rating Analysis


SQL Dataset we will be using

Movies Database


Task 1: Use the LEAD() and LAG() functions to identify movies where the budget increased compared to the previous movie but decreased compared to the next movie, in order of their release dates. Display the movie title, release date, and budget, along with the previous and next budgets.
Task 2: Create a CTE to calculate the moving average rating of movies over a 5-year window for each genre. Display the genre, movie title, release year, and the moving average rating.
Task 3: Use the ROW_NUMBER(), RANK(), and DENSE_RANK() functions to create a comprehensive ranking system for movies based on revenue within each genre. Display the genre, movie title, revenue, and their respective row number, rank, and dense rank.
*/

-- WITH BudgetComparison AS (
--     SELECT 
--         title,
--         release_date,
--         budget,
--         LAG(budget) OVER (ORDER BY release_date) AS previous_budget,
--         LEAD(budget) OVER (ORDER BY release_date) AS next_budget
--     FROM 
--         movies.movie
-- )
-- SELECT 
--     title,
--     release_date,
--     budget,
--     previous_budget,
--     next_budget
-- FROM 
--     BudgetComparison
-- WHERE 
--     budget > previous_budget
--     AND budget > next_budget
-- ORDER BY 
--     release_date;


-- -- Task 2: Create a CTE to calculate the moving average rating
-- -- of movies over a 5-year window for each genre. Display the 
-- -- genre, movie title, release year, and the moving average rating.
-- WITH movie_ratings AS (
--     SELECT 
--         mg.genre_id,
--         g.genre_name AS genre_name,
--         m.title,
--         EXTRACT(YEAR FROM m.release_date) AS release_year,
--         m.vote_average AS rating
--     FROM 
--         movies.movie m
--     JOIN 
--         movies.movie_genres mg ON m.movie_id = mg.movie_id
--     JOIN 
--         movies.genre g ON mg.genre_id = g.genre_id
--     WHERE 
--         m.vote_average IS NOT NULL
--         AND m.release_date IS NOT NULL
-- ),
-- moving_averages AS (
--     SELECT 
--         genre_name,
--         title,
--         release_year,
--         rating,
--         AVG(rating) OVER (
--             PARTITION BY genre_name
--             ORDER BY release_year
--             RANGE BETWEEN 2 PRECEDING AND 2 FOLLOWING
--         ) AS moving_avg_rating
--     FROM 
--         movie_ratings
-- )
-- SELECT 
--     genre_name,
--     title,
--     release_year,
--     ROUND(moving_avg_rating, 2) AS moving_avg_rating
-- FROM 
--     moving_averages
-- ORDER BY 
--     genre_name,
--     release_year,
--     title;


-- -- Task 3: Use the ROW_NUMBER(), RANK(), and DENSE_RANK() functions to 
-- -- create a comprehensive ranking system for movies based on revenue 
-- -- within each genre. Display the genre, movie title, revenue, and their
-- -- respective row number, rank, and dense rank.
-- WITH movie_rankings AS (
--     SELECT 
--         g.genre_name AS genre,
--         m.title,
--         m.revenue,
--         ROW_NUMBER() OVER (PARTITION BY g.genre_id ORDER BY m.revenue DESC) AS row_num,
--         RANK() OVER (PARTITION BY g.genre_id ORDER BY m.revenue DESC) AS rank,
--         DENSE_RANK() OVER (PARTITION BY g.genre_id ORDER BY m.revenue DESC) AS dense_rank
--     FROM 
--         movies.movie m
--     JOIN 
--         movies.movie_genres mg ON m.movie_id = mg.movie_id
--     JOIN 
--         movies.genre g ON mg.genre_id = g.genre_id
--     WHERE 
--         m.revenue IS NOT NULL
-- )
-- SELECT 
--     genre,
--     title,
--     revenue,
--     row_num,
--     rank,
--     dense_rank
-- FROM 
--     movie_rankings
-- ORDER BY 
--     genre, 
--     revenue DESC;



-- #####################################################################################
/*
Exercise 2: In-Depth Actor and Genre Analysis

Task 1: Use the FIRST_VALUE() and LAST_VALUE() functions to find the first and last movie each actor appeared in. Display the actor’s name, first movie title, first movie release date, last movie title, and last movie release date.
Task 2: Create a nested subquery to identify genres where the average movie revenue is above the overall average movie revenue. Within those genres, use a window function to rank movies by their popularity. Display the genre, movie title, revenue, and rank.
Task 3: Use a combination of window functions and CTEs to find actors who have appeared in movies that have collectively grossed in the top 10% of all movie revenues. Display the actor’s name and the total revenue of the movies they have appeared in.
*/
-- WITH actor_movies AS (
--     SELECT 
--         p.person_id,
--         p.person_name AS actor_name,
--         m.title,
--         m.release_date,
--         FIRST_VALUE(m.title) OVER (
--             PARTITION BY p.person_id 
--             ORDER BY m.release_date
--             ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
--         ) AS first_movie,
--         FIRST_VALUE(m.release_date) OVER (
--             PARTITION BY p.person_id 
--             ORDER BY m.release_date
--             ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
--         ) AS first_movie_date,
--         LAST_VALUE(m.title) OVER (
--             PARTITION BY p.person_id 
--             ORDER BY m.release_date
--             ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
--         ) AS last_movie,
--         LAST_VALUE(m.release_date) OVER (
--             PARTITION BY p.person_id 
--             ORDER BY m.release_date
--             ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
--         ) AS last_movie_date
--     FROM 
--         movies.person p
--     JOIN 
--         movies.movie_cast mc ON p.person_id = mc.person_id
--     JOIN 
--         movies.movie m ON mc.movie_id = m.movie_id
-- )
-- SELECT DISTINCT -- this is necessary bc we have repeated rows in the CTE
--     actor_name,
--     first_movie,
--     first_movie_date,
--     last_movie,
--     last_movie_date
-- FROM 
--     actor_movies
-- ORDER BY 
--     actor_name;


-- Task 2: Create a nested subquery to identify genres where the 
-- average movie revenue is above the overall average movie revenue.
-- Within those genres, use a window function to rank movies by their 
-- popularity. Display the genre, movie title, revenue, and rank.

