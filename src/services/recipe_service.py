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
class UsernameAllreadyInUseError(Error):
    """ raised when username is allready in use"""
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
            print(result[0])
            self._user_id = result[0]
        else:
            raise InvalidLoginError('Username or password is wrong')

    def handle_logout(self):
        if self._user:
            print(f'{self._user} logged out')
            self._user = None

    def create_user(self, username, password):
        print(f'trying to create user {username} and {password}') 
        result= self._user_repository.get_user(username)
        if result is None:
            print(f'{username} is created')
            self._user_repository.insert_user(username, password)
        else:
            raise UsernameAllreadyInUseError('Username is allready in use')

    def get_logged_user(self):
        return self._user

    def createRecipe(self, recipe_name, ingredients, instructions):
        splits = ingredients.splitlines()
        print(recipe_name)
        self._recipe_repository.insert_recipe(recipe_name, instructions, self._user_id)
