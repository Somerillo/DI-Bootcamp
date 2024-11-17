-- CREATE TABLE items (
-- item_id SERIAL PRIMARY KEY,
-- item_name VARCHAR(50) NOT NULL,
-- price DECIMAL(7,2) NOT NULL
-- );

-- Add the following items to the items table:

--     1 - Small Desk – 100 (ie. price)
--     2 - Large desk – 300
--     3 - Fan – 80

-- INSERT INTO items (item_name, price) VALUES
-- ('Small Desk', 100),
-- ('Large Desk', 300),
-- ('Fan', 80);
-- SELECT * FROM items;


-- Add 5 new customers to the customers table:

--     1 - Greg - Jones
--     2 - Sandra - Jones
--     3 - Scott - Scott
--     4 - Trevor - Green
--     5 - Melanie - Johnson

-- CREATE TABLE customers (
-- customer_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(20) NOT NULL,
-- last_name VARCHAR(20) NOT NULL
-- );

-- INSERT INTO customers (first_name, last_name) VALUES
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Jonson');

-- SELECT * FROM customers;


-- Use SQL to fetch the following data from the database:

--     All the items.
--     All the items with a price above 80 (80 not included).
--     All the items with a price below 300. (300 included)
--     All customers whose last name is ‘Smith’ (What will be your outcome?).
--     All customers whose last name is ‘Jones’.
--     All customers whose firstname is not ‘Scott’.

-- SELECT * FROM items;

-- SELECT * FROM items WHERE price > 80;

-- SELECT * FROM items WHERE price < 200;

-- SELECT * FROM customers WHERE last_name = 'Smith' -- theres no Smith so we get empty table

-- SELECT * FROM customers WHERE last_name = 'Jones'

-- SELECT * FROM customers WHERE first_name <> 'Scott'