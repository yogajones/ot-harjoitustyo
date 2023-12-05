class LearningJourney:

    def __init__(self, name: str, active=1, lj_id=None) -> None:
        """Creates a new, active Learning Journey."""
        self.id = lj_id
        self.name = name
        self.active = active
