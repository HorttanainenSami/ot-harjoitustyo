from database_connection import get_database_connection

def drop_tables(connection):
    '''Delete all tables and contents from database, is used when initializing databases

    '''
    cursor = connection.cursor()

    cursor.execute('''drop table if exists user;''')
    cursor.execute('''drop table if exists recipes;''')
    cursor.execute('''drop table if exists ingredient;''')

def create_tables(connection):
    '''Create all tables that app needs to work properly

    Args:
        connection: sqlite3.connect Object
    '''
    cursor = connection.cursor()

    cursor.execute('''
        create table user (
        id INTEGER PRIMARY KEY,
        username text,
        password text
        );
    ''')

    cursor.execute('''
        create table recipes (
        id INTEGER PRIMARY KEY,
        user_id text REFERENCES user(id),
        name text,
        instructions text,
        previous_timestamp text
        );
    ''')

    cursor.execute('''
        create table ingredient (
        id INTEGER PRIMARY KEY,
        ingredient text,
        recipe_id text REFERENCES recipes(id)
        ); 
    ''')
    cursor.execute('''
        create index idx_recipeid ON ingredient (recipe_id);
    ''')
    connection.commit()

def initialize_database():
    ''' Delete and initialize tables for app to work properly
    '''
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
