SET search_path TO movies; -- need this!!!

-- -----------------------------------------------------------------------------
-- -----------------------------------------------------------------------------
/*
🌟 Exercise 1: Movie Rankings and Analysis


SQL Dataset we will be using

    Movies Database


Task 1: Rank Movies by Popularity within Each Genre

Use the RANK() function to rank movies by their popularity within each genre.
Display the genre name, movie title, and their rank based on popularity.
*/


-- SELECT 
--     g.genre_name,
--     m.title,
--     RANK() OVER (
-- 		PARTITION BY g.genre_name 
-- 		ORDER BY m.popularity DESC
-- 		) AS popularity_rank
-- FROM 
--     movie AS m
-- JOIN 
--     movie_genres AS mg ON m.movie_id = mg.movie_id
-- JOIN 
--     genre AS g ON mg.genre_id = g.genre_id
-- ORDER BY 
--     g.genre_name, popularity_rank;

-- --------------------------------------------------------------------------------
/*
Task 2: Identify the Top 3 Movies by Revenue within Each Production Company

Use the NTILE() function to divide the movies produced by each production company 
into quartiles based on revenue. Display the company name, movie title, revenue, and quartile.
*/

-- -- step 1: select relevant data and calculate quartiles
-- WITH ranked_movies AS (
--     SELECT 
--         pc.company_name,
--         m.title,
--         m.revenue,
-- 		-- divide into quartiles by revenue
--         NTILE(4) OVER (
-- 			PARTITION BY pc.company_name 
-- 			ORDER BY m.revenue DESC
-- 			) AS revenue_quartile
--     FROM 
--         movie AS m
--     JOIN 
--         movie_company AS mc ON m.movie_id = mc.movie_id
--     JOIN 
--         production_company AS pc ON mc.company_id = pc.company_id
-- )

-- -- step 2: filter for top 3 movies in each quartile
-- SELECT 
--     company_name, 
--     title, 
--     revenue, 
--     revenue_quartile 
-- FROM 
--     ranked_movies 
-- WHERE 
--     revenue_quartile = 1 -- filter for the top quartile (highest revenue)
-- ORDER BY 
--     company_name, revenue DESC; -- order by company name and revenue

-- --------------------------------------------------------------------------------

-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre
-- Use the SUM() function with the ROWS frame specification to calculate the running
-- total of movie budgets within each genre. Display the genre name, movie title, budget,
-- and running total budget.

-- -- step 1: calculate running total of movie budgets by genre
-- WITH budget_totals AS (
--     SELECT 
--         g.genre_name,
--         m.title,
--         m.budget,
--         SUM(m.budget) OVER (
-- 			PARTITION BY g.genre_name 
-- 			ORDER BY m.release_date 
-- 			ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
-- 			) AS running_total_budget
--     FROM 
--         movie AS m
--     JOIN 
--         movie_genres AS mg ON m.movie_id = mg.movie_id
--     JOIN 
--         genre AS g ON mg.genre_id = g.genre_id
-- )

-- -- step 2: select final results
-- SELECT 
--     genre_name, 
--     title, 
--     budget, 
--     running_total_budget 
-- FROM 
--     budget_totals 
-- ORDER BY 
--     genre_name, running_total_budget;

-- ------------------------------------------------------------------------------

-- Task 4: Identify the Most Recent Movie for Each Genre

-- Use the FIRST_VALUE() function to find the most recent movie within each genre 
-- based on the release date. Display the genre name, movie title, and release date.

-- -- step 1: select most recent movie for each genre
-- WITH recent_movies AS (
--     SELECT 
--         g.genre_name,
--         m.title,
--         m.release_date,
--         FIRST_VALUE(m.title) OVER (
--             PARTITION BY g.genre_name
--             ORDER BY m.release_date DESC
--         	) AS most_recent_movie_title,
--         FIRST_VALUE(m.release_date) OVER ( 
--             PARTITION BY g.genre_name 
--             ORDER BY m.release_date DESC 
--         	) AS most_recent_release_date
--     FROM 
--         movie AS m
--     JOIN 
--         movie_genres AS mg ON m.movie_id = mg.movie_id
--     JOIN 
--         genre AS g ON mg.genre_id = g.genre_id
-- )

-- -- step 2: select final results where the title matches the most recent movie
-- SELECT 
--     genre_name, 
--     most_recent_movie_title AS title, 
--     most_recent_release_date AS release_date 
-- FROM 
--     recent_movies 
-- WHERE 
--     title = most_recent_movie_title -- filter to show only the most recent movie per genre
-- ORDER BY 
--     genre_name;



