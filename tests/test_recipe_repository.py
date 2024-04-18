from lib.recipe import *
from lib.recipe_repository import *

"""
When we call on RecipeRepository #all
We get a list of Recipe objects reflecting the seed data
"""

def test_all_gets_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()
    assert recipes == [
        Recipe(1, 'Spaghetti Bolognaise', '1 hour', 4),
        Recipe(2, 'Chicken Tikka Masala', '45 minutes', 3),
        Recipe(3, 'Stir Fry', '25 minutes', 1),
        Recipe(4, 'Pizza', '15 minutes', 2),
        Recipe(5, 'Lemon Garlic Salmon', '20 minutes', 4),
        Recipe(6, 'Beef Stew', '2 hours', 5)
    ]

"""
When we call RecipeRepository #find
We get a single Recipe object reflecting our seed data
"""

def test_find_gets_single_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(4)
    assert recipe == Recipe(4, 'Pizza', '15 minutes', 2)

