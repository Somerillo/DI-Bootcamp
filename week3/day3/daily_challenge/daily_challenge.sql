-- -- --------------------- Part I ---------------------

-- -- Create 2 tables : Customer and Customer profile. They have a One to One relationship.

-- --     A customer can have only one profile, and a profile belongs to only one customer
-- --     The Customer table should have the columns : id, first_name, last_name NOT NULL
-- --     The Customer profile table should have the columns : id, isLoggedIn DEFAULT false
-- -- (a Boolean), customer_id (a reference to the Customer table)
-- CREATE TABLE Customer (
-- 	id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50),
-- 	last_name VARCHAR(50) NOT NULL
-- );
-- SELECT * FROM Customer

-- CREATE TABLE CustomerProfile (
-- 	id SERIAL PRIMARY KEY,
-- 	isLoggedIn BOOLEAN DEFAULT FALSE, -- a boolean false by default
-- 	customer_id INT UNIQUE REFERENCES Customer (id) -- one to one reference to the Customer table, there cant be duplicates 
-- );
-- SELECT * FROM CustomerProfile


-- -- Insert those customers
-- --     John, Doe
-- --     Jerome, Lalu
-- --     Lea, Rive
-- INSERT INTO Customer (first_name, last_name) VALUES ('John', 'Doe');
-- INSERT INTO Customer (first_name, last_name) VALUES ('Jerome', 'Lalu');
-- INSERT INTO Customer (first_name, last_name) VALUES ('Lea', 'Rive');
-- SELECT * FROM Customer


-- -- Insert those customer profiles, use subqueries
-- --     John is loggedIn
-- --     Jerome is not logged in
-- INSERT INTO CustomerProfile (isLoggedIn, customer_id)
-- VALUES
-- 	(TRUE, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')), -- AND last_name not so necessary i think...
-- 	(FALSE, (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu')); -- anyway, using subqueries we use the other table id
-- SELECT * FROM CustomerProfile


-- -- Use the relevant types of Joins to display:
-- --	The first_name of the LoggedIn customers
-- SELECT
-- 	c.first_name
-- FROM
-- 	Customer c
-- JOIN
-- 	CustomerProfile cp ON c.id = cp.customer_id
-- WHERE
-- 	cp.isLoggedIn = TRUE;

-- --	All the customers first_name and isLoggedIn columns - even the customers those 
-- --	who don’t have a profile.
-- SELECT
-- 	-- c.first_name, cp.isLoggedIn AS isLoggedIn -- this doesnt work for those without profile 
-- 	c.first_name, COALESCE(cp.isLoggedIn, FALSE) AS isLoggedIn -- shows FALSE if customer hasnt a profile
-- FROM
-- 	Customer c
-- LEFT JOIN
-- 	CustomerProfile cp ON c.id = cp.customer_id;

-- --	The number of customers that are not LoggedIn
-- SELECT
-- 	COUNT(*)
-- FROM
-- 	Customer c
-- LEFT JOIN -- take all customers, even without profile, and again apply COALESCE
-- 	CustomerProfile cp ON c.id = cp.customer_id
-- WHERE
-- 	COALESCE(cp.isLoggedIn, FALSE) = FALSE




-- -- --------------------- Part II ---------------------

-- -- Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, 
-- -- title NOT NULL, author NOT NULL
-- CREATE TABLE Book (
-- 	book_id SERIAL PRIMARY KEY,
-- 	title TEXT NOT NULL,
-- 	author VARCHAR(120) NOT NULL
-- );
-- SELECT * FROM BOOK;


-- -- Insert those books :
-- --     Alice In Wonderland, Lewis Carroll
-- --     Harry Potter, J.K Rowling
-- --     To kill a mockingbird, Harper Lee
-- INSERT INTO Book (title, author) VALUES
-- 	('Alice In Wonderland', 'Lewis Carroll'),
--     ('Harry Potter', 'J.K Rowling'),
--     ('To kill a mockingbird', 'Harper Lee');
-- SELECT * FROM BOOK;


-- -- Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY,
-- -- name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);
-- CREATE TABLE Student (
-- 	student_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(120) NOT NULL UNIQUE,
-- 	age INT CHECK (age < 16) -- age is never bigger than 15
-- );
-- SELECT * FROM Student;


-- -- Insert those students:
-- --     John, 12
-- --     Lera, 11
-- --     Patrick, 10
-- --     Bob, 14
-- INSERT INTO Student (name, age) VALUES
-- 	('John', 12),
-- 	('Lera', 11),
-- 	('Patrick', 10),
-- 	('Bob', 14);
-- SELECT * FROM Student;


-- -- Create a table named Library, with the columns :
-- --     book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- --     student_id ON DELETE CASCADE ON UPDATE CASCADE
-- --     borrowed_date
-- --     This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- --     book_fk_id is a Foreign Key representing the column book_id from the Book table
-- --     student_fk_id is a Foreign Key representing the column student_id from the Student table
-- --     The pair of Foreign Keys is the Primary Key of the Junction Table
-- CREATE TABLE Library (
-- 	book_fk_id INT REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE, -- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- 	student_fk_id INT REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE, -- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- 	borrowed_date DATE,
-- 	PRIMARY KEY (book_fk_id, student_fk_id) -- The pair of Foreign Keys is the Primary Key of the Junction Table
-- );
-- SELECT * FROM Library;


-- -- Add 4 records in the junction table, use subqueries.
-- --     the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- --     the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- --     the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- --     the student named Bob, borrowed the book Harry Potter the on 12/08/2021
-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES 
--     ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), 
--      (SELECT student_id FROM Student WHERE name = 'John'), 
--      '2022-02-15'),
     
--     ((SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'), 
--      (SELECT student_id FROM Student WHERE name = 'Bob'), 
--      '2021-03-03'),
     
--     ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), 
--      (SELECT student_id FROM Student WHERE name = 'Lera'), 
--      '2021-05-23'),
     
--     ((SELECT book_id FROM Book WHERE title = 'Harry Potter'), 
--      (SELECT student_id FROM Student WHERE name = 'Bob'), 
--      '2021-08-12');
-- SELECT * FROM Library;


-- -- Display the data
-- --     Select all the columns from the junction table
-- SELECT * FROM Library;

-- --     Select the name of the student and the title of the borrowed books
-- SELECT
-- 	s.name AS student_name,
-- 	b.title AS book_title
-- FROM
-- 	Library l
-- JOIN
-- 	Student s ON l.student_fk_id = s.student_id
-- JOIN
-- 	Book b ON l.book_fk_id = b.book_id;

-- --     Select the average age of the children, that borrowed the book Alice in Wonderland
-- SELECT
-- 	AVG(s.age) AS average_age
-- FROM
-- 	Library l
-- JOIN
-- 	Student s ON l.student_fk_id = s.student_id
-- WHERE
-- 	l.book_fk_id = (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland');

-- --     Delete a student from the Student table, what happened in the junction table ?
-- SELECT * FROM Student;
-- SELECT * FROM Library;
-- DELETE FROM Student WHERE name = 'John'; -- student_id = 1
-- SELECT * FROM Student;
-- SELECT * FROM Library; -- we removed John`s register from Library because INT REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE