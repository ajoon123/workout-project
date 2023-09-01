import json

def load_users_from_file(filename):
    with open(filename, "r") as file:
        users_data = json.load(file)
    return users_data
