from database_connection import get_database_connection, get_test_database_connection


class ObjectiveRepository:
    """In charge of reading and writing Objectives to/from the database.
    Deals with Objectives and Evaluations tables."""

    # REFACTOR: privatize methods

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

        return {"obj_id": cursor.lastrowid, "name": name, "lj_id": lj_id}

    def get_one(self, obj_id):
        """Returns a database row from Objectives table if a reference is found."""
        cursor = self._connection.cursor()
        sql = "SELECT id, name, lj_id FROM Objectives WHERE id = ?"
        result = cursor.execute(sql, (obj_id,)).fetchone()
        self._connection.commit()

        return result

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

    def delete_one(self, obj_id):
        """Deletes the given Objective."""
        if self.get_one(obj_id):
            cursor = self._connection.cursor()
            cursor.execute("DELETE FROM Objectives where id = ?", (obj_id,))
            self._connection.commit()
            return True
        return False

    def rename(self, obj_id, new_name):
        """Updates the name field of the given objective.

        Args:
            obj_id (int): Objective's unique ID, originating from the database.
            new_name (str): Name to update, input from user.
        """
        if self.get_one(obj_id) and new_name:
            cursor = self._connection.cursor()
            cursor.execute(
                "UPDATE Objectives SET name = ? WHERE id = ?", (new_name, obj_id))
            self._connection.commit()
            return True
        return False

    def evaluate(self, obj_id, progress, challenge):
        """Updates an Objective's evaluations.

        Args:
            obj_id (int): Objective's unique ID, originating from the database.
            progress (int): Degree of objective completion, input from user.
            challenge (int): Degree of perceived challenge, input from user.

        Returns:
            dict: Updated objective as dict.
        """
        if self.get_one(obj_id):
            cursor = self._connection.cursor()
            sql = "INSERT INTO Evaluations (obj_id, progress, challenge) VALUES (?, ?, ?)"
            cursor.execute(sql, (obj_id, progress, challenge))
            self._connection.commit()

            test_print = cursor.execute("SELECT * FROM Evaluations").fetchall()
            print(test_print)

            return  # objective as dict


objective_repo = ObjectiveRepository(get_database_connection())
test_objective_repo = ObjectiveRepository(get_test_database_connection())
