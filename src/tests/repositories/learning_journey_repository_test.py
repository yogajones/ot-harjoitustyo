import unittest
from repositories.learning_journey_repository import learning_journey_repo
from entities.learningjourney import LearningJourney


class TestLearningJourneyRepository(unittest.TestCase):
    def setUp(self):
        """Empty the repo and create a mock Learning Journey for later use."""
        self.learning_journey_repo = learning_journey_repo
        self.learning_journey_repo.delete_all()
        self.test_journey = LearningJourney("Don't stop believin'", 1)

    def test_repo_is_empty_in_the_beginning(self):
        """Verify that the repo is indeed empty."""
        self.assertFalse(self.learning_journey_repo.get_all())

    def test_create(self):
        """Add a Learning Journey to the empty repo and check
        that the names match."""
        self.learning_journey_repo.create(self.test_journey)
        learning_journeys = self.learning_journey_repo.get_all()
        self.assertEqual("Don't stop believin'", learning_journeys[0][0])

    def test_create_type_conflict(self):
        """Add an object that is not a Learning Journey to the empty repo
        and make sure an error arises."""
        self.assertRaises(TypeError, self.learning_journey_repo.create(True))
