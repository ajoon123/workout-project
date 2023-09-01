class Exercise:
    def __init__(self, name):
        self.name = name
        self.sets = []

    def add_set(self, weight, reps):
        self.sets.append({"weight": weight, "reps": reps})

    def __str__(self):
        sets_str = ", ".join(f"{set['weight']} lbs x {set['reps']} reps" for set in self.sets)
        return f"{self.name}: {sets_str}"
