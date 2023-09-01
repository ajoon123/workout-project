from exercise import Exercise
from workout_tracker import WorkoutTracker

def main():
    filename = "workouts.json"

    workout_tracker = WorkoutTracker(filename)

    new_workout = workout("2023-08-30")
    squat = Exercise("Squats")
    squat.add_set(135, 8)
    squat.add_set(185, 6)
    bench_press = Exercise("Bench Press")
    bench_press.add_set(135, 10)
    bench_press.add_set(185, 5)
    new_workout.add_exercise(squat)
    new_workout.add_exercise(bench_press)

    workout_tracker.save_workout(new_workout)

    workouts = workout_tracker.load_workouts()
    for workout in workouts:
        print(workout)

if __name__ == "__main__":
    main()
