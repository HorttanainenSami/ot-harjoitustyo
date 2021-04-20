import unittest
from services.recipe_service import RecipeService, InvalidLoginError, UsernameAlreadyInUseError
from initialize_database import initialize_database
from tests.config_test import configure

class TestUsersRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self._service = RecipeService()
        configure()
    def test_get_recipe_that_doesnt_exist(self):
        
