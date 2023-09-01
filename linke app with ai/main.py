from fitness_tracker import FitnessTracker

def main():
    exercise_filename = "data/exercises.json"
    user_profiles_filename = "data/user_profiles.json"

    fitness_tracker = FitnessTracker(exercise_filename, user_profiles_filename)

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
