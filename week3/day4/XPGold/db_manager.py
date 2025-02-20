import psycopg2
from config import DB_CONFIG

class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cur = self.conn.cursor()
        self._create_users_table()

    def _create_users_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(50) PRIMARY KEY,
                password VARCHAR(50) NOT NULL
            )
        """)
        self.conn.commit()

    def insert_user(self, username, password):
        self.cur.execute("INSERT INTO users (username, password) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING", (username, password))
        self.conn.commit()

    def check_credentials(self, username, password):
        self.cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        return self.cur.fetchone() is not None

    def close(self):
        self.cur.close()
        self.conn.close()