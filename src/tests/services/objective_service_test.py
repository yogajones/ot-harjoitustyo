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
        self.ob1 = self.objective_service.create_objective(
            "Ob1", self.test_journey.id)

    def test_create_objective_valid_input(self):
        objective = self.objective_service.create_objective(
            "Ob2", self.test_journey.id)
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
        self.assertIsNotNone(self.objective_service.get_objectives())

    def test_delete_objective_returns_true(self):
        self.assertTrue(
            self.objective_service.delete_objective(self.ob1["obj_id"]))

    def test_delete_objective_with_invalid_id_returns_false(self):
        self.assertFalse(self.objective_service.delete_objective(999))

    def test_rename_objective_returns_true(self):
        self.assertTrue(self.objective_service.rename_objective(
            self.ob1["obj_id"], "New name"))

    def test_rename_objective_returns_fails_with_empty_new_name(self):

        self.assertFalse(self.objective_service.rename_objective(
            self.ob1["obj_id"], ""))

    def test_evaluate_objective_returns_true_with_valid_input(self):
        self.assertTrue(
            self.objective_service.evaluate_objective(self.ob1["obj_id"], 5, 5))

    def test_evaluate_objective_returns_false_with_invalid_input(self):
        self.assertFalse(
            self.objective_service.evaluate_objective(self.ob1["obj_id"], 20, 5))
        self.assertFalse(
            self.objective_service.evaluate_objective(999, 5, 5))
        self.assertFalse(
            self.objective_service.evaluate_objective(True, 20, 5))
        self.assertFalse(
            self.objective_service.evaluate_objective(self.ob1["obj_id"], "string", 5))

    def test_get_evaluations_returns_them(self):
        self.objective_service.evaluate_objective(self.ob1["obj_id"], 20, 5)
        self.assertIsNotNone(
            self.objective_service.get_evaluations(self.ob1["obj_id"]))

    def test_get_evaluations_returns_default_0_if_no_evaluations(self):
        evs = self.objective_service.get_evaluations(self.ob1["obj_id"])
        self.assertEqual(evs["progress"], 0)
        self.assertEqual(evs["challenge"], 0)
