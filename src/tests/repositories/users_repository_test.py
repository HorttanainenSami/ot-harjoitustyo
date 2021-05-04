import unittest
from services.recipe_service import RecipeService, InvalidLoginError, UsernameAlreadyInUseError, PasswordTooShortError, UsernameTooShortError
from initialize_database import initialize_database
from tests.config_test import configure

class TestUsersRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self._service = RecipeService()
        configure()
        self._service.create_user('testi', 'asd')

    def test_loging_with_wrong_user(self):
        self.assertRaises(InvalidLoginError, lambda: self._service.handle_login('asd', 'asd'))

    def test_login_with_wrong_password(self):
        self._service.create_user('wrongPassword', '1234')
        self.assertRaises(InvalidLoginError, lambda: self._service.handle_login('wrongPassword', '123'))

    def test_create_user_works(self):
        self.assertTrue(self._service.create_user('sami', '123'))

    def test_cant_create_user_with_too_short_username(self):
        self.assertRaises(UsernameTooShortError, lambda: self._service.create_user('', 'asd'))

    def test_cant_create_user_with_too_short_password(self):
        self.assertRaises(PasswordTooShortError, lambda: self._service.create_user('asd', ''))

    def test_cant_create_dublicate_user(self):
        self._service.create_user('asd1', '123')
        self.assertRaises(UsernameAlreadyInUseError, lambda: self._service.create_user('asd1', '123'))

    def test_login_works(self):
        self._service.create_user('asd', '123')
        self.assertTrue(self._service.handle_login('asd', '123'))
        self._service.handle_logout()

    def test_login_saves_correct_data(self):
        self._service.create_user('asd1', '123')
        self._service.create_user('asd2', '123')
        self._service.handle_login('asd1', '123')
        self.assertEqual('asd1', self._service.get_loggedin_user())
        self._service.handle_logout()

    def test_logout(self):
        self._service.create_user('asd1', '123')
        self._service.handle_login('asd1', '123')
        self.assertEqual('asd1', self._service.get_loggedin_user())
        self._service.handle_logout()
        self.assertEqual(None, self._service.get_loggedin_user())

    def test_empty_list_returns_empty_list(self):
        self._service.handle_login('testi', 'asd')
        self.assertEqual(0, len(self._service.get_all_recipes()))
        self._service.handle_logout()

    def test_creating_recipe_works(self):
        self._service.handle_login('testi', 'asd')
        initial_list = self._service.get_all_recipes()
        recipe_name = 'recipe'
        ingredients = ['ingredient1', 'ingredient2']
        instructions = 'instructions'
        self._service.create_recipe(recipe_name, ingredients, instructions)
        new_recipe_list = self._service.get_all_recipes()
        self.assertEqual(len(initial_list), len(new_recipe_list) - 1)

        recipe_id = new_recipe_list[0][0]
        initial_ingredients = []
        for row in self._service.get_ingredients(recipe_id):
            initial_ingredients.append(row[1])

        self.assertEqual(ingredients, initial_ingredients)

        self._service.handle_logout()


