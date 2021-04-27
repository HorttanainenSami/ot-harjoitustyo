from repositories.users_repository import UserRepository
from repositories.recipes_repository import RecipeRepository
from database_connection import get_database_connection


## errors
class Error(Exception):
    """ base error"""
    pass

class InvalidLoginError(Error):
    """ raised when login ends with error"""
    pass
class UsernameAlreadyInUseError(Error):
    """ raised when username is already in use"""
    pass

class RecipeService:

    def __init__(self):
        self._user_repository = UserRepository(get_database_connection())
        self._recipe_repository = RecipeRepository(get_database_connection())
        self._user = None
        self._user_id = None

    def handle_login(self, username, password):
        result = self._user_repository.check_login(username, password)
        if result:
            self._user = username
            self._user_id = result[0]
            return True
        raise InvalidLoginError('Username or password is wrong')

    def handle_logout(self):
        if self._user:
            print(f'{self._user} logged out')
            self._user = None
            return True
        return False

    def create_user(self, username, password):
        print(f'trying to create user {username} and {password}')
        result = self._user_repository.get_user(username)
        if result is None:
            print(f'{username} is created')
            self._user_repository.insert_user(username, password)
            return True

        raise UsernameAlreadyInUseError('Username is already in use')

    def get_loggedin_user(self):
        return self._user

    def create_recipe(self, recipe_name, ingredients, instructions):
        recipe_id = self._recipe_repository.insert_recipe(recipe_name, instructions, self._user_id)

        for ingredient in ingredients:
            self._recipe_repository.add_ingredients(ingredient, recipe_id)

    def get_all_recipes(self):
        return self._recipe_repository.get_all_recipes(self._user_id)

    def get_ingredients(self, recipe_id):
        return self._recipe_repository.get_ingredients(recipe_id)

    def update_recipe(self, recipe_id, name, ingredients, instructions):
        self._recipe_repository.update_recipe(recipe_id, name, instructions)
        self.ingredients_changed(recipe_id, ingredients)

    def set_recipe_produced(self, recipe_id):
        self._recipe_repository.set_produced(recipe_id)

    def ingredients_changed(self, recipe_id, ingredients):
        saved_ingredients = self._recipe_repository.get_ingredients(recipe_id)
        asd = len(ingredients)
        if len(saved_ingredients) < len(ingredients):
            asd = len(saved_ingredients)
        idx = 0
        while idx < asd:
            server_ingredient_name = str(saved_ingredients[idx][1])
            updated_ingredient_name = ingredients[idx]
            ingredient_id = saved_ingredients[idx][0]

            print(f'name = {server_ingredient_name} : {updated_ingredient_name}')
            if server_ingredient_name != updated_ingredient_name:
                print('update')
                self._recipe_repository.update_ingredient(ingredient_id, updated_ingredient_name)
            idx += 1
        ## add ingredients if new
        i = len(saved_ingredients)
        while i < len(ingredients):
            self._recipe_repository.add_ingredients(ingredients[i], recipe_id)
            i += 1
        ## remove ingredients if removed
        i = len(ingredients)
        while i < len(saved_ingredients):
            self._recipe_repository.remove_ingredient(saved_ingredients[i][0])
            i += 1

    def delete_recipe(self, recipe_id):
        self._recipe_repository.remove_recipe(recipe_id)
