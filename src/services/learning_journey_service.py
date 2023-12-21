from repositories.learning_journey_repository import learning_journey_repo


class LearningJourneyService:
    """Class in charge of business logic."""

    def __init__(self, learning_journey_repository=learning_journey_repo):
        """Creates a LearningJourneyService object with an
        empty repository for Learning Journeys."""
        self._learning_journey_repository = learning_journey_repository

    def create_learning_journey(self, name, active=1):
        return self._learning_journey_repository.create(name, active)

    def get_learning_journeys(self):
        """Calls the repository to query and return all saved Learning Journeys."""
        journeys = self._learning_journey_repository.get_all()
        return journeys


learning_journey_service = LearningJourneyService()
