class FitnessAI:
    def __init__(self):
        pass

    def recommend_exercise(self, user, exercise_list):
        recommended_erercise = None

        if user.weight > 70:
            recommended_erercise = [exercise for exercise in exercise_list if exercise.difficulty == "Intermediate"]
        else:
            recommended_exercise = [exercise for exercise in exercise_list if exercise.difficulty == "Beginner"]
        return recommended_exercise   