-- CREATE TABLE FirstTab ( -- we create FirstTab table
--      id integer, -- id is an integer
--      name VARCHAR(10) -- this is a string of length 10
-- ) 

-- INSERT INTO FirstTab VALUES -- we add 4 names and 'Avtaar' doesnt have an id
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar');

-- SELECT * FROM FirstTab -- with this we visualize both two fields from FirstTab table

-- CREATE TABLE SecondTab ( -- now we create a 2nd table with only one numeric field
--     id integer 
-- );

-- INSERT INTO SecondTab VALUES -- insert one id number and create a 2nd one NULL
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab -- with this we visualize the only field from SecondTab table



-- -- -- -- -- -- -- -- -- -- -- -- QUESTIONS & ANSWERS
-- -- Q1. What will be the OUTPUT of the following statement?
-- -- ANS: the subquery returns the NULL elements in SecondTab, which are not in FirstTab
-- -- so then we have the count of the empty set
-- SELECT COUNT(*) -- this aggregate command counts every row
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )



-- -- Q2. What will be the OUTPUT of the following statement?
-- -- ANS: NOT IN ( id = 5 ) is for FirstTab the rows for id = [6, 7, NULL].
-- -- But comparations with NULL never return True. Then we count only 2 rows
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );


-- -- Q3. What will be the OUTPUT of the following statement?
-- -- ANS: in the subquery we are taking a NULL value, then we evaluate it with the FirstTab
-- -- table and returning empty set. I get it, we must avoid NULL values
-- SELECT COUNT(*)
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );

-- -- Q4. What will be the OUTPUT of the following statement?
-- -- ANS: In the subquery we take only id=5, then we choose NOT that one from FirstTab. That
-- -- leave us with id = [6, 7, NULL]... but, again, we are evaluating NULL then it is not counted and
-- -- we count only two elements which are id = [6, 7]
-- SELECT COUNT(*)
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )