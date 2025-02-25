-- ############################################################################
/*
🌟 Exercise 1: Comprehensive Competitor Analysis


SQL Dataset we will be using

    Olympic Data

    Task 1: Identify competitors who have won medals in both individual and team events. Use subqueries to distinguish between individual and team events and correlate with medal records.

    Task 2: Create a temporary table to store the cumulative medal count for each region, then find the top 3 regions with the highest cumulative medal count. Use nested subqueries and aggregation.

    Task 3: Insert records into a temporary table for competitors who have won at least one gold medal and participated in more than 2 different games. Use subqueries to aggregate the data.

*/

-- -- list all tables in the olympics schema
-- SELECT table_name 
-- FROM information_schema.tables 
-- WHERE table_schema = 'olympics';

-- WITH individual_medals AS (
--     SELECT DISTINCT gc.person_id
--     FROM olympics.games_competitor gc
--     JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
--     JOIN olympics.event e ON ce.event_id = e.id
--     JOIN olympics.medal m ON ce.medal_id = m.id
--     GROUP BY gc.person_id, e.id, m.id
--     HAVING COUNT(gc.person_id) = 1
-- ),
-- team_medals AS (
--     SELECT DISTINCT gc.person_id
--     FROM olympics.games_competitor gc
--     JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
--     JOIN olympics.event e ON ce.event_id = e.id
--     JOIN olympics.medal m ON ce.medal_id = m.id
--     GROUP BY gc.person_id, e.id, m.id
--     HAVING COUNT(gc.person_id) > 1
-- )
-- SELECT p.id, p.full_name, p.gender
-- FROM olympics.person p
-- WHERE p.id IN (
--     SELECT person_id FROM individual_medals
--     INTERSECT
--     SELECT person_id FROM team_medals
-- )
-- ORDER BY p.full_name;



/*
Task 2: Create a temporary table to store the cumulative medal 
count for each region, then find the top 3 regions with the 
highest cumulative medal count. Use nested subqueries and aggregation.
*/
-- -- Drop table if already exists
-- DROP TABLE IF EXISTS region_medal_count;

-- -- Create a temporary table with cumulative medal count for each region
-- CREATE TEMP TABLE region_medal_count AS
-- SELECT pr.region_id, COUNT(m.id) AS medal_count
-- FROM olympics.person_region pr
-- JOIN olympics.games_competitor gc ON pr.person_id = gc.person_id
-- JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
-- JOIN olympics.medal m ON ce.medal_id = m.id
-- GROUP BY pr.region_id;

-- -- Find the top 3 regions with the highest cumulative medal count
-- SELECT nr.region_name, ranked_regions.medal_count
-- FROM (
-- 	SELECT region_id, medal_count,
--            ROW_NUMBER() OVER (ORDER BY medal_count DESC) AS rank
--     FROM region_medal_count
-- ) ranked_regions
-- JOIN olympics.noc_region nr ON ranked_regions.region_id = nr.id
-- WHERE ranked_regions.rank <= 3
-- ORDER BY ranked_regions.medal_count DESC;



/*
Task 3: Insert records into a temporary table for competitors who have 
won at least one gold medal and participated in more than 2 different 
games. Use subqueries to aggregate the data.
*/
-- -- Drop table if already exists
-- DROP TABLE IF EXISTS gold_medalists_multiple_games;

-- -- Create temp table
-- CREATE TEMP TABLE gold_medalists_multiple_games (
--     person_id INT,
--     full_name VARCHAR(255),
--     gold_medals INT,
--     games_count INT
-- );

-- -- Insert records using subquery
-- INSERT INTO gold_medalists_multiple_games (person_id, full_name, gold_medals, games_count)
-- SELECT p.id, p.full_name, gold_count.medal_count, games_count.game_count
-- FROM olympics.person p
-- JOIN (
--     SELECT gc.person_id, COUNT(DISTINCT m.id) AS medal_count
--     FROM olympics.games_competitor gc
--     JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
--     JOIN olympics.medal m ON ce.medal_id = m.id
--     WHERE m.medal_name = 'Gold'
--     GROUP BY gc.person_id
--     HAVING COUNT(DISTINCT m.id) >= 1
-- ) gold_count ON p.id = gold_count.person_id
-- JOIN (
--     SELECT gc.person_id, COUNT(DISTINCT g.id) AS game_count
--     FROM olympics.games_competitor gc
--     JOIN olympics.games g ON gc.games_id = g.id
--     GROUP BY gc.person_id
--     HAVING COUNT(DISTINCT g.id) > 2
-- ) games_count ON p.id = games_count.person_id;

