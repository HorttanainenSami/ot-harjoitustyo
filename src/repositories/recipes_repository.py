import sqlite3
class RecipeRepository:
    '''Class, interface between recipe and Database.

    Attributes:
        _connection: sqlite connection object
        _cursor: sqlite cursor object
    '''
    def __init__(self, connection):

        self._connection = connection
        self._cursor = self._connection.cursor()

    def get_all_recipes(self, user_id):
        '''Gets all recipes which are linked to your user

        Args:
            user_id
        Returns:
            All recipes which are created by user
        '''
        self._cursor.execute('SELECT * FROM recipes WHERE user_id=:user_id ORDER BY previous_timestamp', {'user_id':user_id})
        return self._cursor.fetchall()

    def get_ingredients(self, recipe_id):
        '''Gets all ingredients that are linked to recipe_id

        Args:
            recipe_id

        Returns:
            all ingredients which are linked to recipe
        '''
        self._cursor.execute('SELECT * FROM ingredient WHERE recipe_id=:recipe_id ORDER BY id', {'recipe_id':recipe_id})
        return self._cursor.fetchall()

    def insert_recipe(self, recipe_name, instructions, user_id):
        '''Stores recipe in database and returns recipe_id in database

        Args:
            recipe_name
            instructions
            user_id
        Returns:
            id of newly creaded recipe
        '''
        self._cursor.execute('INSERT INTO recipes (user_id, name, instructions, previous_timestamp) VALUES (:user_id, :name, :instructions, datetime("now"))', {'user_id':user_id, 'name':recipe_name, 'instructions':instructions})

        ## recipe id
        recipe_id = self._cursor.lastrowid
        self._connection.commit()

        return recipe_id

    def remove_ingredient(self, ingredient_id):
        '''Remove particular ingredient from database

        Args:
            ingredient_id: the id of ingredient to be removed
        '''
        self._cursor.execute('DELETE FROM ingredient WHERE id=:ingredient_id', {'ingredient_id':ingredient_id})
        self._connection.commit()

    def add_ingredients(self, ingredient, recipe_id):
        '''Add ingredients to database

        Args:
            ingredient
            recipe_id
        '''
        self._cursor.execute('INSERT INTO ingredient (ingredient, recipe_id) VALUES (:ingredient, :recipe_id)', {'ingredient':ingredient, 'recipe_id':recipe_id})
        self._connection.commit()

    def update_ingredient(self, ingredient_id, ingredient_name):
        '''Change ingredient name
        Args:
            ingredient_id: The id of ingredient that is updated
            ingredien_name: new name of ingredient
        '''
        self._cursor.execute('UPDATE ingredient SET ingredient=:ingredient_name WHERE id=:ingredient_id', {'ingredient_name':ingredient_name, 'ingredient_id':ingredient_id})

    def update_recipe(self, recipe_id, name, instructions):
        '''Update name or instructions of recipe
        Args:
            recipe_id: the id of recipe that is updated
            name: new recipe name
            instructions: new instructions
        '''
        self._cursor.execute('UPDATE recipes SET name=:name, instructions=:instructions WHERE id=:recipe_id', {'instructions': instructions, 'name':name, 'recipe_id':recipe_id})

    def set_produced(self, recipe_id):
        '''Update last preparation time current time
        Args:
            recipe_id
        '''
        self._cursor.execute('UPDATE recipes SET previous_timestamp=datetime("now") WHERE id=:recipe_id', {'recipe_id':recipe_id})

    def remove_recipe(self, recipe_id):
        '''Remove recipe from database
        Args:
            recipe_id
        '''
        self._remove_ingredients(recipe_id)
        self._cursor.execute('DELETE FROM recipes WHERE id=:recipe_id', {'recipe_id':recipe_id})
        self._connection.commit()

    def _remove_ingredients(self, recipe_id):
        '''Remove all ingredients by recipe_id
        Args:
            recipe_id
        '''
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM ingredient WHERE recipe_id=:recipe_id', {'recipe_id':recipe_id})
        self._connection.commit()

