class LearningJourney:

    def __init__(self, name: str, active=1, id=None) -> None:
        """Creates a new, active Learning Journey."""
        self.id = id
        self.name = name
        self.active = active
