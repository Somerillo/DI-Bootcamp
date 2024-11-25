import psycopg2
import requests
# import json
import random

connection = psycopg2.connect(database = "countries",
                              user = "postgres",
                              password = "notapassword",
                              host = "localhost",
                              port = "5432")

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS random_countries")
create_table_query = f"""CREATE TABLE random_countries (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        capital VARCHAR(100) NOT NULL,
                        flag_code VARCHAR(100),
                        population INTEGER)"""

cursor.execute(create_table_query)
connection.commit()

countries_api = requests.get("https://restcountries.com/v3.1/all")
# print(countries_api)

data = countries_api.json()
print(type(data)) #importatnt check data type we get from the api

for i in range(10):
    country = data[i]  # Accedemos a cada país individualmente
    name = country["name"]["official"]
    capital = country["capital"][0] if "capital" in country and country["capital"] else "N/A"
    flag_code = country["flags"]["png"] if "flags" in country else "N/A"
    population = country["population"]
    # subregion = data["subregion"]

    query = """INSERT INTO random_countries (name, capital, flag_code, population)
    VALUES ('{name}'), ('{capital}'), ('{flag_code}'), ('{population}')"""
    cursor.execute(query)
connection.commit()

print("succesfully added to DB")