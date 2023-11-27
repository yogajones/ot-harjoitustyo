from entities.objetive import Objective
from entities.learningjourney import LearningJourney
from repositories.learning_journey_repository import learning_journey_repo
from database_connection import get_database_connection


class ObjectiveRepository:
    "In charge of reading and writing Objectives to/from the database."

    def __init__(self, connection):
        """Establishes a repository for Objective objects
        to be used in database operations."""
        self._connection = connection

    def create(self, objective: Objective, lj: LearningJourney):
        """Appends an Objective to the database and returns it."""

        if not isinstance(lj, LearningJourney) or \
            not isinstance(objective, Objective):
            return TypeError()

        cursor = self._connection.cursor()
        sql = "INSERT INTO Objectives (name, lj_id) VALUES (?, ?)"
        lj_id = learning_journey_repo.get_one(lj)['id']
        cursor.execute(sql, (objective.name, lj_id))
        self._connection.commit()

        return objective
    
    def get_all(self):
        """Returns all saved Objectives."""
        cursor = self._connection.cursor()
        objectives = cursor.execute(
            "SELECT name, lj_id FROM Objectives"
        ).fetchall()
        self._connection.commit()

        return objectives


objective_repo = ObjectiveRepository(get_database_connection())
