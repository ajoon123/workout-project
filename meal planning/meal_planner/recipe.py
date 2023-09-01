class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        ingredients_str = "\n".join(self.ingredients)
        return f"{self.name}:\n{ingredients_str}"
