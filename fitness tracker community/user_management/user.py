class User:
    def __init__(self, username, name, age, height, weight, followers, following, posts):
        self.username = username
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.followers = followers
        self.following = following
        self.posts = posts

    def __str__(self):
        return f"User: {self.username} ({self.name}), Age: {self.age}, Height: {self.height} cm, Weight: {self.weight} kg"
