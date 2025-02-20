from auth_service import AuthService

def main():
    auth_service = AuthService()
    
    while True:
        command = input("Enter 'login' to authenticate or 'exit' to quit: ")
        
        if command.lower() == "exit":
            break
        elif command.lower() == "login":
            username = input("Enter username: ")
            password = input("Enter password: ")
            
            if auth_service.login(username, password):
                print("You are now logged in")
            else:
                print("Invalid username or password")
        else:
            print("Invalid command")

    auth_service.close_connection()

if __name__ == "__main__":
    main()
