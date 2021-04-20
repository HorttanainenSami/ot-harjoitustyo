import unittest
from services.recipe_service import RecipeService, InvalidLoginError, UsernameAlreadyInUseError
from initialize_database import initialize_database
from tests.config_test import configure

class TestUsersRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self._service = RecipeService()
        configure()

    def test_logging_with_wrong_user(self):
        self.assertRaises(InvalidLoginError, lambda: self._service.handle_login('asd', 'asd'))

    def test_create_user_works(self):
        self.assertTrue(self._service.create_user('sami', '123'))

    def test_cant_create_dublicate_user(self):
        self._service.create_user('asd1', '123')
        self.assertRaises(UsernameAlreadyInUseError, lambda: self._service.create_user('asd1', '123'))

    def test_login_works(self):
        self._service.create_user('asd', '123')
        self.assertTrue(self._service.handle_login('asd', '123'))

    def test_login_logs_correct_user(self):
        self._service.create_user('asd1', '123')
        self._service.create_user('asd2', '123')
        self._service.handle_login('asd1', '123')
        self.assertEqual('asd1',self._service.get_loggedin_user())

    def test_logout(self):
        self._service.create_user('asd1', '123')
        self._service.handle_login('asd1', '123')
        self.assertTrue(self._service.handle_logout())

    def test_logout_if_not_loggedin(self):
        self._service.handle_logout()
        self.assertFalse(self._service.handle_logout())
