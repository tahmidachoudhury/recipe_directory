from lib.recipe import Recipe
from lib.artist import Artist
import datetime

class RecipeRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM recipes')
        recipes = []
        for row in rows:
            delta = row["average_cooking_time"]
            duration = str(delta)
            recipe = Recipe(row["id"], row["name"], duration, float(row["rating"]))
            recipes.append(recipe)
        return recipes
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM recipes')
        for row in rows:
            if row['id'] == id:
                delta = row["average_cooking_time"]
                duration = str(delta)
                recipe = Recipe(row["id"], row["name"], duration, float(row["rating"]))
        return recipe

