-- Use a CASE statement to standardize the status column
-- Update the date column to replace the hyphen '-' with a forward slash '/'.
-- Add a CHECK constraint to the exercise_data table to ensure that the value column is greater than 0.
-- Create a trigger named validate_value that fires before an INSERT operation on the exercise_data table. The trigger should validate that the value column is greater than 0. If the value is less than or equal to 0, the trigger should raise an error.



-- CREATE TABLE exercise_data (
--     id INT,
--     date VARCHAR(50),
--     value INT,
--     status VARCHAR(10)
-- );

-- INSERT INTO exercise_data (id, date, value, status) VALUES
-- (1, '2021-01-01', 10, 'A'),
-- (2, '2021-01-02', NULL, 'I'),
-- (3, '2021-01-03', -5, 'A'),
-- (4, '2021-01-04', 20, 'X');


-- -- 1. Standardize the status column using a CASE statement

-- UPDATE exercise_data
-- SET status = CASE
--     WHEN status = 'A' THEN 'Active'
--     WHEN status = 'I' THEN 'Inactive'
--     ELSE 'Unknown'
-- END;



-- -- 2. update column format

-- UPDATE exercise_data
-- SET date = REGEXP_REPLACE(date, '-', '/');
SELECT * FROM exercise_data;


-- 3. add CHECK constraint
-- -- SELECT * FROM exercise_data;
-- ALTER TABLE exercise_data
-- ADD CONSTRAINT positive_value CHECK (value > 0);