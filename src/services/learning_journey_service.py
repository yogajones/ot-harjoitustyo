from repositories.learning_journey_repository import learning_journey_repo


class LearningJourneyService:
    """Class in charge of business logic.
    """

    def __init__(self, learning_journey_repository=learning_journey_repo):

        self._learning_journey_repository = learning_journey_repository

    def create_learning_journey(self, name, active=1):
        """Calls the repository the add a new Learning Journey to the database.

        Args:
            name (str): Name of the new Learning Journey to create, input from user.
            active (int, optional): Activity status of the LJ. Defaults to 1.

        Returns:
            LearningJourney: The newly created Learning Journey.
        """
        return self._learning_journey_repository.create(name, active)

    def get_learning_journeys(self):
        """Calls the repository to query and return all saved Learning Journeys.

        Returns:
            list: List of dictionaries containing existing Learning Journeys.
        """
        journeys = self._learning_journey_repository.get_all()
        return journeys


learning_journey_service = LearningJourneyService()
