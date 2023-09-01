from meal_plan import MealPlanner

def main():
    recipes_filename = "recipes.json"
    days = 5

    meal_planner = MealPlanner(recipes_filename)
    meal_plan = meal_planner.generate_meal_plan(days)

    print("Meal Plan:")
    for day, recipe in meal_plan.items():
        print(f"{day}: {recipe.name}")

if __name__ == "__main__":
    main()
