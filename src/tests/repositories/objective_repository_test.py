import unittest
from repositories.objective_repository import test_objective_repo
from repositories.learning_journey_repository import test_learning_journey_repo
from entities.objective import Objective
from entities.learningjourney import LearningJourney


class TestObjectiveRepository(unittest.TestCase):
    def setUp(self):
        """Create a mock Objective Repo and Learning Journey Repo,
        a mock journey and a mock objective."""
        self.objective_repo = test_objective_repo
        self.learning_journey_repo = test_learning_journey_repo
        self.objective_repo.delete_all()
        self.learning_journey_repo.delete_all()

        self.test_journey = LearningJourney("Don't stop believin'", 1)
        self.learning_journey_repo.create(self.test_journey)
        self.test_objective = Objective("Be able to explain how CDs work")

    def test_repo_is_empty_in_the_beginning(self):
        """Verify that the repo is indeed empty."""
        self.assertFalse(self.objective_repo.get_all())

    def test_create(self):
        """Add an Objective to the empty repo and check
        that the names match."""
        objective = self.objective_repo.create(
            self.test_objective.name, self.test_journey.id)
        self.assertEqual("Be able to explain how CDs work",
                         objective["name"])

    def test_create_type_conflict(self):
        """Add a non-string as objective name to the empty repo and make sure an error arises."""
        self.assertRaises(TypeError, self.objective_repo.create(
            True, self.test_journey.id))

    def test_returns_all_objectives(self):
        """Expect a list of all objectives regardless of their lj_id."""
        self.objective_repo.create("Ob 1.1", 1)
        self.objective_repo.create("Ob 1.2", 1)
        self.objective_repo.create("Ob 3.1", 3)
        self.objective_repo.create("Ob 4.1", 4)

        objectives = self.objective_repo.get_all()
        self.assertEqual(len(objectives), 4)

    def test_returns_all_objectives_of_a_given_journey(self):
        """Expect a list of only those objectives that adhere to a specific lj_id."""
        self.objective_repo.create("Ob 1.1", 1)
        self.objective_repo.create("Ob 1.2", 1)
        self.objective_repo.create("Ob 3.1", 3)
        self.objective_repo.create("Ob 4.1", 4)

        objectives = self.objective_repo.get_all(4)
        self.assertEqual(len(objectives), 1)

    def test_objective_gets_deleted(self):
        """Add two objectives to an empty repo, delete one
        and expect only the other to remain."""
        ob1 = self.objective_repo.create("Ob 3.1", 3)
        ob2 = self.objective_repo.create("Ob 4.1", 4)
        self.objective_repo.delete_one(ob1["obj_id"])

        remaining_objectives = self.objective_repo.get_all()
        self.assertEqual(len(remaining_objectives), 1)

    def test_objective_gets_renamed(self):
        """Create an objective, rename it and verify new name."""
        objective = self.objective_repo.create(
            "Be able to explain how CDs work", self.test_journey.id)
        self.objective_repo.rename(
            objective["obj_id"], "Recall Journey's current and past members")
        renamed_objective = self.objective_repo.get_one(objective["obj_id"])

        self.assertEqual("Recall Journey's current and past members",
                         renamed_objective["name"])
