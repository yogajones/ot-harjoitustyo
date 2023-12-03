from entities.learningjourney import LearningJourney
from entities.objective import Objective
from repositories.objective_repository import objective_repo


class ObjectiveService:
    """Class in charge of business logic."""

    def __init__(self, objective_repository=objective_repo):
        """Creates a ObjectService object with an
        empty repository for Objectives."""
        self._objective_repository = objective_repository

    def create_objective(self, name: str, lj: LearningJourney):
        """Calls the repository to create an Objective object and returns it."""
        # REFACTOR: perhaps a try-except block with a boolean return would be better here

        if not isinstance(name, str) or not isinstance(lj, LearningJourney):
            return TypeError()
        if len(name) == 0 or len(name) > 50:
            return ValueError()

        objective = Objective(name)
        return self._objective_repository.create(objective, lj)

    def get_objectives(self, lj_id=None):
        """Calls the repository to query and return all saved Objectives. Optional filter: Learning Journey."""
        return self._objective_repository.get_all(lj_id)


objective_service = ObjectiveService()
