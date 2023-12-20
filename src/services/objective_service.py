from repositories.objective_repository import objective_repo


class ObjectiveService:
    """Class in charge of business logic."""

    def __init__(self, objective_repository=objective_repo):
        """Creates a ObjectService object with an
        empty repository for Objectives."""
        self._objective_repository = objective_repository

    def create_objective(self, name: str, lj_id):
        """Calls the repository to create an Objective object and returns it as a dictionary."""
        # REFACTOR: perhaps a try-except block with a boolean return would be better here

        if not isinstance(name, str):
            return TypeError()
        if len(name) == 0 or len(name) > 50 or not lj_id:
            return ValueError()

        return self._objective_repository.create(name, lj_id)

    def get_objectives(self, lj_id=None):
        """Calls the repository to query and return all saved Objectives.
        Optional filter: Learning Journey."""
        return self._objective_repository.get_all(lj_id)

    def delete_objective(self, obj_id):
        """Calls the repository to delete one Objective."""
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
            dict: Updated objective as dict.
        """
        return self._objective_repository.evaluate(obj_id, progress, challenge)


objective_service = ObjectiveService()
