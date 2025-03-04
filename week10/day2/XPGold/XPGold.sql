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

WITH BudgetComparison AS (
    SELECT 
        title,
        release_date,
        budget,
        LAG(budget) OVER (ORDER BY release_date) AS previous_budget,
        LEAD(budget) OVER (ORDER BY release_date) AS next_budget
    FROM 
        movies.movie
)
SELECT 
    title,
    release_date,
    budget,
    previous_budget,
    next_budget
FROM 
    BudgetComparison
WHERE 
    budget > previous_budget
    AND budget > next_budget
ORDER BY 
    release_date;

