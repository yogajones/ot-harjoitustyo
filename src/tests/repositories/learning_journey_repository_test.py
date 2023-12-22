import unittest
from repositories.learning_journey_repository import LearningJourneyRepository, AlreadyInUse
from initialize_database import initialize_test_database
from database_connection import get_test_database_connection

test_learning_journey_repo = LearningJourneyRepository(
    get_test_database_connection())


class TestLearningJourneyRepository(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self.learning_journey_repo = test_learning_journey_repo
        self.test_lj_name = "LJ"

    def test_repo_is_empty_in_the_beginning(self):
        self.assertFalse(self.learning_journey_repo.get_all())

    def test_new_LJ_with_valid_input(self):
        result = self.learning_journey_repo.create(self.test_lj_name, 1)
        self.assertEqual("LJ", result.name)

    def test_new_LJ_with_empty_name(self):
        self.assertRaises(ValueError, self.learning_journey_repo.create, "", 1)

    def test_new_LJ_with_name_already_taken(self):
        self.learning_journey_repo.create(self.test_lj_name, 1)
        self.assertRaises(
            AlreadyInUse, self.learning_journey_repo.create, "LJ", 1)

    def test_new_LJ_with_all_whitespace_name(self):
        self.assertRaises(
            ValueError, self.learning_journey_repo.create, "       ", 1)

    def test_get_one_with_valid_input(self):
        self.learning_journey_repo.create(self.test_lj_name, 1)
        result = self.learning_journey_repo.get_one(self.test_lj_name)
        self.assertIsNotNone(result)

    def test_get_one_with_nonexisting_lj(self):
        self.learning_journey_repo.create(self.test_lj_name, 1)
        result = self.learning_journey_repo.get_one("bamboozle")
        self.assertIsNone(result)

    def test_get_all_returns_all(self):
        self.learning_journey_repo.create("First", 1)
        self.learning_journey_repo.create("Second", 1)
        self.learning_journey_repo.create("Third", 1)

        result = self.learning_journey_repo.get_all()
        self.assertEqual(len(result), 3)
