I am not upset but furious for the fact that i paid 30k ILS for a DA course that every-single-week
shows only improvisation. It wasnt only once or twice, and today it was the worst of all.
Spending one and a half hour trying simply to start the exercice and after that spend another 4
hours to see how to connect the tables, to finally be able to make the exercise

NOT EVEN A BRIEF COLUMN MAP OR DESCRIPTION???? 

I am not complaining about the teachers but about the organization.



-- Task 1: Find the average age of competitors who have won at least one medal, 
-- grouped by the type of medal they won. Use a correlated subquery to achieve this.
/*
SELECT m.medal_name, AVG(gc.age) AS average_age
FROM medal m
JOIN competitor_event ce ON m.id = ce.medal_id
JOIN games_competitor gc ON ce.competitor_id = gc.person_id
WHERE gc.person_id IN (
    SELECT ce_inner.competitor_id
    FROM competitor_event ce_inner
    WHERE ce_inner.medal_id IS NOT NULL 
      AND ce_inner.competitor_id = ce.competitor_id
)
GROUP BY m.medal_name;

-- Avoiding Correlated Subqueries: Use joins instead of correlated subqueries when possible, 
-- as joins are generally more efficient. Correlated subqueries are executed once for each row processed
-- by the outer query, which can be slow. Joins, on the other hand,
-- combine rows from two or more tables based on related columns, and are usually faster.
*/

--------------------------------------------------------------------------------------------------------
/*
-- Task 2: Identify the top 5 regions with the highest number of unique competitors who have
-- participated in more than 3 different events. Use nested subqueries to filter and aggregate the data.

SELECT nr.region_name, COUNT(DISTINCT gc.person_id) AS unique_competitors
FROM person_region pr
JOIN games_competitor gc ON pr.person_id = gc.person_id
JOIN noc_region nr ON pr.region_id = nr.id
WHERE gc.person_id IN (
    SELECT ce.competitor_id
    FROM competitor_event ce
    GROUP BY ce.competitor_id
    HAVING COUNT(DISTINCT ce.event_id) > 3
)
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5;
*/

-------------------------------------------------------------------------------------------
/*
-- Task 3: Create a temporary table to store the total number of medals won by each competitor and
-- filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.

-- Step 1: Create the temporary table to store total medals by each competitor
CREATE TEMPORARY TABLE competitor_medals AS
SELECT 
    ce.competitor_id,
    COUNT(ce.medal_id) AS total_medals
FROM competitor_event ce
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id;

-- Step 2: Query the temporary table to filter competitors with more than 2 medals
SELECT competitor_id, total_medals
FROM competitor_medals
WHERE total_medals > 2;
*/

------------------------------------------------------------------------------------------------------
/*
-- Task 4: Use a subquery within a DELETE statement to remove records of competitors
-- who have not won any medals from a temporary table created for analysis.

-- Step 1: Create the temporary table for analysis
CREATE TEMPORARY TABLE competitor_analysis AS
SELECT 
    ce.competitor_id,
    COUNT(ce.medal_id) AS total_medals
FROM competitor_event ce
GROUP BY ce.competitor_id;

-- Step 2: Use a DELETE statement with a subquery to remove competitors with no medals
DELETE FROM competitor_analysis
WHERE competitor_id IN (
    SELECT competitor_id
    FROM competitor_analysis
    WHERE total_medals = 0
);
*/

--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
/*
Exercise 2: Advanced Data Manipulation and Optimization
*/

/*
-- Task 1: Update the heights of competitors based on the average height of competitors from the same region.
-- Use a correlated subquery within the UPDATE statement.
UPDATE person
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    JOIN person_region pr2 ON p2.id = pr2.person_id
    WHERE pr2.region_id = (
        SELECT pr.region_id
        FROM person_region pr
        WHERE pr.person_id = person.id
    )
)
WHERE EXISTS ( -- the EXISTS clause checks if the person has an entry in the person_region table
    SELECT 1 -- SELECT 1 doesn't return any data, it just checks if there is any row that matches the condition
    FROM person_region pr
    WHERE pr.person_id = person.id
);
*/


---------------------------------------------------------------------------------------------------------

-- Task 2: Insert new records into a temporary table for competitors who participated in more than one event
-- in the same games and list their total number of events participated. Use nested subqueries for filtering.
/*
-- create the temporary table
CREATE TEMPORARY TABLE CompetitorEventsTemp (
    competitor_id INT,
    total_events INT
);

-- insert data into the temporary table
INSERT INTO CompetitorEventsTemp (competitor_id, total_events)
SELECT gc.person_id, COUNT(DISTINCT ce.event_id) AS total_events
FROM games_competitor gc
JOIN competitor_event ce ON gc.person_id = ce.competitor_id
GROUP BY gc.person_id, gc.games_id
HAVING COUNT(DISTINCT ce.event_id) > 1;

-- verify
SELECT * from CompetitorEventsTemp;

*/

----------------------------------------------------------------------------------------
/*
-- Task 3: Identify regions where the average number of medals won per competitor is
-- greater than the overall average. Use subqueries to calculate and compare averages.

-- step 1: First, we need to calculate the overall average number of medals won per competitor. This will be done in a subquery
SELECT AVG(medal_count) AS overall_average
FROM (
    SELECT ce.competitor_id, COUNT(*) AS medal_count
    FROM competitor_event ce
    WHERE ce.medal_id IS NOT NULL
    GROUP BY ce.competitor_id
) AS competitor_medals;

-- step 2: we use overall average in another subquery to find regions
-- where the average number of medals per competitor exceeds this average.
SELECT nr.region_name, AVG(medal_count) AS average_medals_per_competitor
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN (
    SELECT ce.competitor_id, COUNT(*) AS medal_count
    FROM competitor_event ce
    WHERE ce.medal_id IS NOT NULL
    GROUP BY ce.competitor_id
) AS competitor_medals ON pr.person_id = competitor_medals.competitor_id
GROUP BY nr.region_name
HAVING AVG(medal_count) > (
    SELECT AVG(medal_count)
    FROM (
        SELECT ce.competitor_id, COUNT(*) AS medal_count
        FROM competitor_event ce
        WHERE ce.medal_id IS NOT NULL
        GROUP BY ce.competitor_id
    ) AS overall_medals
);
*/

-----------------------------------------------------------------------------------
/*
-- Task 4: Create a temporary table to track competitors’ participation across different seasons
-- and identify those who have participated in both Summer and Winter games.

-- 1. Temporary table
CREATE TEMPORARY TABLE CompetitorParticipation (
    competitor_id INT,
    season VARCHAR(10)
);

-- 2. insert data
INSERT INTO CompetitorParticipation (competitor_id, season)
SELECT gc.person_id, 'Summer' AS season
FROM games_competitor gc
JOIN competitor_event ce ON gc.person_id = ce.competitor_id
WHERE gc.games_id IN (SELECT id FROM games WHERE season = 'Summer')
GROUP BY gc.person_id

UNION ALL

SELECT gc.person_id, 'Winter' AS season
FROM games_competitor gc
JOIN competitor_event ce ON gc.person_id = ce.competitor_id
WHERE gc.games_id IN (SELECT id FROM games WHERE season = 'Winter')
GROUP BY gc.person_id;

SELECT * from CompetitorParticipation;

-- 3. identify those who participated in both
SELECT competitor_id
FROM CompetitorParticipation
GROUP BY competitor_id
HAVING COUNT(DISTINCT season) = 2;

*/
