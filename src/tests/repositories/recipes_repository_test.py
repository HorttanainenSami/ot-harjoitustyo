import unittest
from services.recipe_service import RecipeService
from initialize_database import initialize_database
from tests.config_test import configure

class TestRecipesRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self._service = RecipeService()
        configure()
    
