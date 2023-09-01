class User:
    def __init__(self, username, name, age, height, weight, goals, measurements):
        self.username = username
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.goals = goals
        self.measurements = measurements

    def __str__(self):
        return f"User: {self.username} ({self.name}), Age: {self.age}, Height: {self.height} cm, Weight: {self.weight} kg"

class Measurement:
    def __init__(self, date, weight, body_fat):
        self.date = date
        self.weight = weight
        self.body_fat = body_fat
