from db_manager import DBManager

class AuthService:
    def __init__(self):
        self.db_manager = DBManager()
        self._initialize_users()
        self.logged_in = None

    def _initialize_users(self):
        users = {
            "alice": "password123",
            "bob": "securepass",
            "charlie": "qwerty"
        }
        for username, password in users.items():
            self.db_manager.insert_user(username, password)

    def login(self, username, password):
        if self.db_manager.check_credentials(username, password):
            self.logged_in = username
            return True
        return False

    def close_connection(self):
        self.db_manager.close()