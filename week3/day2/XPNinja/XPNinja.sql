/*
Exercise 1 : Bonus Public Database (Continuation of XP)
*/

-- 1. Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
-- SELECT first_name, last_name
-- FROM customers
-- ORDER BY last_name, first_name
-- LIMIT 2;



-- 2. Use SQL to delete all purchases made by Scott.
-- DELETE FROM purchases
-- WHERE customer_id = (
--     SELECT customer_id 
--     FROM customers 
--     WHERE first_name = 'Scott' AND last_name = 'Scott'
-- );



-- 3. Does Scott still exist in the customers table, even though he has been deleted? Try and find him.
-- SELECT *
-- FROM customers
-- WHERE first_name = 'Scott' AND last_name = 'Scott';
-- Scott will still exist in the customers table because deleting
-- his purchases only affects the purchases table. Unless a cascading 
-- delete is explicitly defined on the foreign key relationship between
-- purchases.customer_id and customers.customer_id, deleting rows in the
-- purchases table does not delete corresponding rows in the customers table.



-- 4. Use SQL to find all purchases. Join purchases with the customers table,
-- so that Scott’s order will appear, although instead of the customer’s first
-- and last name, you should only see empty/blank. (Which kind of join should 
-- you use?).
-- SELECT 
--     COALESCE(c.first_name, '') AS customer_first_name,
--     COALESCE(c.last_name, '') AS customer_last_name,
--     p.item_id,
--     p.quantity_purchased
-- FROM 
--     purchases p
-- LEFT JOIN 
--     customers c ON p.customer_id = c.customer_id;

-- The COALESCE(c.first_name, '') and COALESCE(c.last_name, '')
-- replace NULL values with empty strings (''). This ensures that if 
-- a customer is missing (e.g., Scott has been deleted), their name 
-- fields will show as blank instead of NULL.



-- 5. Use SQL to find all purchases. Join purchases with the customers table,
-- so that Scott’s order will NOT appear. (Which kind of join should you use?)
-- SELECT 
--     c.first_name AS customer_first_name,
--     c.last_name AS customer_last_name,
--     p.item_id,
--     p.quantity_purchased
-- FROM 
--     purchases p
-- INNER JOIN 
--     customers c ON p.customer_id = c.customer_id;

-- An INNER JOIN only includes rows where there is a match between the 
-- purchases table and the customers table.
-- If Scott has been deleted from the customers table, his customer_id will
-- no longer have a match in the customers table, and his orders will be 
-- excluded from the results.