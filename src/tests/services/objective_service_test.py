import unittest
from services.objective_service import ObjectiveService
from repositories.learning_journey_repository import LearningJourneyRepository
from repositories.objective_repository import ObjectiveRepository
from entities.objective import Objective
from initialize_database import initialize_test_database
from database_connection import get_test_database_connection

test_objective_repo = ObjectiveRepository(get_test_database_connection())
test_learning_journey_repo = LearningJourneyRepository(
    get_test_database_connection())


class TestObjectiveService(unittest.TestCase):
    def setUp(self):
        """Create an Objective Service instance
        that uses an emptied mock repository."""
        initialize_test_database()
        self.learning_journey_repo = test_learning_journey_repo
        self.objective_repo = test_objective_repo

        self.test_journey = self.learning_journey_repo.create("LJ")
        self.objective_service = ObjectiveService(self.objective_repo)

    def test_create_objective_valid_input(self):
        objective = self.objective_service.create_objective(
            "OB", self.test_journey.id)
        self.assertIsInstance(objective, dict)

    def test_create_objective_empty_name(self):
        self.assertIsInstance(
            self.objective_service.create_objective("", self.test_journey), ValueError)
        self.assertIsInstance(self.objective_service.create_objective(
            "Fifty characters is the upper limit for Objective name",
            self.test_journey), ValueError)

    def test_create_objective_type_conflict(self):
        self.assertIsInstance(
            self.objective_service.create_objective(
                True, self.test_journey), TypeError)
        self.assertIsInstance(
            self.objective_service.create_objective(
                Objective("Valid"), "Not valid"), TypeError)

    def test_get_objectives_returns_them(self):
        self.objective_service.create_objective(
            "Gain experience with Unittest", self.test_journey.id)
        self.assertIsNotNone(self.objective_service.get_objectives())

    def test_delete_objective_returns_true(self):
        ob1 = self.objective_service.create_objective(
            "Ob1", self.test_journey.id)
        self.assertTrue(self.objective_service.delete_objective(ob1["obj_id"]))

    def test_delete_objective_with_invalid_id_returns_false(self):
        self.assertFalse(self.objective_service.delete_objective(999))

    def test_rename_objective_returns_true(self):
        ob1 = self.objective_service.create_objective(
            "Ob1", self.test_journey.id)
        self.assertTrue(self.objective_service.rename_objective(
            ob1["obj_id"], "New name"))

    def test_rename_objective_returns_fails_with_empty_new_name(self):
        ob1 = self.objective_service.create_objective(
            "Ob1", self.test_journey.id)
        self.assertFalse(self.objective_service.rename_objective(
            ob1["obj_id"], ""))