-- -- Check results
-- SELECT * FROM gold_medalists_multiple_games
-- ORDER BY gold_medals DESC, games_count DESC;



-- ############################################################################
/*
🌟 Exercise 2: Advanced Data Manipulation and Optimization

Task 1: Update the weights of competitors who have won medals in multiple games, setting it to the average weight of all medal winners. Use subqueries within the UPDATE statement.

Task 2: Create a temporary table to store the number of events participated by each competitor, then identify those who have participated in events across different seasons. Use complex subqueries for filtering.

Task 3: Find the average height of competitors from each region who have won at least one medal, and compare it to the average height of all competitors. Use nested subqueries and temporary tables for calculations.
*/

-- UPDATE olympics.person p
-- SET weight = (
--     SELECT AVG(p2.weight)
--     FROM olympics.person p2
--     JOIN olympics.games_competitor gc ON p2.id = gc.person_id
--     JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
--     JOIN olympics.medal m ON ce.medal_id = m.id
--     WHERE p2.weight IS NOT NULL
-- )
-- WHERE p.id IN (
--     SELECT gc.person_id
--     FROM olympics.games_competitor gc
--     JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
--     JOIN olympics.medal m ON ce.medal_id = m.id
--     GROUP BY gc.person_id
--     HAVING COUNT(DISTINCT gc.games_id) > 1
-- );



/*
Task 2: Create a temporary table to store the number of events 
participated by each competitor, then identify those who have 
participated in events across different seasons. Use complex 
subqueries for filtering.
*/
-- -- Drop table if exists
-- DROP TABLE IF EXISTS competitor_event_count;

-- -- Create temporary table
-- CREATE TEMP TABLE competitor_event_count AS
-- SELECT 
--     gc.person_id,
--     p.full_name,
--     COUNT(DISTINCT ce.event_id) AS event_count,
--     COUNT(DISTINCT g.season) AS season_count
-- FROM olympics.games_competitor gc
-- JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
-- JOIN olympics.games g ON gc.games_id = g.id
-- JOIN olympics.person p ON gc.person_id = p.id
-- GROUP BY gc.person_id, p.full_name;

-- -- Identify competitors who participated in events across different seasons
-- SELECT 
--     cec.person_id,
--     cec.full_name,
--     cec.event_count,
--     cec.season_count
-- FROM competitor_event_count cec
-- WHERE cec.season_count > 1
-- ORDER BY cec.event_count DESC, cec.season_count DESC;



/*
Task 3: Find the average height of competitors from each region who 
have won at least one medal, and compare it to the average height 
of all competitors. Use nested subqueries and temporary tables for calculations.
*/
-- -- Drop table if exists
-- DROP TABLE IF EXISTS medal_winners;

-- -- Create a temporary table for medal winners
-- CREATE TEMP TABLE medal_winners AS
-- SELECT DISTINCT pr.region_id, p.id AS person_id, p.height
-- FROM olympics.person_region pr
-- JOIN olympics.person p ON pr.person_id = p.id
-- JOIN olympics.games_competitor gc ON p.id = gc.person_id
-- JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
-- JOIN olympics.medal m ON ce.medal_id = m.id
-- WHERE p.height IS NOT NULL;

-- -- Calculate average heights
-- WITH region_averages AS (
--     SELECT 
--         nr.region_name,
--         AVG(mw.height) AS avg_height_medalists,
--         (SELECT AVG(height) FROM olympics.person WHERE height IS NOT NULL) AS avg_height_all
--     FROM medal_winners mw
--     JOIN olympics.noc_region nr ON mw.region_id = nr.id
--     GROUP BY nr.region_name
-- )
-- SELECT 
--     region_name,
--     avg_height_medalists,
--     avg_height_all,
--     avg_height_medalists - avg_height_all AS height_difference
-- FROM region_averages
-- ORDER BY height_difference DESC;