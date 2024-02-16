from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
when .all() is called on recipe repository, 
it returns a list of album objects
in the same format as the seed data.
"""

def test_get_all_recipes(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = RecipeRepository(db_connection) # Create a new RecipeRepository

    recipes = repository.all() # Get all recipes

    # Assert on the results
    assert recipes == [
        Recipe(1, "Spaghetti Carbonara", '0:30:00', 4.0),
        Recipe(2, 'Beef Stew', '4:00:00', 3.2),
        Recipe(3, 'Roast Chicken', '2:30:00', 3.8),
        Recipe(4, 'Lamb & Beef Lasanga', '2:00:00', 4.5),
        Recipe(5, 'Bengali Chicken Curry', '1:15:00', 5.0),
    ]

"""
The .find() should be able to retrieve one recipe
given the id as the argument - it should return a 
single recipe that matches the id.
"""
def test_get_one_recipe(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(1)
    assert recipe == Recipe(1, "Spaghetti Carbonara", '0:30:00', 4.0)

def test_get_beef_stew(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(2)
    assert recipe == Recipe(2, "Beef Stew", '4:00:00', 3.2)

def test_get_chicken_curry(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(5)
    assert recipe == Recipe(5, "Bengali Chicken Curry", '1:15:00', 5.0)