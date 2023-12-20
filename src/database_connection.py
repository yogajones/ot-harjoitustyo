import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(
    dirname, "..", "data", "database.sqlite"))
connection.row_factory = sqlite3.Row

test_connection = sqlite3.connect(os.path.join(
    dirname, "..", "data", "test_database.sqlite"))
test_connection.row_factory = sqlite3.Row


def enable_foreign_keys(connection):
    """Enables the use of the 'ON DELETE CASCADE' in the schema.

    Args:
        connection (Connection): database connection
    """
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    connection.commit()


def get_database_connection():
    """Establishes a production database connection.

    Returns:
        Connection: connection to production database
    """
    enable_foreign_keys(connection=connection)
    return connection


def get_test_database_connection():
    """Establishes a test database connection.

    Returns:
        Connection: connection to test database
    """
    enable_foreign_keys(connection=test_connection)
    return test_connection
