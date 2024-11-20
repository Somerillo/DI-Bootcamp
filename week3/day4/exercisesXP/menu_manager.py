import psycopg2
from menu_item import MenuItem

# configure database
DB_CONFIG = {
    "database": "RestaurantMenuManager",
    "user": "postgres",
    "password": "postgres_password",
    "host": "localhost",
    "port": "5432"
}


class MenuManager:
    @classmethod
    def _connect(cls):  # 'cls' in the argument for we modify the class
        """
        stablish connection to the DB
        """
        return psycopg2.connect(
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"]
        )

    @classmethod
    def get_by_name(cls, name: str):
        """get item by name"""
        name = name.lower() # importante!!!
        connection = cls._connect()
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT item_id, item_name, item_price
                        FROM Menu_Items
                        WHERE item_name = %s;
                        """,
                        (name,)  # as a tuple
                    )
                    result = cursor.fetchone()
                    if result:
                        # print(f"found item: ID {result[0]}, name {result[1]}, price {result[2]}")
                        return MenuItem(result[1], result[2], result[0])
                    else:
                        print("item not found")
                        return None
        finally:
            connection.close()

    @classmethod
    def all_items(cls):
        """gets all items in the menu"""
        connection = cls._connect()  # Usar el método de conexión
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT item_id, item_name, item_price
                        FROM Menu_Items;
                        """
                    )
                    results = cursor.fetchall()
                    items = [MenuItem(row[1], row[2], row[0])
                             for row in results]
                    for item in items:
                        print(f"ID: {item.item_id}, name: {item.name}, price: {item.price}")
                    return items
        finally:
            connection.close()


# # testing

# print("all menu items:")
# MenuManager.all_items()
# print()
# print("search item by name:")
# item = MenuManager.get_by_name('Lomito')