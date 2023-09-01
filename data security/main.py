from user_manager import UserManager

def main():
    users_filename = "users.json"
    user_manager = UserManager(users_filename)

    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1": 
            print("1 Register")
            
        elif choice == "2":
            print("2 Login")
 
        elif choice == "3":
            print("3 Exit")
            break

if __name__ == "__main__":
    main()
