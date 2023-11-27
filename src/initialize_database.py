from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS LearningJourneys;''')
    cursor.execute('''DROP TABLE IF EXISTS Objectives;''')
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE LearningJourneys (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL UNIQUE,
                   active INTEGER);''')
    cursor.execute('''CREATE TABLE Objectives (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   lj_id INTEGER,
                   FOREIGN KEY (lj_id) REFERENCES LearningJourneys(id));''')

    connection.commit()


def initialize_database():
    """Creates tables with no data.
    CAUTION: will destroy all saved data."""
    connection = get_database_connection()

    drop_tables(connection=connection)
    create_tables(connection=connection)
