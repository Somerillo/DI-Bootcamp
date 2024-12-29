/*
-- Exercise 1: Detailed Medal Analysis

-- SQL Dataset we will be using

--     Olympic Data

-- Task 1: Identify competitors who have won at least one medal in events spanning both 
-- Summer and Winter Olympics. Create a temporary table to store these competitors and
-- their medal counts for each season, and then display the contents of this table.

-- 1. temp table
CREATE TEMPORARY TABLE CompetitorMedals (
    competitor_id INT,
    season VARCHAR(10),
    medal_count INT
);

-- 2. insert data
INSERT INTO CompetitorMedals (competitor_id, season, medal_count)
SELECT ce.competitor_id, 'Summer' AS season, COUNT(*) AS medal_count
FROM competitor_event ce
WHERE ce.medal_id IS NOT NULL
AND ce.competitor_id IN (
    SELECT DISTINCT gc.person_id
    FROM games_competitor gc
    WHERE gc.games_id IN (SELECT id FROM games WHERE season = 'Summer')
)
GROUP BY ce.competitor_id

UNION ALL

SELECT ce.competitor_id, 'Winter' AS season, COUNT(*) AS medal_count
FROM competitor_event ce
WHERE ce.medal_id IS NOT NULL
AND ce.competitor_id IN (
    SELECT DISTINCT gc.person_id
    FROM games_competitor gc
    WHERE gc.games_id IN (SELECT id FROM games WHERE season = 'Winter')
)
GROUP BY ce.competitor_id;

-- verify
SELECT * FROM CompetitorMedals;


-- Task 2: Create a temporary table to store competitors who have won medals
-- in exactly two different sports, and then use a subquery to identify the top 3
-- competitors with the highest total number of medals across all sports. Display the contents of this table.

-- 1. temp table medal count by sport
CREATE TEMPORARY TABLE CompetitorsTwoSports (
    competitor_id INT,
    sport_count INT,
    total_medals INT
);

-- 2. insert data in temp table
INSERT INTO CompetitorsTwoSports (competitor_id, sport_count, total_medals)
SELECT ce.competitor_id,
       COUNT(DISTINCT e.sport_id) AS sport_count,
       COUNT(ce.medal_id) AS total_medals
FROM competitor_event ce
JOIN event e ON ce.event_id = e.id
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id
HAVING COUNT(DISTINCT e.sport_id) = 2;

-- 3. verify
SELECT * FROM CompetitorsTwoSports;

-- 4. top comp
SELECT competitor_id, total_medals
FROM CompetitorsTwoSports
ORDER BY total_medals DESC
LIMIT 3;
*/

--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
/*
-- Exercise 2: Region and Competitor Performance

-- Task 1: Retrieve the regions that have competitors who have won the highest number of medals
-- in a single Olympic event. Use a subquery to determine the event with the highest number of medals
-- for each competitor, and then display the top 5 regions with the highest total medals.

-- 1. subquery for highst medal count per competitor
SELECT competitor_id, MAX(medal_count) AS max_medals
FROM (
    SELECT competitor_id, event_id, COUNT(*) AS medal_count
    FROM competitor_event
    WHERE medal_id IS NOT NULL
    GROUP BY competitor_id, event_id
) AS event_medals
GROUP BY competitor_id;

-- 2. main query to retrieve regions and tot medals
SELECT nr.region_name, SUM(em.max_medals) AS total_medals
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN (
    SELECT competitor_id, MAX(medal_count) AS max_medals
    FROM (
        SELECT competitor_id, event_id, COUNT(*) AS medal_count
        FROM competitor_event
        WHERE medal_id IS NOT NULL
        GROUP BY competitor_id, event_id
    ) AS event_medals
    GROUP BY competitor_id
) em ON pr.person_id = em.competitor_id
GROUP BY nr.region_name
ORDER BY total_medals DESC
LIMIT 5;

----------------------------------------------------------------------------------------------

-- Task 2: Create a temporary table to store competitors who have participated in more
-- than three Olympic Games but have not won any medals. Retrieve and display the contents
-- of this table, including their full names and the number of games they participated in.

-- 1. temp table
CREATE TEMPORARY TABLE CompetitorsNoMedals (
    competitor_id INT,
    full_name VARCHAR(100),
    games_participated INT
);

-- 2. insert into tt
INSERT INTO CompetitorsNoMedals (competitor_id, full_name, games_participated)
SELECT gc.person_id, p.full_name, COUNT(DISTINCT gc.games_id) AS games_participated
FROM games_competitor gc
JOIN person p ON gc.person_id = p.id
LEFT JOIN competitor_event ce ON gc.person_id = ce.competitor_id
WHERE ce.medal_id IS NULL  -- competitors who have not won any medals
GROUP BY gc.person_id, p.full_name
HAVING COUNT(DISTINCT gc.games_id) > 3;  -- more than 3 OG
*/
-- verify
-- SELECT * FROM CompetitorsNoMedals; -- EMPTY????????????????

-- -- this is not empty:
-- SELECT gc.person_id, COUNT(DISTINCT gc.games_id) AS games_participated
-- FROM games_competitor gc
-- GROUP BY gc.person_id
-- HAVING COUNT(DISTINCT gc.games_id) > 3;

-- -- but this one is empty:
-- SELECT DISTINCT ce.competitor_id
-- FROM competitor_event ce
-- WHERE ce.medal_id IS NULL;

-- At this point if its ok not i dont really care