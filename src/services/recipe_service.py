from repositories.users_repository import UserRepository
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
        self._user = None
    
    def handle_login(self, username, password):
        if self._user_repository.check_login(username, password):
            self._user = username
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

