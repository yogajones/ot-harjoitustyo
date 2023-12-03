from entities.objective import Objective
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

    def get_all(self, lj_id):
        """Returns all saved Objectives. Optional filter by Learning Journey."""
        cursor = self._connection.cursor()
        if lj_id:
            objectives_data = cursor.execute(
                "SELECT name, lj_id FROM Objectives WHERE lj_id = ?", (lj_id,)).fetchall()
        else:
            objectives_data = cursor.execute(
                "SELECT name, lj_id FROM Objectives").fetchall()
        self._connection.commit()

        # Convert database records to Objectives
        objectives = [
            Objective(name=objective_data['name'],
                      lj_id=objective_data['lj_id'])
            for objective_data in objectives_data]

        return objectives

    def delete_all(self):
        """Deletes all saved Objectives."""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Objectives;")
        self._connection.commit()


objective_repo = ObjectiveRepository(get_database_connection())
