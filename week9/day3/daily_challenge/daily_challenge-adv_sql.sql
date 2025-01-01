-- -- Create the employees table
-- CREATE TABLE employees (
--     employee_id INT PRIMARY KEY,
--     employee_name VARCHAR(50),
--     salary DECIMAL(10, 2),
--     hire_date VARCHAR(20),
--     department VARCHAR(50)
-- );

-- -- Insert 20 sample records 
-- INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
-- (1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
-- (2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
-- (3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
-- (4, 'John White', 90000.00, '2020-11-05', 'Finance'),
-- (5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
-- (6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
-- (7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
-- (8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
-- (9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
-- (10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
-- (11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
-- (12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
-- (13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
-- (14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
-- (15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
-- (16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
-- (17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
-- (18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
-- (19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
-- (20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

---------------------------------------------------------------------------------------------
-- 1. Identify and handle any missing value.

-- -- missing values identification
-- SELECT *
-- FROM employees
-- WHERE employee_id IS NULL
-- 	OR employee_name is NULL
-- 	OR salary IS NULL
-- 	OR hire_date IS NULL
-- 	OR department IS NULL;

-- -- missing values handling
-- UPDATE employees
-- SET department = 'not assigned'
-- WHERE department IS NULL;

---------------------------------------------------------------------------------------------
-- 2. Check for and eliminate any duplicate rows in the dataset.

-- -- check for duplicates
-- SELECT employee_name, salary, hire_date, department, COUNT(*)
-- FROM employees
-- GROUP BY employee_name, salary, hire_date, department
-- HAVING COUNT(*) > 1;

-- -- no duplicates, but in case there were uncomment below
-- DELETE FROM employees
-- WHERE eployee_id NOT IN(
-- 	SELECT MIN(employee_id) -- this MIN makes the difference
-- 	FROM employees
-- 	GROUP BY employee_name, salary, hire_date, department
-- );

---------------------------------------------------------------------------------------------
-- 3. Correct any structural issues, such as inconsistent naming conventions or formatting errors.

-- -- standarize names and dept by capitalizind 1st letter
-- UPDATE employees
-- SET employee_name = INITCAP(employee_name),
-- 	department = INITCAP(department);

---------------------------------------------------------------------------------------------
-- 4. Ensure all columns have appropriate data types (e.g. the hire_date column).

-- -- 'hire_date' is a VARCHAR type, we create a new col to replace the original
-- -- there are several reason why its better this approach
-- ALTER TABLE employees ADD COLUMN new_hire_date DATE;

-- pass the data into the new one
-- UPDATE employees
-- SET new_hire_date = TO_DATE(hire_date , 'YYYY-MM-DD');

-- -- drop old column
-- ALTER TABLE employees DROP COLUMN hire_date;

-- -- rename the new col
-- ALTER TABLE employees RENAME COLUMN new_hire_date TO hire_date;

-- -- verify names, depts standarization, cols datetype
-- SELECT * FROM employees;

---------------------------------------------------------------------------------------------
-- 5. Detect and address any outliers that may skew the analysis.

-- -- retrieve outliers with percentile_cont
-- WITH salary_stats AS (
-- 	SELECT
-- 		percentile_cont(0.25) WITHIN GROUP (ORDER BY salary) AS Q1,
-- 		percentile_cont(0.75) WITHIN GROUP (ORDER BY salary) AS Q3,
-- 		percentile_cont(0.75) WITHIN GROUP (ORDER BY salary) - 
-- 			percentile_cont(0.25) WITHIN GROUP (ORDER BY salary) AS IQR
-- 		FROM employees
-- ),
-- outliers AS (
-- 	SELECT e.*,
-- 		s.Q1 - 1.5 * s.IQR AS lower_bound,
-- 		s.Q3 + 1.5 * s.IQR AS upper_bound
-- 	FROM employees e, salary_stats s
-- 	WHERE e.salary < (s.Q1 - 1.5 *s.IQR) OR e.salary > (s.Q3 + 1.5 * s.IQR)
-- )
-- SELECT * FROM outliers;

/*
There are no outliers, if there were there we could a) remove them, 
b) cap them, c) replace them with the median, the avg, etc... Whatsoever,
any choosen method should be done inside the upper query, for 'outliers' is
a CTE and lives only while that query is running
*/


---------------------------------------------------------------------------------------------
-- 6. Standardize and normalize data where applicable to ensure consistency.

/*
-- We can plot the salary distribution by runing the query below, then setting salary_range 
-- to X-axis and employee_count to the Y-axis
SELECT 
    width_bucket(salary, 
                 (SELECT MIN(salary) FROM employees), 
                 (SELECT MAX(salary) FROM employees), 
                 10) AS salary_range,
    COUNT(*) AS employee_count
FROM 
    employees
GROUP BY 
    salary_range
ORDER BY 
    salary_range;
-- In the distribution plot we appreciate the histogram is not normal. It is important if we
-- refer to one of the two (most common) scalers:

-- * Z-score normalization when:

--     The data distribution is approximately normal
--     We want to preserve outliers effects
--     Comparing across different datasets

-- * Min-Max scaling when:

--     We need values in a specific range (e.g., 0 to 1)
--     The distribution is not Gaussian or unknown
*/

-- -- Given the data distribution we choose Min-Max
-- -- Instead of replacing values, we make a new col for scaled values

-- new col for scaled values
-- ALTER TABLE employees ADD COLUMN IF NOT EXISTS scaled_salary DECIMAL(10, 5);

-- apply min-max scaling
-- WITH min_max AS (
-- 	SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary
-- 	FROM employees
-- )
-- UPDATE employees e
-- SET scaled_salary = (e.salary - m.min_salary) / (m.max_salary - m.min_salary)
-- FROM min_max m;

-- verify
-- SELECT salary, scaled_salary
-- FROM employees
-- ORDER BY salary;