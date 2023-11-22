from tkinter import ttk
from services.learning_journey_service import learning_journey_service


class UI:
    """User Interface class"""

    def __init__(self, root):
        self._root = root

    def add_entry_handler(self):
        """Using LearningJourneyService class, add a journey."""
        new_lj_name = self.lj_name_entry.get()
        learning_journey_service.create_learning_journey(new_lj_name)

        # REFACTOR / TEST
        # print all journeys to test that it works
        # add better tests in Sprint 2
        current_journeys = [(j[0], j[1])
                            for j in learning_journey_service.get_learning_journeys()]
        test = ttk.Label(master=self._root, text=str(current_journeys))
        test.pack()

    def start(self):
        """Starts the user interface."""

        # REFACTOR
        # the code below should be moved to another class but called
        # from within this start() function
        # also make self variables private

        self.lj_name_label = ttk.Label(
            master=self._root, text="Learning Journey name:")
        self.lj_name_entry = ttk.Entry(master=self._root)
        self.lj_name_submit = ttk.Button(
            master=self._root, text="Add", command=self.add_entry_handler)

        self.lj_name_label.pack()
        self.lj_name_entry.pack()
        self.lj_name_submit.pack()
