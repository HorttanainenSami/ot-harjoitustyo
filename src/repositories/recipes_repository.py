import sqlite3

class RecipeRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all_recipes(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM recipes WHERE user_id=:user_id ORDER BY previous_timestamp', {'user_id':user_id})
        return cursor.fetchall()

    def get_ingredients(self, recipe_id):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM ingredient WHERE recipe_id=:recipe_id ORDER BY id', {'recipe_id':recipe_id})
        return cursor.fetchall()

    def insert_recipe(self, recipe_name, instructions, user_id):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO recipes (user_id, name, instructions, previous_timestamp) VALUES (:user_id, :name, :instructions, datetime("now"))', {'user_id':user_id, 'name':recipe_name, 'instructions':instructions})

        ## recipe id
        recipe_id = cursor.lastrowid
        self._connection.commit()

        return recipe_id

    def remove_ingredient(self, ingredient_id):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM ingredient WHERE id=:ingredient_id', {'ingredient_id':ingredient_id})
        self._connection.commit()

    def add_ingredients(self, ingredient, recipe_id):
        cursor = self._connection.cursor()
        print(f'Appending recipe_id {recipe_id} with {ingredient}')
        cursor.execute('INSERT INTO ingredient (ingredient, recipe_id) VALUES (:ingredient, :recipe_id)', {'ingredient':ingredient, 'recipe_id':recipe_id})

        self._connection.commit()

    def update_ingredients(self, ingredient_id, ingredient_name):
        cursor = self._connection.cursor()
        print(f'Updating ingredients')
        cursor.execute('UPDATE ingredient SET ingredient=:ingredient_name WHERE id=:ingredient_id',{'ingredient_name':ingredient_name, 'ingredient_id':ingredient_id})

    def update_recipe(self, recipe_id, name, instructions):
        cursor = self._connection.cursor()
        print(f'Updating recipe with id:{recipe_id}')
        cursor.execute('UPDATE recipes SET name=:name, instructions=:instructions WHERE id=:recipe_id', {'instructions': instructions, 'name':name, 'recipe_id':recipe_id})
