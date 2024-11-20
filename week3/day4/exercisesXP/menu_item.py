# Description: Create a restaurant menu management system for a manager. The program should allow the manager to view the menu, add an item and delete an item.


# PART 1

# In this exercise we will use PostgreSQL and Python.

#     Create a new database and a new table in pgAdmin (or in psql). The table is named Menu_Items and contains the columns
#         item_id : SERIAL PRIMARY KEY
#         item_name : VARCHAR(30) NOT NULL
#         item_price : SMALLINT DEFAULT 0

#     In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.

#     Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the Menu_Items table.
# The update method can update the name as well as the price of an item.

#     In the file menu_manager.py, create a new class called MenuManager
#         Create a Class Method called get_by_name that will return a single item from the Menu_Items table depending on it’s name, if an object is not found (there is no item matching the name in the get_by_name method) return None.

#         Create a Class Method called all_items which will return a list of all the items from the Menu_Items table.


# Codebox:

# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuManager.get_by_name('Beef Stew')
# items = MenuManager.all()

import psycopg2

# configure database
DB_CONFIG = {
    "database": "RestaurantMenuManager",
    "user": "postgres",
    "password": "postgres_password",
    "host": "localhost",
    "port": "5432"
}


class MenuItem:
    def __init__(self, name: str, price: float, item_id: int = None):
        self.name = name.lower()
        self.price = round(price, 2)  # two decimal places
        self.item_id = item_id

    def _connect(self):
        """
        internal variable to stablish a connection to the database
        without this we have to define the database on each method
        """
        return psycopg2.connect(
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"]
        )

    def save(self):
        """
        saves a new item in the DB, return the item ID
        """
        connection = self._connect()
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO Menu_Items (item_name, item_price)
                        VALUES (%s, %s)
                        RETURNING item_id;
                        """,
                        (self.name, self.price)
                    )
                    self.item_id = cursor.fetchone()[0]
                    print(f"item saved with ID: {self.item_id}")
                    return self.item_id
        finally:
            connection.close()  # release resources

    def delete(self):
        """
        deletes item based on its ID
        """
        if not self.item_id:
            print("item ID is required to delete item")
            return
        connection = self._connect()
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        DELETE FROM Menu_Items
                        WHERE item_id = %s;
                        """,
                        (self.item_id,)  # its passed as a tuple
                    )
                    print(f"item id: {self.item_id} has been removed from database")
        finally:
            connection.close()  # release resources

    def update(self, new_name: str, new_price: float):
        """
        updates name & price of an item based on its ID
        """
        if not self.item_id:
            print("item ID is required to update item")
            return
        connection = self._connect()
        try:
            with connection:
                with connection.cursor() as cursor:
                    rounded_price = round(new_price, 2) # only two decimal places

                    cursor.execute(
                        """
                        UPDATE Menu_Items
                        SET item_name = %s, item_price = %s
                        WHERE item_id = %s;
                        """,
                        (new_name, rounded_price, self.item_id)
                    )
                    self.name = new_name
                    self.price = rounded_price
                    print(f"item id: {self.item_id} has been updated to {new_name} with {new_price}")
        finally:
            connection.close()  # release resources


# # testing.....
# # create new item and save it
# item = MenuItem('Lomito', 35.50)
# item_id = item.save()

# # show item id
# print(f"Ítem guardado con ID: {item_id}")

# # update item
# item.update('Veggie Burger', 37.75)

# # delete item
# item.delete()