from fitness_tracker import FitnessTracker

def main():
    user_profiles_filename = "user_profiles.json"

    fitness_tracker = FitnessTracker(user_profiles_filename)

    for user in fitness_tracker.user_profiles:
        print(user)
        print("Measurements:")
        for measurement in user.measurements:
            print(f"Date: {measurement.date}, Weight: {measurement.weight} kg, Body Fat: {measurement.body_fat}%")
        print()

if __name__ == " __main__ ":
    main()