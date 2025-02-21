-- ############################################################################
/*
🌟 Exercise 1: Comprehensive Competitor Analysis


SQL Dataset we will be using

    Olympic Data

    Task 1: Identify competitors who have won medals in both individual and team events. Use subqueries to distinguish between individual and team events and correlate with medal records.

    Task 2: Create a temporary table to store the cumulative medal count for each region, then find the top 3 regions with the highest cumulative medal count. Use nested subqueries and aggregation.

    Task 3: Insert records into a temporary table for competitors who have won at least one gold medal and participated in more than 2 different games. Use subqueries to aggregate the data.

*/

-- list all tables in the olympics schema
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'olympics';

SELECT DISTINCT gc.id
FROM games_competitor gc
JOIN 
