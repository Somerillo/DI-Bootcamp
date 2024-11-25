import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('HOSTNAME')
DB_NAME = os.getenv('DATABASE')
DB_USER = os.getenv('USER')
DB_PASSWORD = os.getenv('PASSWORD')
DB_PORT = os.getenv('PORT')

conn = psycopg2.connect(database = DB_NAME,
                              user = DB_USER,
                              password = DB_PASSWORD,
                              host = DB_HOST,
                              port = DB_PORT)


cursor = conn.cursor()

class MenuItem:
    def __init__(self, name, price = 0):
        self.name = name
        self.price = price
        
    def save(self):
        query = "INSERT INTO menu_items (item_name, item_price) VALUES ( '%s', '%s' )" %(self.name, self.price)
        cursor.execute(query)
        conn.commit()

    def delete(self):
        query = "DELETE FROM menu_items WHERE item_name = %s" %(self.name)
        cursor.execute(query)
        conn.commit()

    def updated(self, new_name, new_price):
        new_name = new_name.lower()
        query = "UPDATE menu_items SET item_name = %s, item_price = %s, WHERE item_name = %s" 
        cursor.execute(query, (new_name, new_price, self.name))
        conn.commit()

hamburger = MenuItem('burger', 69)
hamburger.save()

pizza = MenuItem('pizza', 69)
pizza.save()

milkshake = MenuItem('milkshake', 69)
milkshake.save()

pizza.updated("kids pizza", 35)