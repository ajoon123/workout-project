class Workout:
    def __init__(self, date):
        self.date = date
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def __str__(self):
        exercises_str = "\n".join(str(exercise) for exercise in self.exercises)
        return f"Workout on {self.date}:\n{exercises_str}"

