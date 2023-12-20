class Objective:

    def __init__(self, name: str, lj_id=None, progress=None, challenge=None) -> None:
        """Creates a new Objective."""
        self.name = name
        self.lj_id = lj_id
        self.progress = progress
        self.challenge = challenge
