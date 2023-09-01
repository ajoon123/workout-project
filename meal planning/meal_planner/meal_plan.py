import random
from utils import load_recipes_from_file
from recipe import Recipe

class MealPlanner:
    def __init__(self, recipes_filename):
        self.recipes = self.load_recipes(recipes_filename)

    def load_recipes(self, recipes_filename):
        recipes_data = load_recipes_from_file(recipes_filename)
        recipes = [Recipe(recipe["name"], recipe["ingredients"]) for recipe in recipes_data]
        return recipes

    def generate_meal_plan(self, days):
        meal_plan = {}
        for _ in range(days):
            recipe = random.choice(self.recipes)
            meal_plan[self.get_day_of_week()] = recipe
        return meal_plan

    def get_day_of_week(self):
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return random.choice(days_of_week)
