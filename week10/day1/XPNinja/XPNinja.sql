/*
🌟 Exercise 1: Advanced Medal Analysis

SQL Dataset we will be using

Olympic Data

Task 1: Identify competitors who have won medals in both individual 
and team events, and calculate the total number of medals they have 
won in each category. Create a temporary table to store the results 
and ensure it includes their full name, total medals in individual 
events, and total medals in team events.
*/

-- -- Drop the table if exists
-- DROP TABLE IF EXISTS medal_winners;

-- -- Create temporary table to store results
-- CREATE TEMP TABLE medal_winners AS
-- WITH individual_medals AS (
--     SELECT gc.person_id, COUNT(DISTINCT m.id) AS individual_medal_count
--     FROM olympics.games_competitor gc
--     JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
--     JOIN olympics.event e ON ce.event_id = e.id
--     JOIN olympics.medal m ON ce.medal_id = m.id
--     GROUP BY gc.person_id, e.id
--     HAVING COUNT(gc.person_id) = 1
-- ),
-- team_medals AS (
--     SELECT gc.person_id, COUNT(DISTINCT m.id) AS team_medal_count
--     FROM olympics.games_competitor gc
--     JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
--     JOIN olympics.event e ON ce.event_id = e.id
--     JOIN olympics.medal m ON ce.medal_id = m.id
--     GROUP BY gc.person_id, e.id
--     HAVING COUNT(gc.person_id) > 1
-- )
-- SELECT 
--     p.id AS person_id,
--     p.full_name,
--     COALESCE(im.individual_medal_count, 0) AS individual_medals,
--     COALESCE(tm.team_medal_count, 0) AS team_medals
-- FROM olympics.person p
-- JOIN individual_medals im ON p.id = im.person_id
-- JOIN team_medals tm ON p.id = tm.person_id;

-- -- Display results
-- SELECT * FROM medal_winners
-- ORDER BY individual_medals + team_medals DESC, individual_medals DESC
-- LIMIT 10;

-- -- Drop the table after using it
-- DROP TABLE IF EXISTS medal_winners;

/*
🌟 Exercise 2: Complex Event Participation

Task 2: Create a temporary table to store the competitors who have won 
medals in exactly 3 different sports. Then, using this temporary table, 
identify the top 3 competitors with the highest total number of medals 
across all sports. Use nested subqueries and aggregation.
*/
-- -- Drop the table if exists
-- DROP TABLE IF EXISTS three_sport_medalists;

-- -- Create temporary table for competitors with medals in exactly 3 sports
-- CREATE TEMP TABLE three_sport_medalists AS
-- SELECT 
--     gc.person_id,
--     p.full_name,
--     COUNT(DISTINCT s.id) AS sport_count,
--     COUNT(m.id) AS total_medals
-- FROM olympics.games_competitor gc
-- JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
-- JOIN olympics.event e ON ce.event_id = e.id
-- JOIN olympics.sport s ON e.sport_id = s.id
-- JOIN olympics.medal m ON ce.medal_id = m.id
-- JOIN olympics.person p ON gc.person_id = p.id
-- GROUP BY gc.person_id, p.full_name
-- HAVING COUNT(DISTINCT s.id) = 3;

-- -- Identify top 3 competitors with highest total medal count
-- SELECT person_id, full_name, total_medals
-- FROM three_sport_medalists
-- ORDER BY total_medals DESC
-- LIMIT 3;

-- -- Drop the table after finish
-- DROP TABLE IF EXISTS three_sport_medalists;



/*
🌟 Exercise 3: Cross-Region and Season Analysis

Task 3: Find the regions that have competitors who have won medals in both
the Summer and Winter games, and calculate the average age of these 
competitors. Use subqueries and temporary tables to ensure accurate 
and efficient calculations.
*/
-- -- Drop the table if exists
-- DROP TABLE IF EXISTS dual_season_medalists;

-- -- Create temporary table for medal winners in both seasons
-- CREATE TEMP TABLE dual_season_medalists AS
-- SELECT DISTINCT pr.region_id, gc.person_id, gc.age
-- FROM olympics.person_region pr
-- JOIN olympics.games_competitor gc ON pr.person_id = gc.person_id
-- JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
-- JOIN olympics.medal m ON ce.medal_id = m.id
-- JOIN olympics.games g ON gc.games_id = g.id
-- WHERE g.season IN ('Summer', 'Winter')
-- GROUP BY pr.region_id, gc.person_id, gc.age
-- HAVING COUNT(DISTINCT g.season) = 2;

-- -- Calculate average age and select regions
-- SELECT 
--     nr.region_name,
--     AVG(dsm.age) AS avg_age
-- FROM dual_season_medalists dsm
-- JOIN olympics.noc_region nr ON dsm.region_id = nr.id
-- GROUP BY nr.region_name
-- ORDER BY avg_age DESC;

-- -- Drop the table after finish
-- DROP TABLE IF EXISTS dual_season_medalists;