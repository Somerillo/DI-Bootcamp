-- Instructions

-- Description: Create a restaurant menu management system for a manager. The program should allow the manager to view the menu, add an item and delete an item.


-- PART 1

-- In this exercise we will use PostgreSQL and Python.

--     Create a new database and a new table in pgAdmin (or in psql). The table is named Menu_Items and contains the columns
--         item_id : SERIAL PRIMARY KEY
--         item_name : VARCHAR(30) NOT NULL
--         item_price : SMALLINT DEFAULT 0

--     In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.

--     Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the Menu_Items table. The update method can update the name as well as the price of an item.

--     In the file menu_manager.py, create a new class called MenuManager
--         Create a Class Method called get_by_name that will return a single item from the Menu_Items table depending on it’s name, if an object is not found (there is no item matching the name in the get_by_name method) return None.

--         Create a Class Method called all_items which will return a list of all the items from the Menu_Items table.

CREATE TABLE Menu_Items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL,
    item_price SMALLINT DEFAULT 0
);

SELECT * FROM Menu_Items;