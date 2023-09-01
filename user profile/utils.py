import json

def load_user_profiles_from_file(filename):
    with open(filename, "r") as file:
        user_profiles_data = json.load(file)
    return user_profiles_data

def save_user_profiles_to_file(filename, user_profiles):
    with open(filename, "w") as file:
        json.dump(user_profiles, file, indent=4)
