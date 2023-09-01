import json

def load_user_profiles_from_file(filename):
    with open(filename, "r") as file:
        user_profiles_data = json.load(file)
        return user_profiles_data