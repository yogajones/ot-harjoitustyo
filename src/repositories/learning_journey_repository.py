from entities.learningjourney import LearningJourney

class LearningJourneyRepository:
    "In charge of reading and writing Learning Journeys to/from the database."

    def __init__(self, connection):
        """Establishes a repository for Learning Journey objects to be used in database operations."""
        self._connection = connection

    def create(self, learning_journey: LearningJourney):
        """Appends a Learning Journey to the database and returns it."""
        cursor = self._connection.cursor()
        sql = "INSERT INTO LearningJourneys (name, active) VALUES (?, ?)"
        cursor.execute(sql, (learning_journey.name, learning_journey.active))

        return learning_journey
    
    def get_all(self):
        """Returns all saved Learning Journeys."""
        
        cursor = self._connection.cursor()
        journeys = cursor.execute("SELECT name, active FROM LearningJourneys").fetchall()
        return journeys