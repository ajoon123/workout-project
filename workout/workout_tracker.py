import json
from datetime import datetime
from exercise import Exercise
from workout import Workout

class WorkoutTracker:
    def __init__(self, filename):
        self.filename = filename

    def load_workouts(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []
        return [self.create_workout(workout) for workout in data]

    def create_workout(self, data):
        workout = Workout(data["date"])
        for exercise_data in data["exercises"]:
            exercise = Exercise(exercise_data["name"])
            for set_data in exercise_data["sets"]:
                exercise.add_set(set_data["weight"], set_data["reps"])
            workout.add_exercise(exercise)
        return workout

    def save_workout(self, workout):
        workouts = self.load_workouts()
        workouts.append(workout)
        with open(self.filename, "w") as file:
            json.dump([workout.__dict__ for workout in workouts], file, indent=4)
