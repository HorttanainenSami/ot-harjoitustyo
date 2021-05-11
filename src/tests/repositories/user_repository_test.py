import unittest
from repositories.users_repository import UserRepository
from initialize_database import initialize_database
from tests.config_test import configure
from database_connection import get_database_connection

class TestUsersRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self._user = UserRepository(get_database_connection())
        configure()

    def test_get_empty_list_of_users(self):
        users_list = self._user.get_all_users()
        self.assertEqual(0, len(users_list))

    def test_insert_user_works(self):
        self._user.insert_user('sami', 'sami')
        user = self._user.get_all_users()
        self.assertEqual(1, len(user))
       
    def test_get_user_works(self):
        self._user.insert_user('test', 'test')
        user = self._user.get_user('test')
        self.assertEqual('test', user[1])

    def test_insert_user_adds_password_hash(self):
        self._user.insert_user('test1', 'test')
        user = self._user.get_user('test1')
        self.assertEqual('test', user[2])

