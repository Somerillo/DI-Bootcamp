-- -- ------------------  Daily Challenge: Items and Orders  ------------------

-- -- 1- Create a table called product_orders and a table called items. You decide which fields 
-- -- should be in each table, although make sure the items table has a column called price.
-- -- 2- There should be a one to many relationship between the product_orders table and the items table. 
-- -- An order can have many items, but an item can belong to only one order. 
-- CREATE TABLE product_orders (
--     order_id SERIAL PRIMARY KEY,
--     customer_name VARCHAR(100) NOT NULL,
--     order_date DATE NOT NULL
-- );
-- SELECT * FROM product_orders;

-- CREATE TABLE items (
--     item_id SERIAL PRIMARY KEY,
--     order_id INT REFERENCES product_orders(order_id) ON DELETE CASCADE,
--     item_name VARCHAR(100) NOT NULL,
--     price NUMERIC(10, 2) NOT NULL
-- );
-- SELECT * FROM items;

-- CREATE OR REPLACE FUNCTION get_total_price(order_id  INT) -- parametro: `order_id INT` Este es el identificador del pedido para el cual se desea calcular el precio total.

-- RETURNS NUMERIC AS $$
-- DECLARE
-- 	total_price NUMERIC; -- `total_price NUMERIC` Variable que almacenará el precio total calculado
-- BEGIN
-- 	-- Se utiliza una consulta SELECT para sumar los precios de todos 
-- 	--los artículos en la tabla items que coinciden con el order_id proporcionado
-- 	-- El resultado se almacena en la variable total_price
--     SELECT SUM(price) INTO total_price
--     FROM items
--     WHERE order_id = $1;

-- 	-- Se utiliza COALESCE(total_price, 0) para devolver 0 si no hay artículos asociados
-- 	--al pedido (es decir, si la suma es NULL)
-- 	RETURN COALESCE(total_price, 0); -- Devuelve 0 si no hay artículos en el pedido
-- END;
-- $$
--  LANGUAGE plpgsql;

-- uso de la funcion
-- SELECT get_total_price(1); -- Reemplaza 1 con el order_id deseado



-- -- Bonus :
-- --     Create a table called users.
-- CREATE TABLE users (
--     user_id SERIAL PRIMARY KEY,
--     username VARCHAR(100) NOT NULL,
--     email VARCHAR(100) NOT NULL UNIQUE
-- );

-- --     There should be a one to many relationship between the users table and the product_orders table.
-- ALTER TABLE product_orders ADD COLUMN user_id INT REFERENCES users(user_id) ON DELETE CASCADE;

-- --     Create a function that returns the total price for a given order of a given user.
-- -- user_id INT: El identificador del usuario
-- -- order_id INT: El identificador del pedido
-- CREATE OR REPLACE FUNCTION get_user_order_total(user_id INT, order_id INT)
-- -- La función devuelve un valor de tipo NUMERIC, que representa el precio total del pedido del usuario
-- RETURNS NUMERIC AS $$
-- DECLARE
-- 	-- total_price NUMERIC: Variable que almacenará el precio total calculado
--     total_price NUMERIC;
-- BEGIN
-- 	-- Se utiliza una consulta SELECT que suma los precios de los artículos en la tabla items, 
-- 	-- haciendo un JOIN con la tabla product_orders para filtrar por el user_id y el order_id 
-- 	-- proporcionados.
-- 	-- El resultado se almacena en la variable total_price
--     SELECT SUM(i.price) INTO total_price
--     FROM items i
--     JOIN product_orders o ON i.order_id = o.order_id
--     WHERE o.user_id = $1 AND o.order_id = $2;

-- 	-- Se utiliza COALESCE(total_price, 0) para devolver 0 si no hay artículos asociados al pedido.
--     RETURN COALESCE(total_price, 0); -- Devuelve 0 si no hay artículos en el pedido
-- END;
-- $$
--  LANGUAGE plpgsql;

-- -- Uso de la función
-- -- Para utilizar esta función y obtener el precio total de un pedido específico de un usuario, 
-- -- puedes ejecutar una consulta como esta:
-- SELECT get_user_order_total(1, 1); -- Reemplaza 1 con el user_id y order_id deseados