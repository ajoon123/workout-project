class Exercise:
    def __init__(self, name, muscle_group, difficulty):
        self.name = name
        self.muscle_group = muscle_group
        self.difficult = difficulty

    def __str__(self):    
        return f"{self.name} ({self.muscle_group}, {self.difficult})"