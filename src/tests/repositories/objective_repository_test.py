import unittest
from repositories.objective_repository import objective_repo
from repositories.learning_journey_repository import learning_journey_repo
from entities.objective import Objective
from entities.learningjourney import LearningJourney


class TestObjectiveRepository(unittest.TestCase):
    def setUp(self):
        """Create a mock Objective Repo and Learning Journey Repo,
        a mock journey and a mock objective."""
        self.objective_repo = objective_repo
        self.learning_journey_repo = learning_journey_repo
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
        self.objective_repo.create(self.test_objective, self.test_journey)
        objectives = self.objective_repo.get_all()
        self.assertEqual("Be able to explain how CDs work", objectives[0].name)

    def test_create_type_conflict(self):
        """Add an object that is not a Objective to the empty repo
        and make sure an error arises."""
        self.assertRaises(TypeError, self.objective_repo.create(
            "I'm just a string", self.test_journey))
