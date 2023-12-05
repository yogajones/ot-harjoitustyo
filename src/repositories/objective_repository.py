from database_connection import get_database_connection


class ObjectiveRepository:
    "In charge of reading and writing Objectives to/from the database."

    def __init__(self, connection):
        """Establishes a repository for Objective objects
        to be used in database operations."""
        self._connection = connection

    def create(self, name: str, lj_id):
        """Appends an objective to the database and returns it as a dictionary."""

        if not isinstance(name, str):
            return TypeError()

        cursor = self._connection.cursor()
        sql = "INSERT INTO Objectives (name, lj_id) VALUES (?, ?)"
        cursor.execute(sql, (name, lj_id))
        self._connection.commit()

        return {"name": name, "lj_id": lj_id}

    def get_all(self, lj_id=None):
        """Returns all saved Objectives as a list of dictionaries.
        Optional filter by Learning Journey."""
        cursor = self._connection.cursor()
        if lj_id:
            objectives_data = cursor.execute(
                "SELECT id, name, lj_id FROM Objectives WHERE lj_id = ?", (lj_id,)).fetchall()
        else:
            objectives_data = cursor.execute(
                "SELECT id, name, lj_id FROM Objectives").fetchall()
        self._connection.commit()

        objectives = []
        for objective_data in objectives_data:
            objective_dict = {
                'id': objective_data[0],
                'name': objective_data[1],
                'lj_id': objective_data[2]
            }
            objectives.append(objective_dict)

        return objectives

    def delete_all(self):
        """Deletes all saved Objectives."""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Objectives;")
        self._connection.commit()


objective_repo = ObjectiveRepository(get_database_connection())
