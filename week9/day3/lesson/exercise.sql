-- Challenge : Detecting and Handling Missing Data
-- Identify missing values in a sample dataset.
-- Replace missing values using COALESCE and imputation methods.

-- identifying missing values
SELECT * FROM sample_data WHERE value IS NULL;

-- replace missing values
-- COALESCE returns the first non null value in the list
SELECT id, COALESCE(value, 'Unknown') AS value FROM sample_data;


-- replace using imputation (NOT-NULL)
WITH mode_value AS (
	SELECT MODE() WITHIN GROUP (ORDER BY value) AS mode
	FROM sample_data
	WHERE value IS NOT NULL
)
SELECT id, COALESCE(value, mode) AS value
FROM sample_data, mode_value;