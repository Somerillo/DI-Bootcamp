/*
Exercise 1 : Students table #2
Instructions

Continuation of the Exercise XP +
Select

For the following questions, you have to fetch the first_names, last_names and birth_dates of the students.

    Fetch the first four students. You have to order the four students alphabetically by last_name.
    Fetch the details of the youngest student.
    Fetch three students skipping the first two students.
*/

/* Fetch the first four students. You have to order the answer by last_name alphabetically. */
-- SELECT first_name, last_name, birth_date
-- FROM students
-- WHERE id <= 4
-- ORDER BY last_name;

/* Fetch the birth_date of the youngest student. */
-- SELECT first_name, last_name, birth_date
-- FROM students
-- ORDER BY birth_date DESC
-- LIMIT 1;

/* Fetch three students, skipping the first two students. */
-- SELECT first_name, last_name, birth_date
-- FROM students
-- OFFSET 2
-- LIMIT 3;