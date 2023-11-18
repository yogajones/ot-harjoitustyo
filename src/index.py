from repositories.learning_journey_repository import LearningJourneyRepository
from initialize_database import initialize_database
from database_connection import get_database_connection
from services.learning_journey_service import LearningJourneyService

def main():
    # reset the database
    initialize_database()

    # connect to database
    # create a repo for learning journeys
    # create a learning journey
    repo = LearningJourneyRepository(get_database_connection())
    service = LearningJourneyService(repo)
    service.create_learning_journey(name="My First Journey", active=1)
    
    # a quick test to try if the above works
    if not service.get_learning_journeys():
        print("Error")
    else:
        for row in service.get_learning_journeys():
            print(f"These Learning Journeys are currently saved: {row[0]}")

if __name__ == "__main__":
    main()