/*
Exercise 2: students table
Instructions

Continuation of the Day1 Exercise XPGold : students table


Update

1. ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
2. Change the last_name of David from ‘Grez’ to ‘Guez’.
*/
-- UPDATE students
-- SET birth_date = '1998-11-02'
-- WHERE (first_name = 'Lea' AND last_name = 'Benichou') 
--    OR (first_name = 'Marc' AND last_name = 'Benichou');

-- UPDATE students
-- SET last_name = 'Guez'
-- WHERE first_name = 'David' AND last_name = 'Grez';

/*
Delete

Delete the student named ‘Lea Benichou’ from the table.
*/
-- DELETE FROM students
-- WHERE first_name = 'Lea' AND last_name = 'Benichou';

-- SELECT * FROM students
-- WHERE first_name = 'Lea' AND last_name = 'Benichou';

/*
Count

    Count how many students are in the table.
    Count how many students were born after 1/01/2000.
*/
-- SELECT COUNT(*) AS total_students
-- FROM students;

-- SELECT COUNT(*) AS total_students
-- FROM students
-- WHERE birth_date > '2000-01-01';

/*
Insert / Alter
*/
-- 1. Add a column to the student table called math_grade.
-- ALTER TABLE students
-- ADD COLUMN math_grade INTEGER;

-- 2. Add 80 to the student which id is 1.
-- UPDATE students
-- SET math_grade = 80
-- WHERE id = 1;

-- 3. Add 90 to the students which have ids of 2 or 4.
-- UPDATE students
-- SET math_grade = 90
-- WHERE id IN (2, 4);

-- 4. Add 40 to the student which id is 6.
-- UPDATE students
-- SET math_grade = 40
-- WHERE id = 6;

-- 5. Count how many students have a grade bigger than 83 
-- SELECT COUNT(*) AS total_students
-- FROM students
-- WHERE math_grade > 83;

-- 6. Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70
-- SELECT birth_date 
-- FROM students 
-- WHERE first_name = 'Omer' AND last_name = 'Simpson';

-- INSERT INTO students (first_name, last_name, birth_date, math_grade)
-- VALUES ('Omer', 'Simpson', '1980-10-03', 70);

-- 7. Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam. 
-- SELECT *
-- FROM students
-- WHERE first_name = 'Omer' AND last_name = 'Simpson';

/*
Bonus: Count how many grades each student has.

Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
Tip : Use an alias called total_grade to fetch the grades.
Hint : Use GROUP BY.
*/
-- SELECT
-- 	first_name, last_name, COUNT(math_grade) AS total_grade
-- FROM
-- 	students
-- GROUP BY
-- 	first_name, last_name;

/*
SUM

Find the sum of all the students grades.
*/
-- SELECT SUM(math_grade) AS total_grades
-- FROM students;

-- ##################################################################
-- ##################################################################

/*
Exercise 3 : Items and customers
Instructions

We will work on the public database that we created yesterday.

Part I

Create a table named purchases. It should have 3 columns :
	id : the primary key of the table
	customer_id : this column references the table customers
	item_id : this column references the table items
	quantity_purchased : this column is the quantity of items purchased by a certain customer
*/
-- CREATE TABLE purchases (
--     id SERIAL PRIMARY KEY, -- Primary key for the table
--     customer_id INT NOT NULL, -- Foreign key referencing customers table
--     item_id INT NOT NULL, -- Foreign key referencing items table
--     quantity_purchased INT NOT NULL CHECK (quantity_purchased > 0), -- Quantity purchased must be positive
--     CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers (customer_id) ON DELETE CASCADE,
--     CONSTRAINT fk_item FOREIGN KEY (item_id) REFERENCES items (item_id) ON DELETE CASCADE
-- );

/*
Insert purchases for the customers, use subqueries:

    Scott Scott bought one fan
    Melanie Johnson bought ten large desks
    Greg Jones bougth two small desks
*/
-- Insert: Scott Scott bought one fan
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (
--     (SELECT customer_id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'),
--     (SELECT item_id FROM items WHERE item_name = 'Fan'),
--     1
-- );

-- melanie is not in the customers!!!
-- SELECT * FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson';

-- -- insert melanie
-- INSERT INTO customers (customer_id, first_name, last_name)
-- VALUES (DEFAULT, 'Melanie', 'Johnson');

-- -- Insert: Melanie Johnson bought ten large desks
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (
--     (SELECT customer_id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
--     (SELECT item_id FROM items WHERE item_name = 'Large Desk'),
--     10
-- );

-- -- Insert: Greg Jones bought two small desks
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (
--     (SELECT customer_id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
--     (SELECT item_id FROM items WHERE item_name = 'Small Desk'),
--     2
-- );

-- SELECT * FROM purchases;

/*
Part II

Use SQL to get the following from the database:

    All purchases. Is this information useful to us?
    All purchases, joining with the customers table.
    Purchases of the customer with the ID equal to 5.
    Purchases for a large desk AND a small desk
*/
-- All purchases. Is this information useful to us?
-- SELECT * FROM purchases;

-- Is this information useful?
-- This query returns all rows from the purchases table, 
-- which includes id, customer_id, item_id, and quantity_purchased. 
-- While this provides raw data, it lacks context 
-- (e.g., customer names or item names). To make it more meaningful, 
-- joining with other tables is recommended.

-- All purchases, joining with the customers table.
-- SELECT 
--     p.id AS purchase_id,
--     c.first_name AS customer_first_name,
--     c.last_name AS customer_last_name,
--     p.item_id,
--     p.quantity_purchased
-- FROM 
--     purchases p
-- JOIN 
--     customers c ON p.customer_id = c.customer_id;


-- -- Purchases of the customer with the ID equal to 5.
-- SELECT 
--     p.id AS purchase_id,
--     c.first_name AS customer_first_name,
--     c.last_name AS customer_last_name,
--     i.item_name AS item_name,
--     p.quantity_purchased
-- FROM 
--     purchases p
-- JOIN 
--     customers c ON p.customer_id = c.customer_id
-- JOIN 
--     items i ON p.item_id = i.item_id
-- WHERE 
--     p.customer_id = 5;

-- -- Purchases for a large desk AND a small desk
-- SELECT 
--     c.first_name AS customer_first_name,
--     c.last_name AS customer_last_name,
--     i.item_name AS item_name,
--     p.quantity_purchased
-- FROM 
--     purchases p
-- JOIN 
--     customers c ON p.customer_id = c.customer_id
-- JOIN 
--     items i ON p.item_id = i.item_id
-- WHERE 
--     i.item_name IN ('Large Desk', 'Small Desk')
-- GROUP BY 
--     c.customer_id, i.item_name, c.first_name, c.last_name, p.quantity_purchased
-- HAVING 
--     COUNT(DISTINCT i.item_name) = 2;

/*
Use SQL to show all the customers who have made a purchase. Show the following fields/columns:

    Customer first name
    Customer last name
    Item name
*/
-- SELECT 
--     c.first_name AS customer_first_name,
--     c.last_name AS customer_last_name,
--     i.item_name AS item_name
-- FROM 
--     purchases p
-- INNER JOIN 
--     customers c ON p.customer_id = c.customer_id
-- INNER JOIN 
--     items i ON p.item_id = i.item_id;

/*
Add a row which references a customer by ID, but does not 
reference an item by ID (leave it blank). Does this work? Why/why not?
*/
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (
--     1, -- Assuming customer with ID 1 exists
--     NULL, -- No item referenced
--     3 -- Quantity purchased
-- );
-- the item_id column in the purchases table has a NOT NULL constraint 
-- or if there is a foreign key constraint referencing the items table.