from repositories.users_repository import UserRepository
from repositories.recipes_repository import RecipeRepository
from database_connection import get_database_connection
from werkzeug.security import check_password_hash, generate_password_hash


## errors
class PasswordTooShortError(Exception):
    """ raised when password is shorter than 3 chars """
    pass
class UsernameTooShortError(Exception):
    """ raised when username shorter than 3 chars """
    pass
class InvalidLoginError(Exception):
    """ raised when login ends with error"""
    pass
class UsernameAlreadyInUseError(Exception):
    """ raised when username is already in use"""
    pass

class RecipeService:
    '''Class, which handles logic behind recipe app'''

    def __init__(self):
        self._user_repository = UserRepository(get_database_connection())
        self._recipe_repository = RecipeRepository(get_database_connection())
        self._user = None
        self._user_id = None

    def handle_login(self, username, password):
        '''Checks if input credentials are correct.
        Args:
            username
            password
        Returns:
            true: if logging in is successfull
        Raises:
            InvalidLoginError: if username or password is invalid
        '''
        result = self._user_repository.get_user(username)
        if result:
            if check_password_hash(result[2], password):
                self._user = username
                self._user_id = result[0]
                return True
        raise InvalidLoginError('Username or password is invalid')

    def handle_logout(self):
        '''Logs user out of app
        Returns:
            true: if user was logged out successfully
        '''
        self._user = None
        self._user_id = None

    def create_user(self, username, password):
        '''Create user if username and password is atleast 3 characters long and username is unique
        Raises:
            UsernameTooShortError: if username is shorter than 3 characters
            PasswordTooShortError: if password is shorter than 3 characters
            UsernameAlreadyInUseError: if username is already in use
        Returns:
            true: if creating user was success
        '''
        if len(username) < 3:
            raise UsernameTooShortError('username length must be atleast (3) characters long')
        if len(password) < 3:
            raise PasswordTooShortError('password length must be atleast (3) characters long')

        password_hash = generate_password_hash(password)
        result = self._user_repository.get_user(username)
        if result is None:
            print(f'{username} is created')
            self._user_repository.insert_user(username, password_hash)
            return True

        raise UsernameAlreadyInUseError('Username must be unique')

    def get_loggedin_user(self):
        '''Fetch logged id user

        Returns:
            username: if logged in or None
        '''
        return self._user

    def create_recipe(self, recipe_name, ingredients, instructions):
        '''save recipe and ingredients to database
        Args:
            recipe_name
            ingredients: List
            instructions
        '''
        recipe_id = self._recipe_repository.insert_recipe(recipe_name, instructions, self._user_id)

        for ingredient in ingredients:
            self._recipe_repository.add_ingredients(ingredient, recipe_id)

    def get_all_recipes(self):
        '''Fetch all recipes that is created by logged in user
        Returns:
            all usermade recipes
        '''
        return self._recipe_repository.get_all_recipes(self._user_id)

    def get_ingredients(self, recipe_id):
        '''Fetch all ingredients that is linked to recipe_id
        Args:
            recipe_id
        Returns:
            Ingredients
        '''
        return self._recipe_repository.get_ingredients(recipe_id)

    def update_recipe(self, recipe_id, name, ingredients, instructions):
        '''Update name, ingredienst and instructions of recipe
        Args:
            recipe_id
            name: new recipe name
            ingredients: new ingredients list
            instructions: new instructions
        '''
        self._recipe_repository.update_recipe(recipe_id, name, instructions)
        self.ingredients_changed(recipe_id, ingredients)

    def set_recipe_produced(self, recipe_id):
        '''Update recipe timestamp when recipe was last prepared
        Args:
            recipe_id
        '''
        self._recipe_repository.set_produced(recipe_id)

    def ingredients_changed(self, recipe_id, ingredients):
        '''Update remove or add ingredients
        Args:
            recipe_id
            ingredients: updated ingredients list
        '''
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
        '''Delete recipe
        Args:
            recipe_id
        '''
        self._recipe_repository.remove_recipe(recipe_id)
