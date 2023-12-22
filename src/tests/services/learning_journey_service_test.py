import unittest
from services.learning_journey_service import LearningJourneyService
from repositories.learning_journey_repository import LearningJourneyRepository, AlreadyInUse
from entities.learningjourney import LearningJourney
from initialize_database import initialize_test_database
from database_connection import get_test_database_connection

test_learning_journey_repo = LearningJourneyRepository(
    get_test_database_connection())


class TestLearningJourneyService(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self.learning_journey_repo = test_learning_journey_repo
        self.lj_service = LearningJourneyService(self.learning_journey_repo)

    def test_create_lj_valid_input(self):
        lj_object = self.lj_service.create_learning_journey("LJ", 1)
        self.assertIsInstance(lj_object, LearningJourney)

    def test_create_lj_empty_name(self):
        self.assertRaises(
            ValueError, self.lj_service.create_learning_journey, "", 1)

    def test_create_lj_with_invalid_status_parameter(self):
        self.assertRaises(
            ValueError, self.lj_service.create_learning_journey, "LJ", 2)

    def test_create_lj_type_conflict(self):
        self.assertRaises(
            TypeError, self.lj_service.create_learning_journey, True, 1)

    def test_create_lj_name_already_in_use(self):
        self.lj_service.create_learning_journey("LJ", 1)
        self.assertRaises(
            AlreadyInUse, self.lj_service.create_learning_journey, "LJ", 1)

    def test_get_ljs_returns_them(self):
        self.lj_service.create_learning_journey("Unit testing 101")
        self.assertIsNotNone(self.lj_service.get_learning_journeys())

    def test_archive_returns_true_with_existing_journey(self):
        test_lj = self.lj_service.create_learning_journey("LJ", 1)
        self.assertTrue(self.lj_service.archive(test_lj.id))

    def test_archive_raises_error_with_nonexisting_journey(self):
        self.assertRaises(ValueError, self.lj_service.archive, 999)
