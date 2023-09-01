class User:
    def __init__(self, username, age, weight, height):
        self.username = username
        self.age = age
        self.weight = weight
        self.height = height
        self.exercise_log = {}

    def add_exercise_log(self, exercise, reps, sets):    
        if exercise.name not in self.exercise_log:
            self.exercise_log[exercise.name] = []
            self.exercise_log[exercise.name].append({"reps": reps, "sets": sets})

    def __str__(self):        
        return f"User: {self.username} (Age: {self.age}, Weight: {self.weight}, Height: {self.height})"