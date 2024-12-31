/*
🌟 Exercise 1: Building a Comprehensive Dataset for Employee Analysis

    Create a temporary table that join all tables and create a new one using LEFT JOIN.
    Create an unique identifier code between the columns ‘employee_id’ and ‘date’ and call it ‘id’.
    Convert the column ‘date’ to DATE type because it was previously configured as TIMESTAMP.
    Transform this new table into a dataset “df_employee” for analysis.
*/
/*
DROP table if EXISTS df_employee;

CREATE TEMPORARY TABLE df_employee AS
SELECT
	s.employee_id || '_' || s.date AS id, -- concatenates {employee_id}_{date}
    s.date as month_year, -- it is already as datetype
    s.employee_id,
    s.employee_name,
    e.'GEN(M_F)' AS gender, -- column name in between ''
    e.age,
    CAST(REPLACE(s.salary, ',', '.') AS REAL) AS salary, -- replace ',' separator and transform to REAL
    f.function_code,
    f.function,
    f.function_group,
    c.company_name,
    c.company_city,
    c.company_state,
    c.company_type,
    c.const_site_category
FROM salaries s
LEFT JOIN employees e ON s.employee_id = e.employee_code_emp
left JOIN functions f ON s.func_code = f.function_code
LEFT JOIN companies c on s.comp_name = c.company_name;

SELECT * from df_employee;
*/

-------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------
/*
🌟 Exercise 2: Cleaning Data for Consistency and Quality

1. run the following SQLite request and observe your new table.
*/

-- SELECT * FROM df_employee;

/*
-- 2. Remove all unwanted spaces from all text columns using TRIM

UPDATE df_employee
SET -- specify which columns
id = TRIM(id), -- replaces inplace
employee_name = TRIM(employee_name),
gender = TRIM(gender),
function = TRIM(function),
function_group = TRIM(function_group),
company_name = TRIM(company_name),
company_city = TRIM(company_city),
company_state = TRIM(company_state),
company_type = TRIM(company_type),
const_site_category = TRIM(const_site_category);

SELECT * from df_employee;
*/

/*
3. Check for NULL values and empty values.
Note: All null cells filled with a space ' ' were trimed. So now if any, they're ''
*/

/*
SELECT *
FROM df_employee
WHERE id IS NULL OR id = ''
	OR month_year IS NULL OR month_year = ''
	OR employee_id IS NULL OR employee_id = ''
	OR employee_name IS NULL OR employee_name = ''
	OR gender IS NULL OR gender = ''
	OR age IS NULL OR age <= 0
	OR salary IS NULL OR salary = 0 -- null vals were set to 0 when fixed format
--    OR function_code IS NULL OR = '' -- doesnt apply?
	OR function IS NULL OR function = ''
	OR function_group IS NULL OR function_group = ''
	OR company_name IS NULL OR company_name = ''
	OR company_city IS NULL OR company_city = ''
	OR company_state IS NULL OR company_state = ''
	OR company_type IS NULL OR company_type = '';
--    OR const_site_category IS NULL OR const_site_category = ''; -- shouldnt be removed
*/

/*
4. Delete rows of the detected missing values.
*/
/*
DELETE FROM df_employee
WHERE salary = 0;
*/

-------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------
/*
🌟 Exercise 3 : Calculating Current Employee Counts by Company

    How many employees do the companies have today?
    Group them by company
*/
/*
SELECT
	company_name,
    COUNT(employee_id) AS employee_count
From 
	df_employee
-- WHERE
--	month_year = DATE('now') -- today there is none, that's why commented
GROUP BY
	company_name;
*/

------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------
/*
🌟 Exercise 4 : Analyzing Employee Distribution by City and Over Time

    What is the total number of employees each city? Add a percentage column
    What is the total number of employees each month?
    What is the average number of employees each month?
*/
/*
-- 1. What is the total number of employees each city? Add a percentage column
SELECT
	company_city,
    COUNT(employee_id) AS total_employees, -- tot employee column
    -- we use COUNT(*) to count all rows, regardless of wether any column contains NULL values
    (COUNT(employee_id) * 100. / (SELECT COUNT(*) from df_employee)) AS percentage -- % col
FROM
	df_employee
GROUP BY
	company_city;
*/
/*
-- 2. What is the total number of employees each month?
SELECT
	strftime('%Y-%m', 
    		 -- the format is DD/MM/YYYY hh:mm
             substr(month_year, 7, 4) || '-' || -- extract year, starts at pos 7 and takes 4 digits
             substr(month_year, 4, 2) || '-' || -- extract month, starts at pos 4 and takes 2 digits
             substr(month_year, 1, 2) -- extract day, starts at 1 and takes 2 digits
    ) AS month,
    COUNT(employee_id) AS total_employees_month
FROM
	df_employee
GROUP BY
	month;

SELECT * FROM df_employee;
*/

/*
-- 3. What is the average number of employees each month?
SELECT 
    month,
    AVG(total_employees_month) AS average_employees
FROM (
    SELECT 
        strftime('%Y-%m', 
            substr(month_year, 7, 4) || '-' ||  -- extract year
            substr(month_year, 4, 2) || '-' ||  -- extract month
            substr(month_year, 1, 2) -- extract day
        ) AS month,
        COUNT(employee_id) AS total_employees_month
    FROM 
        df_employee
    GROUP BY 
        month
)
GROUP BY 
    month;
*/

---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
/*
🌟 Exercise 5 : Analyzing Employment Trends and Salary Metrics

    What is the minimum and maximum number of employees throughout all the months? In which months were they?
    What is the monthly average number of employees by function group?
    What is the annual average salary?
*/
/*
-- 1. What is the minimum and maximum number of employees throughout all the months? In which months were they?
SELECT 
    MIN(total_employees) AS min_employees,
    MAX(total_employees) AS max_employees
FROM (
    SELECT 
        month,
        COUNT(employee_id) AS total_employees
    FROM (
        SELECT 
            strftime('%Y-%m', 
                substr(month_year, 7, 4) || '-' ||  
                substr(month_year, 4, 2) || '-' ||  
                substr(month_year, 1, 2)
            ) AS month,
            employee_id
        FROM df_employee
    )
    GROUP BY month
);

SELECT 
    month,
    COUNT(employee_id) AS total_employees_by_month
FROM (
    SELECT 
        strftime('%Y-%m', 
            substr(month_year, 7, 4) || '-' ||  
            substr(month_year, 4, 2) || '-' ||  
            substr(month_year, 1, 2)
        ) AS month,
        employee_id
    FROM df_employee
)
GROUP BY month
ORDER BY total_employees_by_month;
*/

/*
-- 2. What is the monthly average number of employees by function group?
SELECT
	function_group,
    AVG(total_employees) as average_employees
FROM(
    SELECT 
        function_group,
        strftime('%Y-%m', 
            substr(month_year, 7, 4) || '-' ||  
            substr(month_year, 4, 2) || '-' ||  
            substr(month_year, 1, 2)
        ) AS month,
        COUNT(employee_id) AS total_employees
	FROM
  		df_employee
  	GROUP BY
  		function_group, month
) -- monthly counts
GROUP BY 
    function_group
ORDER BY 
    function_group;
*/
/*
-- 3. What is the annual average salary?
SELECT 
    strftime('%Y', 
        substr(month_year, 7, 4) || '-' ||  
        substr(month_year, 4, 2) || '-' ||  
        substr(month_year, 1, 2)
    ) AS year,
    AVG(salary) AS annual_average_salary
FROM 
    df_employee
GROUP BY 
    year
ORDER BY 
    year;
*/