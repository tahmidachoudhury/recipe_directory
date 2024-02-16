from lib.recipe import Recipe

"""
Recipe constructs with an id, name, average cooking time and rating
"""
def test_constructs_recipe():
    recipe = Recipe(1, "chicken soup", "20 minutes", 3.0)
    assert recipe.id == 1
    assert recipe.name == "chicken soup"
    assert recipe.time == "20 minutes"
    assert recipe.rating == 3.0