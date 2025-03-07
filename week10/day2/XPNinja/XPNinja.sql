/*
Task 1: Identify the top 5 movies in each genre based on the revenue 
growth rate compared to the previous movie released in the same 
genre. Use window functions to calculate the growth rate and rank the 
movies. Then, list the movies with their rank and revenue growth rate.
*/
-- WITH genre_growth AS (
--     SELECT
--         g.genre_name AS genre,
--         m.title,
--         m.release_date,
--         m.revenue,
--         LAG(m.revenue) OVER (
--             PARTITION BY g.genre_id 
--             ORDER BY m.release_date
--         ) AS previous_revenue
--     FROM
--         movies.movie m
--     JOIN 
--         movies.movie_genres mg ON m.movie_id = mg.movie_id
--     JOIN 
--         movies.genre g ON mg.genre_id = g.genre_id
--     WHERE
--         m.revenue IS NOT NULL
-- ),
-- calculated_rates AS (
--     SELECT
--         genre,
--         title,
--         release_date,
--         revenue,
--         ROUND(
--             ((revenue - previous_revenue) * 100.0 / NULLIF(previous_revenue, 0)),
--             2
--         ) AS growth_rate,
--         ROW_NUMBER() OVER (
--             PARTITION BY genre 
--             ORDER BY ((revenue - previous_revenue) * 100.0 / NULLIF(previous_revenue, 0)) DESC
--         ) AS genre_rank
--     FROM
--         genre_growth
--     WHERE
--         previous_revenue IS NOT NULL
-- )
-- SELECT
--     genre,
--     title,
--     growth_rate AS revenue_growth_rate_percent,
--     genre_rank
-- FROM
--     calculated_rates
-- WHERE
--     genre_rank <= 5
-- ORDER BY
--     genre,
--     genre_rank;




/*
Task 2: Calculate the cumulative average rating for each movie in each genre, 
but only include movies that have at least 50 votes. Use the AVG() function 
with windowing and filter the results.
*/
WITH filtered_movies AS (
    SELECT 
        g.genre_name AS genre,
        m.title,
        m.release_date,
        m.vote_average,
        m.vote_count
    FROM 
        movies.movie m
    JOIN 
        movies.movie_genres mg ON m.movie_id = mg.movie_id
    JOIN 
        movies.genre g ON mg.genre_id = g.genre_id
    WHERE 
        m.vote_count >= 50
        AND m.release_date IS NOT NULL
)
SELECT 
    genre,
    title,
    release_date,
    vote_average,
    ROUND(
        AVG(vote_average) OVER (
            PARTITION BY genre 
            ORDER BY release_date
        ), 2
    ) AS cumulative_avg_rating
FROM 
    filtered_movies
ORDER BY 
    genre, 
    release_date;