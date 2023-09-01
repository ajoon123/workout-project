from user_manager import UserManager

def main():
    users_filename = "users.json"
    user_manager = UserManager(users_filename)

    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            name = input("Name: ")
            age = int(input("Age: "))
            email = input("Email: ")

            if user_manager.register_user(username, password, name, age, email):
                print("Registration successful.")
            else:
                print("Username already exists.")

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")

            user = user_manager.authenticate_user(username, password)
            if user:
                print("Login successful.")
                print(user)
            else:
                print("Login failed. Incorrect username or password.")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
