import json

def load_posts_from_file(filename):
    with open(filename, "r") as file:
        posts_data = json.load(file)
    return posts_data
