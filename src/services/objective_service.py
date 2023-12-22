from repositories.objective_repository import objective_repo


class ObjectiveService:
    """Class in charge of business logic.
    """

    def __init__(self, objective_repository=objective_repo):
        self._objective_repository = objective_repository

    def _validate_create(self, name, lj_id):
        if not isinstance(name, str):
            raise TypeError()
        if len(name) == 0 or len(name) > 50 or not lj_id:
            raise ValueError()

    def create_objective(self, name, lj_id):
        """Calls the repository to create an objective
        and returns it as a dictionary.

        Args:
            name (str): Name of the new objective.
            lj_id (int): Unique ID of the Learning Journey to append the objective to.

        Returns:
            dict: A dictionary containing the newly created objective.
        """
        self._validate_create(name, lj_id)
        return self._objective_repository.create(name, lj_id)

    def get_objectives(self, lj_id=None):
        """Calls the repository to query and return all saved Objectives.
        Optional filter: Learning Journey.
        """
        return self._objective_repository.get_all(lj_id)

    def delete_objective(self, obj_id):
        """Calls the repository to delete one Objective.
        """
        return self._objective_repository.delete_one(obj_id)

    def rename_objective(self, obj_id, new_name):
        """Calls the repository to update the name field.

        Args:
            obj_id (int): Objective's unique ID, originating from the database.
            new_name (str): Name to update, input from user.
        """
        return self._objective_repository.rename(obj_id, new_name)

    def evaluate_objective(self, obj_id, progress, challenge):
        """Calls the repository to insert evaluations. Returns objective as dict.

        Args:
            obj_id (int): Objective's unique ID, originating from the database.
            progress (int): Degree of objective completion, input from user.
            challenge (int): Degree of perceived challenge, input from user.

        Returns:
            Bool: Signals if the operation was succesful.
        """
        return self._objective_repository.evaluate(obj_id, progress, challenge)

    def get_evaluations(self, obj_id):
        """Calls the repository to fetch an objective's current
        evaluations from the database.

        Args:
            obj_id (int): Objective's unique ID, originating from the database.

        Returns:
            dict: Dictionary containing the current progress and challenge values.
        """
        objective = self._objective_repository.get_one(obj_id)
        return {"progress": objective["progress"],
                "challenge": objective["challenge"]}


objective_service = ObjectiveService()
