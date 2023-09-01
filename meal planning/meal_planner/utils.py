import json

def load_recipes_from_file(filename):
    with open(filename, "r") as file:
        recipes_data = json.load(file)
    return recipes_data
