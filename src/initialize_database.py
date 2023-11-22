from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS LearningJourneys;''')
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE LearningJourneys (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   active INTEGER);''')

    connection.commit()


def initialize_database():
    """Creates tables with no data.
    CAUTION: will destroy all saved data."""
    connection = get_database_connection()

    drop_tables(connection=connection)
    create_tables(connection=connection)
