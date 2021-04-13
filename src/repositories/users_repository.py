import sqlite3


class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM user;')

    def insert_user(self, username, password):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO user (username, password) VALUES (:username, :password)', {'username':username, 'password':password})
        self._connection.commit()

    def get_user(self, username):
        cursor = self._connection.cursor()
        result = cursor.execute('SELECT * FROM user WHERE username=:username', {'username':username})
        return result.fetchone()

    def check_login(self, username, password):
        cursor = self._connection.cursor()
        result = cursor.execute('SELECT * FROM user WHERE username=:username AND password=:password', {'username':username, 'password':password})
        return result.fetchone()

