SET search_path TO movies; -- need this!!!

-- Daily Challenge : Advanced Movie Data Analysis

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
-- 🌟 Task 1: Calculate the Average Budget Growth Rate for Each Production Company

-- Calculate the average budget growth rate for each production company across
-- all movies they have produced. Use window functions to determine the budget 
-- growth rate and then calculate the average growth rate.

-- -- step 1: calculate budget growth rates for each movie
-- WITH budget_growth AS (
--     SELECT 
--         pc.company_name, -- production company name
--         m.budget,
--         LAG(m.budget) OVER (
-- 			PARTITION BY pc.company_name 
-- 			ORDER BY m.release_date
-- 		) AS previous_budget, -- get previous movie's budget
--         (
-- 			m.budget - LAG(m.budget) OVER (
-- 				PARTITION BY pc.company_name 
-- 				ORDER BY m.release_date
-- 			)
-- 		) / NULLIF(
-- 			LAG(m.budget) OVER (
-- 				PARTITION BY pc.company_name 
-- 				ORDER BY m.release_date
-- 			), 0
-- 		) AS growth_rate -- calculate growth rate
--     FROM 
--         movie_company AS mc
--     JOIN
-- 		-- join with production_company table to get company names
--         production_company AS pc ON mc.company_id = pc.company_id
--     JOIN
-- 		-- join with movie table to get budgets
--         movie AS m ON mc.movie_id = m.movie_id
-- )

-- -- step 2: calculate average growth rate for each production company
-- SELECT 
--     company_name, 
--     AVG(growth_rate) AS average_growth_rate
-- FROM 
--     budget_growth 
-- WHERE 
--     growth_rate IS NOT NULL -- filter out null values (first movie has no previous budget)
-- GROUP BY 
--     company_name
-- ORDER BY 
--     average_growth_rate DESC;

---------------------------------------------------------------------------------------------
-- 🌟 Task 2: Determine the Most Consistently High-Rated Actor

-- Identify the actor who has appeared in the most movies that are 
-- rated above the average rating of all movies. Use window functions 
-- and CTEs to calculate the average rating and filter the actors based on this criterion.

-- -- step 1: calculate the average movie rating
-- WITH average_rating AS (
--     SELECT 
--         AVG(vote_average) AS avg_rating -- overall average rating
--     FROM 
--         movie -- from movie table
-- ),

-- -- step 2: count movies for each actor with ratings above average
-- actor_high_rated_movies AS (
--     SELECT 
--         p.person_name, -- actor name
--         COUNT(m.movie_id) AS high_rated_count, -- count movies rated above average
-- 		-- rank actors by count of high-rated movies
--         RANK() OVER (ORDER BY COUNT(m.movie_id) DESC) AS rank
--     FROM 
--         movie_cast AS mc
--     JOIN 
--         person AS p ON mc.person_id = p.person_id -- join with person table to get actor names
--     JOIN 
--         movie AS m ON mc.movie_id = m.movie_id -- join with movie table to get ratings
--     CROSS JOIN 
--         average_rating ar -- cross join to get average rating
--     WHERE 
--         m.vote_average > ar.avg_rating -- filter movies rated above average
--     GROUP BY 
--         p.person_name -- group by actor name
-- )

-- -- step 3: select the most consistently high-rated actor
-- SELECT 
--     person_name, 
--     high_rated_count 
-- FROM 
--     actor_high_rated_movies 
-- WHERE 
--     rank = 1; -- filter for the top ranked actor

--------------------------------------------------------------------------------------------
-- 🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre

-- Calculate the rolling average revenue for movies within each genre, 
-- considering only the last three movies released in the genre. Use window 
-- functions with the ROWS frame specification to achieve this.

-- -- step 1: calculate rolling average revenue for each genre
-- WITH genre_revenue AS (
--     SELECT 
--         g.genre_name,
--         m.revenue,
--         m.release_date,
-- 		-- assign row numbers to movies within each genre
--         ROW_NUMBER() OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS rn
--     FROM 
--         movie AS m
--     JOIN 
--         movie_genres AS mg ON m.movie_id = mg.movie_id
--     JOIN 
--         genre AS g ON mg.genre_id = g.genre_id
-- )

-- -- step 2: calculate rolling average for the last three movies per genre
-- SELECT 
--     genre_name, 
--     AVG(revenue) AS rolling_average_revenue -- average revenue for the last three movies
-- FROM 
--     genre_revenue 
-- WHERE 
--     rn <= 3 -- consider only the last three movies
-- GROUP BY 
--     genre_name
-- ORDER BY 
--     genre_name;

---------------------------------------------------------------------------------------------
-- 🌟 Task 4: Identify the Highest-Grossing Movie Series

-- Identify the movie series (based on shared keywords) with the highest total
-- revenue. Use window functions and CTEs to group movies by their series and 
-- calculate the total revenue.

-- -- step 1: calculate total revenue for each movie series based on keywords
-- WITH series_revenue AS (
--     SELECT 
--         k.keyword_name, -- keyword name as series identifier
--         m.movie_id,
--         SUM(m.revenue) AS total_revenue -- total revenue for each movie
--     FROM 
--         movie_keywords AS mk
--     JOIN 
--         keyword AS k ON mk.keyword_id = k.keyword_id -- join with keyword table to get keyword names
--     JOIN 
--         movie AS m ON mk.movie_id = m.movie_id -- join with movie table to access revenue
--     GROUP BY 
--         k.keyword_name, m.movie_id -- group them
-- ),

-- -- step 2: aggregate total revenue by series (keyword)
-- keyword_revenue AS (
--     SELECT 
--         keyword_name,
--         SUM(total_revenue) AS series_total_revenue, -- sum the total revenues for each series
--         RANK() OVER (ORDER BY SUM(total_revenue) DESC) AS revenue_rank  -- rank series by total revenue
--     FROM 
--         series_revenue -- use the previous CTE results
--     GROUP BY 
--         keyword_name -- group it
-- )

-- -- step 3: select the highestgrossing movie series
-- SELECT 
--     keyword_name, 
--     series_total_revenue -- displays the series name and its total revenue
-- FROM 
--     keyword_revenue 
-- WHERE 
--     revenue_rank = 1; -- filter to get the top ranked series

-------------------------------------------------------------------------------------------------

