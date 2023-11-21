from entities.learningjourney import LearningJourney
from repositories.learning_journey_repository import learning_journey_repo


class LearningJourneyService:
    """Class in charge of business logic."""

    def __init__(self, learning_journey_repository=learning_journey_repo) -> None:
        """Creates a LearningJourneyService object with an empty repository for Learning Journeys."""
        self._learning_journey_repository = learning_journey_repository


    def create_learning_journey(self, name: str, active: int=1):
        """Calls the repository to create a Learning Journey object and returns it."""
        if type(name) != str or type(active) != int:
            return TypeError()
        if len(name) == 0 or active < 0 or active > 1:
            return ValueError()
        
        learning_journey = LearningJourney(name=name, active=active)
        return self._learning_journey_repository.create(learning_journey=learning_journey)
    

    def get_learning_journeys(self):
        """Calls the repository to query and return all saved Learning Journeys."""
        journeys = self._learning_journey_repository.get_all()
        return journeys
    
learning_journey_service = LearningJourneyService()