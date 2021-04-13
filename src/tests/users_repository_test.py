import unittest
from services.recipe_service import RecipeService, InvalidLoginError, UsernameAllreadyInUseError
from initialize_database import initialize_database

class TestUsersRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self._service = RecipeService()

    def test_logging_with_wrong_user(self):
        self.assertRaises(InvalidLoginError, lambda:self._service.handle_login('asd', 'asd'))
