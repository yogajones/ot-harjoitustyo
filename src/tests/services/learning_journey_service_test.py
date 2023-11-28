import unittest
from services.learning_journey_service import LearningJourneyService
from repositories.learning_journey_repository import learning_journey_repo, AlreadyInUse
from entities.learningjourney import LearningJourney


class TestLearningJourneyService(unittest.TestCase):
    def setUp(self):
        """Create a Learning Journey Service instance
        that uses an emptied mock repository."""
        self.learning_journey_repo = learning_journey_repo
        self.learning_journey_repo.delete_all()
        self.lj_service = LearningJourneyService(self.learning_journey_repo)

    def test_create_lj_valid_input(self):
        """With valid input, succesfully create and return a Learning Journey.

        test_create in learning_journey_repository_test.py checks that the
        object is indeed saved to the database."""
        lj_object = self.lj_service.create_learning_journey(
            "Wheel in the Sky", 1)
        self.assertIsInstance(lj_object, LearningJourney)

    def test_create_lj_empty_name(self):
        """With an invalid input (empty name), return an error."""
        self.assertIsInstance(
            self.lj_service.create_learning_journey("", 1), ValueError)
        self.assertIsInstance(self.lj_service.create_learning_journey(
            "Any Way You Want It", 2), ValueError)

    def test_create_lj_type_conflict(self):
        """With an invalid input (wrong type), return an error."""
        self.assertIsInstance(
            self.lj_service.create_learning_journey(True, 1), TypeError)

    def test_create_lj_name_already_in_use(self):
        """Using an already existing name, return an error."""
        self.lj_service.create_learning_journey("Wheel in the Sky", 1)
        self.assertIsInstance(self.lj_service.create_learning_journey(
            "Wheel in the Sky", 1), AlreadyInUse)
        
    def test_get_ljs_returns_them(self):
        """When a Learning Journey is known to be added,
        make sure it is returned."""
        self.lj_service.create_learning_journey("Unit testing 101")
        self.assertIsNotNone(self.lj_service.get_learning_journeys())
