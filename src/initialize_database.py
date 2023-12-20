from database_connection import get_database_connection, get_test_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS LearningJourneys;''')
    cursor.execute('''DROP TABLE IF EXISTS Objectives;''')
    cursor.execute('''DROP TABLE IF EXISTS Evaluations;''')
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
    cursor.execute('''CREATE TABLE Evaluations (
                   id INTEGER PRIMARY KEY,
                   obj_id INTEGER NOT NULL,
                   progress INTEGER,
                   challenge INTEGER,
                   FOREIGN KEY (obj_id) REFERENCES Objectives(id));''')

    connection.commit()


def initialize_database():
    """Creates tables with no data. CAUTION: will destroy all saved data.
    """
    connection = get_database_connection()

    drop_tables(connection=connection)
    create_tables(connection=connection)


def initialize_test_database():
    """Creates test tables with no data.
    """
    test_connection = get_test_database_connection()

    drop_tables(connection=test_connection)
    create_tables(connection=test_connection)
