from entities.learningjourney import LearningJourney
from database_connection import get_database_connection, get_test_database_connection


class AlreadyInUse(Exception):
    pass


class LearningJourneyRepository:
    "In charge of reading and writing Learning Journeys to/from the database."

    def __init__(self, connection):
        """Establishes a repository for Learning Journey objects
        to be used in database operations."""
        self._connection = connection

    def get_one(self, lj_name):
        """Returns a database row from LearningJourneys table
        if a reference is found."""
        cursor = self._connection.cursor()
        sql = "SELECT id, name, active FROM LearningJourneys WHERE name = ?"
        result = cursor.execute(sql, (lj_name,)).fetchone()
        self._connection.commit()

        return result

    def create(self, name, active):
        """Appends a Learning Journey to the database and returns it."""
        if self.get_one(name):
            raise AlreadyInUse(f"The name {name} is already in use.")

        cursor = self._connection.cursor()
        sql = "INSERT INTO LearningJourneys (name, active) VALUES (?, ?)"
        cursor.execute(sql, (name, active))
        lj_id = cursor.lastrowid
        self._connection.commit()

        return LearningJourney(name, active, lj_id)

    def get_all(self):
        """Returns all saved Learning Journeys, parsed to a list of dictionaries."""
        cursor = self._connection.cursor()
        cursor.execute("SELECT id, name, active FROM LearningJourneys")
        journeys_data = cursor.fetchall()
        self._connection.commit()

        journeys = []
        for journey_data in journeys_data:
            journey_dict = {
                'id': journey_data[0],
                'name': journey_data[1],
                'active': journey_data[2]
            }
            journeys.append(journey_dict)

        return journeys


learning_journey_repo = LearningJourneyRepository(get_database_connection())
test_learning_journey_repo = LearningJourneyRepository(
    get_test_database_connection())
