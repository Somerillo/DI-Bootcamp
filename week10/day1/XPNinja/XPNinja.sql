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

-- Create temporary table to store results
CREATE TEMP TABLE medal_winners AS
WITH individual_medals AS (
    SELECT gc.person_id, COUNT(DISTINCT m.id) AS individual_medal_count
    FROM olympics.games_competitor gc
    JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
    JOIN olympics.event e ON ce.event_id = e.id
    JOIN olympics.medal m ON ce.medal_id = m.id
    GROUP BY gc.person_id, e.id
    HAVING COUNT(gc.person_id) = 1
),
team_medals AS (
    SELECT gc.person_id, COUNT(DISTINCT m.id) AS team_medal_count
    FROM olympics.games_competitor gc
    JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
    JOIN olympics.event e ON ce.event_id = e.id
    JOIN olympics.medal m ON ce.medal_id = m.id
    GROUP BY gc.person_id, e.id
    HAVING COUNT(gc.person_id) > 1
)
SELECT 
    p.id AS person_id,
    p.full_name,
    COALESCE(im.individual_medal_count, 0) AS individual_medals,
    COALESCE(tm.team_medal_count, 0) AS team_medals
FROM olympics.person p
JOIN individual_medals im ON p.id = im.person_id
JOIN team_medals tm ON p.id = tm.person_id;

-- Display results
SELECT * FROM medal_winners
ORDER BY individual_medals + team_medals DESC, individual_medals DESC
LIMIT 10;
