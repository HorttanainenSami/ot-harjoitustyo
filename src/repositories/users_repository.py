import sqlite3


class UserRepository:
    '''Interface between database and User table

    '''
    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor()
    def get_all_users(self):
        '''Fetch all users from database
        Returns:
            all users in database
        '''
        return self._cursor.execute('SELECT * FROM user').fetchall()

    def insert_user(self, username, password):
        '''Inserts user in database
        Args:
            username
            password
        '''
        self._cursor.execute('INSERT INTO user (username, password) VALUES (:username, :password)', {'username':username, 'password':password})
        self._connection.commit()

    def get_user(self, username):
        '''Fetch user by username from database
        Args:
            username
        Returns:
            user which username is equal with keyword
        '''
        result = self._cursor.execute('SELECT * FROM user WHERE username=:username', {'username':username})
        return result.fetchone()
