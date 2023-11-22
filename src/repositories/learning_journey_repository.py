from entities.learningjourney import LearningJourney
from database_connection import get_database_connection


class AlreadyInUse(Exception):
    pass


class LearningJourneyRepository:
    "In charge of reading and writing Learning Journeys to/from the database."

    def __init__(self, connection):
        """Establishes a repository for Learning Journey objects
        to be used in database operations."""
        self._connection = connection

    def get_one(self, learning_journey):
        """Returns a database row from LearningJourneys table
        if a reference is found."""
        cursor = self._connection.cursor()
        sql = "SELECT 1 FROM LearningJourneys WHERE name = ?"
        result = cursor.execute(sql, (learning_journey.name,)).fetchone()
        self._connection.commit()

        return result

    def create(self, learning_journey: LearningJourney):
        """Appends a Learning Journey to the database and returns it."""

        if not isinstance(learning_journey, LearningJourney):
            return TypeError()
        if self.get_one(learning_journey):
            return AlreadyInUse()

        cursor = self._connection.cursor()
        sql = "INSERT INTO LearningJourneys (name, active) VALUES (?, ?)"
        cursor.execute(sql, (learning_journey.name, learning_journey.active))
        self._connection.commit()

        return learning_journey

    def get_all(self):
        """Returns all saved Learning Journeys."""
        cursor = self._connection.cursor()
        journeys = cursor.execute(
            "SELECT name, active FROM LearningJourneys"
        ).fetchall()
        self._connection.commit()

        return journeys

    def delete_all(self):
        """Deletes all saved Learning Journeys."""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM LearningJourneys;")
        self._connection.commit()


learning_journey_repo = LearningJourneyRepository(get_database_connection())
