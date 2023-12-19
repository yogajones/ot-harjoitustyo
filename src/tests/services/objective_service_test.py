import unittest
from services.objective_service import ObjectiveService
from repositories.learning_journey_repository import test_learning_journey_repo
from repositories.objective_repository import test_objective_repo
from initialize_database import initialize_test_database
from entities.learningjourney import LearningJourney
from entities.objective import Objective


class TestObjectiveService(unittest.TestCase):
    def setUp(self):
        """Create an Objective Service instance
        that uses an emptied mock repository."""
        initialize_test_database()
        self.learning_journey_repo = test_learning_journey_repo
        self.objective_repo = test_objective_repo
        self.test_journey = LearningJourney("Babbys first LJ")
        self.learning_journey_repo.create(self.test_journey)

        self.objective_service = ObjectiveService(self.objective_repo)

    def test_create_objective_valid_input(self):
        """With valid input, succesfully create and return an objective dictionary."""
        objective = self.objective_service.create_objective(
            "Some stupid objective", self.test_journey.id)
        self.assertIsInstance(objective, dict)

    def test_create_objective_empty_name(self):
        """With an invalid input (empty name), return an error."""
        self.assertIsInstance(
            self.objective_service.create_objective("", self.test_journey), ValueError)
        self.assertIsInstance(self.objective_service.create_objective(
            "Fifty characters is the upper limit for Objective name",
            self.test_journey), ValueError)

    def test_create_objective_type_conflict(self):
        """With an invalid input (wrong type), return an error."""
        self.assertIsInstance(
            self.objective_service.create_objective(
                True, self.test_journey), TypeError)
        self.assertIsInstance(
            self.objective_service.create_objective(
                Objective("Valid"), "Not valid"), TypeError)

    def test_get_objectives_returns_them(self):
        """When an Objective is known to be added, make sure it is returned."""
        self.objective_service.create_objective(
            "Gain experience with Unittest", self.test_journey.id)
        self.assertIsNotNone(self.objective_service.get_objectives())

    def test_delete_objective_returns_true(self):
        """If the method call returns True, the operation was succesful."""
        ob1 = self.objective_service.create_objective(
            "Ob1", self.test_journey.id)
        self.assertTrue(self.objective_service.delete_objective(ob1["obj_id"]))

    def test_delete_objective_with_invalid_id_returns_false(self):
        """With a non-existing obj_id, the method should return False."""
        self.assertFalse(self.objective_service.delete_objective(999))

    def test_rename_objective_returns_true(self):
        """With a valid new name, the method should return True."""
        ob1 = self.objective_service.create_objective(
            "Ob1", self.test_journey.id)
        self.assertTrue(self.objective_service.rename_objective(
            ob1["obj_id"], "New name"))

    def test_rename_objective_returns_fails_with_empty_new_name(self):
        ob1 = self.objective_service.create_objective(
            "Ob1", self.test_journey.id)
        self.assertFalse(self.objective_service.rename_objective(
            ob1["obj_id"], ""))
