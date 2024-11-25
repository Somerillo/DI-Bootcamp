
    # Using this REST Countries API, create the functionality which will write 10 random countries to your database.

    # These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.


import psycopg2
import requests
import random

# connect to DB
connection = psycopg2.connect(database="countries",
                              user="postgres",
                              password="password",
                              host="localhost",
                              port="5432")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS random_countries") # drop if exists... duh
create_table_query = f"""CREATE TABLE random_countries (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(120) NOT NULL,
                        capital VARCHAR(120) NOT NULL,
                        flag_code VARCHAR(100),
                        population INTEGER,
                        subregion VARCHAR(100))"""
cursor.execute(create_table_query)
connection.commit()

# get data from api rest
response = requests.get("https://restcountries.com/v3.1/all")
countries = response.json()

# 10 random countries
random_countries = random.sample(countries, 10)

# insert countries in DB
for country in random_countries:
    try:
        name = country['name']['official']
    except:
        name = country['name']['official'][0]
    name = name.replace('\'', '`')
    capital = country['capital'][0] if "capital" in country and country["capital"] else "N/A"
    capital = capital.replace('\'', '`')
    flag_code = country['flag'] #['png'] if 'flags' in country else "no data" # Flagpedia links to svg and png flags
    population = country['population']
    subregion = country['subregion'] if 'subregion' in country else "No data"

    insert_query = """
    INSERT INTO random_countries (name, capital, flag_code, population, subregion)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (name, capital, flag_code, population, subregion))

# confirm changes
connection.commit() # start connection
cursor.execute("SELECT * FROM random_countries")
rows = cursor.fetchall()
print("the random inserted countries are:")
for row in rows:
    print(f"{row[0]}- {row[1]}; capital: {row[2]}; flag code: {row[3]}; pop: {row[4]}; subregion: {row[5]}")

# close connection, important!!!! open connection means unused resources
cursor.close()
connection.close()