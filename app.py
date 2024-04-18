
from lib.database_connection import *
from lib.recipe_repository import *
from lib.recipe import *

connection = DatabaseConnection()
connection.connect()
connection.seed("seeds/recipes.sql")

recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()

for recipe in recipes:
    print(recipe)

print(recipe_repository.find(4))

