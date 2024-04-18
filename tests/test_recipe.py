
from lib.recipe import *

"""
Recipe constructs with an id, name, cooking_time and rating
"""

def test_recipe_construction():
    recipe = Recipe(1, 'Test recipe', 'test time', 2)
    assert recipe.id == 1
    assert recipe.name == 'Test recipe'
    assert recipe.cooking_time == 'test time'
    assert recipe.rating == 2

"""
We can format recipes to strings
"""    

def test_recipe_formats_nicely():
    recipe = Recipe(1, 'Test recipe', 'test time', 2)
    assert str(recipe) == "Recipe(1, Test recipe, test time, 2)"

"""
We can compare two identical recipes 
and have them be equal
"""

def test_recipes_are_equal():
    recipe1 = Recipe(1, 'Test recipe', 'test time', 2)
    recipe2 = Recipe(1, 'Test recipe', 'test time', 2)
    assert recipe1 == recipe2

    