from database_connection import get_database_connection


class ObjectiveRepository:
    """In charge of reading and writing Objectives to/from the database.
    Deals with Objectives and Evaluations tables.
    """

    def __init__(self, connection):
        self._connection = connection

    def _validate_create_and_rename(self, name, lj_id=-1, obj_id=-1):
        if not isinstance(name, str) or \
                not isinstance(lj_id, int) or \
                not isinstance(obj_id, int):
            raise TypeError()
        if len(name.strip()) == 0:
            raise ValueError(f"Name cannot be empty.")

    def _validate_evaluate(self, obj_id, progress, challenge):
        if not isinstance(progress, int) or \
                not isinstance(challenge, int) or \
                not (0 <= progress <= 10) or \
                not (0 <= challenge <= 10) or \
                not self.get_one(obj_id):
            return False
        return True

    def create(self, name, lj_id):
        """Appends an objective to the database and returns it as a dictionary.

        Args:
            name (str): Name of the new objective.
            lj_id (int): Unique ID of the Learning Journey to append the objective to.

        Returns:
            dict: A dictionary containing the newly created objective.
        """
        self._validate_create_and_rename(name=name, lj_id=lj_id)

        cursor = self._connection.cursor()
        sql = "INSERT INTO Objectives (name, lj_id) VALUES (?, ?)"
        cursor.execute(sql, (name, lj_id))
        self._connection.commit()

        return {"obj_id": cursor.lastrowid, "name": name, "lj_id": lj_id}

    def get_one(self, obj_id):
        """Returns an objective as dictionary if a reference is found.

        Args:
            obj_id (int): Unique ID of the objective, originates from the database.

        Returns:
            dict: A dictionary containing the fetched objective.
        """
        try:
            cursor = self._connection.cursor()
            sql = '''SELECT O.id, O.name, O.lj_id, E.progress, E.challenge 
                    FROM Objectives AS O
                    LEFT JOIN Evaluations AS E ON O.id = E.obj_id
                    WHERE O.id = ?'''
            objective_data = cursor.execute(sql, (obj_id,)).fetchone()
            self._connection.commit()

            objective_dict = {
                "id": objective_data[0],
                "name": objective_data[1],
                "lj_id": objective_data[2],
                "progress": objective_data[3] or 0,
                "challenge": objective_data[4] or 0
            }

            return objective_dict

        except:
            return None

    def get_all(self, lj_id=None):
        """Returns all saved Objectives as a list of dictionaries.
        Optional filter by Learning Journey.

        Args:
            lj_id (int, optional): Unique ID of a Learning Journey filter. Defaults to None.

        Returns:
            list: List of dictionaries containing all (filtered) objectives.
        """
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
                "id": objective_data[0],
                "name": objective_data[1],
                "lj_id": objective_data[2]
            }
            objectives.append(objective_dict)

        return objectives

    def delete_one(self, obj_id):
        """Deletes the given Objective.

        Args:
            obj_id (int): Unique ID of the objective, originates from the database.

        Returns:
            bool: Signal whether the operation was succesful.
        """
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
        self._validate_create_and_rename(obj_id=obj_id, name=new_name)

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
            Bool: Signals if the operation was succesful.
        """

        if not self._validate_evaluate(obj_id, progress, challenge):
            return False

        cursor = self._connection.cursor()
        sql = '''INSERT OR REPLACE INTO Evaluations
                    (obj_id, progress, challenge)
                    VALUES (?, ?, ?)'''
        cursor.execute(sql, (obj_id, progress, challenge))
        self._connection.commit()
        return True


objective_repo = ObjectiveRepository(get_database_connection())