-- ------------------------------------------------------------------------------------------
-- ------------------------------------------------------------------------------------------
/*
🌟 Exercise 2: Cast and Crew Performance Analysis


Task 1: Rank Actors by Their Appearance in Movies

Use the DENSE_RANK() function to rank actors based on the number of movies 
they have appeared in. Display the actor’s name and their rank.
*/

-- -- step 1: count appearances and rank actors
-- WITH actor_appearances AS (
--     SELECT 
--         p.person_name,
--         COUNT(mc.movie_id) AS movie_count,
--         DENSE_RANK() OVER (
-- 			ORDER BY COUNT(mc.movie_id) DESC
-- 			) AS appearance_rank -- rank actors by their movie count
--     FROM 
--         movie_cast AS mc
--     JOIN 
--         person AS p ON mc.person_id = p.person_id -- join with person table to get actor names
--     GROUP BY 
--         p.person_name -- group by actor's name
-- )

-- -- step 2: select final results
-- SELECT 
--     person_name, 
--     appearance_rank 
-- FROM 
--     actor_appearances 
-- ORDER BY 
--     appearance_rank; -- order by rank

-- -------------------------------------------------------------------------------------------
-- Task 2: Identify the Top Director by Average Movie Rating

-- Use a CTE and the RANK() function to find the director with the highest 
-- average movie rating. Display the director’s name and their average rating.

-- -- step 1: calculate average ratings for directors
-- WITH director_ratings AS (
--     SELECT 
--         pc.person_name,
--         AVG(m.vote_average) AS average_rating, -- average movie rating
--         RANK() OVER (
-- 			ORDER BY AVG(m.vote_average) DESC
-- 			) AS rating_rank -- rank directors by average rating
--     FROM 
--         movie_crew AS mc
--     JOIN 
--         person AS pc ON mc.person_id = pc.person_id
--     JOIN 
--         movie AS m ON mc.movie_id = m.movie_id
--     WHERE 
--         mc.job = 'Director' -- filter for directors only
--     GROUP BY 
--         pc.person_name -- group by director's name
-- )

-- -- step 2: select final results for the top director
-- SELECT 
--     person_name, 
--     average_rating 
-- FROM 
--     director_ratings 
-- WHERE 
--     rating_rank = 1; -- filter the top-ranked director

----------------------------------------------------------------------------------------
-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

-- Use the SUM() function to calculate the cumulative revenue of movies acted
-- by each actor. Display the actor’s name and the cumulative revenue.

-- -- step 1: calculate cumulative revenue for each actor
-- WITH actor_revenue AS (
--     SELECT 
--         p.person_name, -- select actor name
--         m.revenue,
--         SUM(m.revenue) OVER (
-- 			PARTITION BY p.person_name 
-- 			ORDER BY m.release_date 
-- 			ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
-- 		) AS cumulative_revenue -- here cumulative revenue
--     FROM 
--         movie_cast AS mc
--     JOIN 
--         person AS p ON mc.person_id = p.person_id -- join with person table to get actor names
--     JOIN 
--         movie AS m ON mc.movie_id = m.movie_id  -- join with movie table to get revenue
-- )

-- -- step 2: select final results
-- SELECT 
--     person_name, 
-- 	-- MAX to get the cumulative revenue for each actor
--     MAX(cumulative_revenue) AS total_cumulative_revenue
-- FROM 
--     actor_revenue 
-- GROUP BY 
--     person_name -- group by actor name
-- ORDER BY 
--     person_name; -- order by actor's name

-------------------------------------------------------------------------------------------
-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget

-- Use a CTE and a window function to find the director whose movies have
-- the highest total budget. Display the director’s name and the total budget.

-- -- step 1: calculate total budget for each director
-- WITH director_budget AS (
--     SELECT 
--         pc.person_name, -- director's name
--         SUM(m.budget) AS total_budget, -- total budget for each director
--         RANK() OVER (
-- 			ORDER BY SUM(m.budget) DESC
-- 			) AS budget_rank -- rank directors by total budget
--     FROM 
--         movie_crew AS mc
--     JOIN 
--         person AS pc ON mc.person_id = pc.person_id
--     JOIN 
--         movie AS m ON mc.movie_id = m.movie_id -- join with movie table to get budgets
--     WHERE 
--         mc.job = 'Director' -- filter for directors only
--     GROUP BY 
--         pc.person_name -- group by director name
-- )

-- -- step 2: select final results for the top director
-- SELECT 
--     person_name, 
--     total_budget 
-- FROM 
--     director_budget 
-- WHERE 
--     budget_rank = 1; -- filter the top ranked director

/*
The total production budget for Steven Spielberg's films from 1975 to 
2018 is approximately $2.09 billion. His movies have generated over 
$10.75 billion in global box office revenue, making him the highest-grossing 
director in cinematic history.
*/
