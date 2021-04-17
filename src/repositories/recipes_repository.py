import sqlite3

class RecipeRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all_recipes(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM recipes;')

    def insert_recipe(self, recipe_name, instructions, user_id):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO recipes (user_id, name, instructions) VALUES (:user_id, :name, :instructions)', {'user_id':user_id, 'name':recipe_name, 'instructions':instructions})

        ## recipe id
        recipe_id = cursor.lastrowid
        self._connection.commit()

        return recipe_id
