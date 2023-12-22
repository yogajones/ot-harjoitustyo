from entities.learningjourney import LearningJourney
from database_connection import get_database_connection


class AlreadyInUse(Exception):
    pass


class LearningJourneyRepository:
    """In charge of reading and writing Learning Journeys
    to/from the database.
    """

    def __init__(self, connection):
        self._connection = connection

    def get_one(self, lj_name):
        """Returns a database row from LearningJourneys table
        if a reference is found.

        Args:
            lj_name (str): The name of the Learning Journey to fetch.

        Returns:
            sqlite3.Row: Database row from LearningJourneys table.
        """
        cursor = self._connection.cursor()
        sql = "SELECT id, name, active FROM LearningJourneys WHERE name = ?"
        result = cursor.execute(sql, (lj_name,)).fetchone()
        self._connection.commit()

        return result

    def _validate(self, name, active):
        if not isinstance(name, str) or not isinstance(active, int):
            raise TypeError()
        if self.get_one(name):
            raise AlreadyInUse(f"The name {name} is already in use.")
        if len(name.strip()) == 0:
            raise ValueError(f"Name cannot be empty.")
        if active not in [0, 1]:
            raise ValueError(
                "A Learning Journey can be either active (1) or passive (0).")

    def create(self, name, active=1):
        """Appends a Learning Journey to the database and returns it.

        Args:
            name (str): Name of the new Learning Journey, input from user.
            active (int, optional): Activity status of the LJ. Defaults to 1.

        Returns:
            LearningJourney: Newly created Learning Journey.
        """
        self._validate(name, active)

        cursor = self._connection.cursor()
        sql = "INSERT INTO LearningJourneys (name, active) VALUES (?, ?)"
        cursor.execute(sql, (name, active))
        lj_id = cursor.lastrowid
        self._connection.commit()

        return LearningJourney(name, active, lj_id)

    def get_all(self):
        """Returns all saved Learning Journeys, parsed to a list of dictionaries.

        Returns:
            list: List of dictionaries containing existing Learning Journeys.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT id, name, active FROM LearningJourneys")
        journeys_data = cursor.fetchall()
        self._connection.commit()

        journeys = []
        for journey_data in journeys_data:
            journey_dict = {
                "id": journey_data[0],
                "name": journey_data[1],
                "active": journey_data[2]
            }
            journeys.append(journey_dict)

        return journeys


learning_journey_repo = LearningJourneyRepository(get_database_connection())
