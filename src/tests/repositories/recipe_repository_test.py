import unittest
from repositories.recipes_repository import RecipeRepository
from initialize_database import initialize_database
from tests.config_test import configure
from database_connection import get_database_connection

class TestUsersRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self._user = RecipeRepository(get_database_connection())
        configure()

