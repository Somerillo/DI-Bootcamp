-- RESTRICT: NOT POSSIBLE TO DELETE A RECORD THAT IS CONNECTED TO OTHER TABLE (CHILD TABLE)
-- PARENT TABLE
-- CREATE TABLE colors(
-- color_id SERIAL PRIMARY KEY,
-- color_name VARCHAR(100) NOT NULL)

-- INSERT INTO colors (color_name)
-- VALUES ('pink')
--  SELECT * FROM colors

-- CREATE TABLE cars(
-- car_id SERIAL PRIMARY KEY,
-- car_color INTEGER REFERENCES colors (color_id) ON DELETE SET DEFAULT,
-- car_name TEXT);

-- INSERT INTO cars(car_color, car_name)
-- VALUES ((SELECT color_id FROM colors WHERE color_name = 'blue'), 'Mazda')

-- SELECT * FROM colors

-- DELETE FROM colors where color_name = 'yellow';

-- ON DELETE CASCADE: allow you to delete from the parent BUT the record will be deleted also in the child

-- CREATE TABLE cars(
-- car_id SERIAL PRIMARY KEY,
-- car_color_id INT DEFAULT 7 REFERENCES colors (color_id) ON DELETE SET DEFAULT, 
-- car_name TEXT);

-- INSERT INTO cars(car_color_id, car_name)
-- VALUES 
-- ((SELECT color_id FROM colors WHERE color_name = 'yellow'), 'Ferrari');

-- DELETE FROM colors where color_name = 'yellow'

-- SELECT * FROM cars

-- SET DEFAULT: WE NEED TO DEFINE THE DEFAULT BUT IT HAS TO BE SOME VALUE THAT IS PRESENT IN THE PARENT TABLE

