from initialize_database import initialize_database


def build():
    """Build tasks:
        - empty existing data in database and replace with empty tables
    """
    initialize_database()


if __name__ == "__main__":
    build()
