import unittest
from repositories.objective_repository import ObjectiveRepository
from repositories.learning_journey_repository import LearningJourneyRepository
from initialize_database import initialize_test_database
from database_connection import get_test_database_connection

test_objective_repo = ObjectiveRepository(get_test_database_connection())
test_learning_journey_repo = LearningJourneyRepository(
    get_test_database_connection())


class TestObjectiveRepository(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self.objective_repo = test_objective_repo
        self.learning_journey_repo = test_learning_journey_repo

        self.test_objective_name = "OB"

        self.test_lj_1 = self.learning_journey_repo.create("LJ_1", 1)
        self.test_lj_2 = self.learning_journey_repo.create("LJ_2", 1)

    def test_repo_is_empty_in_the_beginning(self):
        self.assertFalse(self.objective_repo.get_all())

    def test_create_valid_name_and_lj_id(self):
        objective = self.objective_repo.create(
            self.test_objective_name, self.test_lj_1.id)
        self.assertEqual("OB", objective["name"])

    def test_create_type_conflict(self):
        self.assertRaises(TypeError, self.objective_repo.create(
            True, self.test_lj_1.id))

    def test_returns_all_objectives(self):
        self.objective_repo.create("Ob 1.1", 1)
        self.objective_repo.create("Ob 1.2", 1)
        self.objective_repo.create("Ob 2.1", 2)

        objectives = self.objective_repo.get_all()
        self.assertEqual(len(objectives), 3)

    def test_returns_all_objectives_of_a_given_journey(self):
        self.objective_repo.create("Ob 1.1", 1)
        self.objective_repo.create("Ob 1.2", 1)
        self.objective_repo.create("Ob 2.1", 2)

        objectives = self.objective_repo.get_all(2)
        self.assertEqual(len(objectives), 1)

    def test_objective_gets_deleted(self):
        ob1 = self.objective_repo.create("Ob 3.1", 1)
        ob2 = self.objective_repo.create("Ob 4.1", 2)
        self.objective_repo.delete_one(ob1["obj_id"])

        remaining_objectives = self.objective_repo.get_all()
        self.assertEqual(len(remaining_objectives), 1)

    def test_objective_gets_renamed(self):
        objective = self.objective_repo.create(
            "Before renaming", self.test_lj_1.id)
        self.objective_repo.rename(
            objective["obj_id"], "After renaming")
        renamed_objective = self.objective_repo.get_one(objective["obj_id"])

        self.assertEqual("After renaming",
                         renamed_objective["name"])

    def test_evaluate_operation_succeeds_with_valid_input(self):
        objective = self.objective_repo.create(
            self.test_objective_name, self.test_lj_1.id)
        self.assertTrue(self.objective_repo.evaluate(
            objective["obj_id"], 5, 5))

    # def test_evaluate_operation_fails_with_invalid_input(self):
    #    objective = self.objective_repo.create(
    #        self.test_objective_name, self.test_lj_1.id)
    #    self.assertFalse(self.objective_repo.evaluate(
    #        objective["obj_id"], 20, 5))
    #    self.assertFalse(self.objective_repo.evaluate(
    #        objective["obj_id"], 5, "string"))
    #    self.assertFalse(self.objective_repo.evaluate(
    #        999, 5, 5))

    def evaluate(self, obj_id, progress, challenge):
        if self.get_one(obj_id):
            cursor = self._connection.cursor()
            cursor.execute(sql, (obj_id, progress, challenge))
            self._connection.commit()

            return True
        return False
