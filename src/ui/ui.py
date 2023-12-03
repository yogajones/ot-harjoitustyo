from tkinter import ttk, END
from services.learning_journey_service import learning_journey_service
from services.objective_service import objective_service
import traceback


class UI:
    """
    User Interface class.

    The User Path is currently chained as follows:

        -> Create first Learning Journey
        -> Select that LJ to manage
        -> Go to management view
        -> Add Learning Objectives
    """

    def __init__(self, root):
        self._root = root
        self._selected_journey = None
        self._objective_entry = None
        self._add_journey_frame = None
        self._manage_journey_frame = None
        self._add_objective_frame = None

    def _display_manage_journey(self):
        """Directs the user to add Objectives to the selected Learning Journey."""
        self._manage_journey_frame = ttk.Frame(master=self._root, padding=40)
        ttk.Label(master=self._manage_journey_frame,
                  text=f"Manage Learning Journey: {self._selected_journey.name}.",
                  font=("Arial", 16)).pack()

        # Learning Journey Management Options Menu
        ttk.Button(master=self._manage_journey_frame,
                   text="Add Objectives",
                   command=self._add_objective).pack()
        ttk.Button(master=self._manage_journey_frame,
                   text="Delete",
                   command=self._delete_objective).pack()
        ttk.Button(master=self._manage_journey_frame,
                   text="Evaluate",
                   command=self._evaluate_objective).pack()

        self._manage_journey_frame.pack()

    def _handle_add_objective(self):
        """Using ObjectiveService class, add an Objective."""
        try:
            new_objective = objective_service.create_objective(
                self._objective_entry.get(), self._selected_journey)

            # display success message
            success_message = ttk.Label(master=self._add_objective_frame,
                                        text=f"Awesome! You have succesfully added the Learning Objective: {new_objective.name}."
                                        )
            success_message.pack()
            self._objective_entry.delete(0, END)
            self._add_objective_frame.after(10000, success_message.pack_forget)

        except Exception as e:
            ttk.Label(master=self._root,
                      text="Something went terribly wrong!").pack()
            traceback.print_exc()

    def _add_objective(self):
        """Input form for adding a new Objective."""
        if self._add_objective_frame is not None:
            self._add_objective_frame.pack_forget()

        self._add_objective_frame = ttk.Frame(master=self._manage_journey_frame,
                                              padding=40)

        ttk.Label(master=self._add_objective_frame,
                  text="Objective:").pack()
        self._objective_entry = ttk.Entry(master=self._add_objective_frame)
        self._objective_entry.pack()
        ttk.Button(master=self._add_objective_frame,
                   text="Add",
                   command=self._handle_add_objective).pack()
        self._add_objective_frame.pack()

    def _delete_objective(self):
        """TODO"""
        self._add_objective()

    def _evaluate_objective(self):
        """TODO"""
        self._add_objective()

    def _handle_add_journey(self):
        """Using LearningJourneyService class, add a journey."""
        try:
            new_journey = learning_journey_service.create_learning_journey(
                self._lj_name_entry.get())

            # clear the view and display success message
            self._add_journey_frame.pack_forget()
            ttk.Label(master=self._root,
                      text=f"Great! You have now begun a new Learning Journey: {new_journey.name}.", padding=20, font=("Arial", 16)).pack()

            self._selected_journey = new_journey

            # redirect to manage the new journey
            self._display_manage_journey()

        except Exception as e:
            ttk.Label(master=self._root,
                      text="Something went terribly wrong!").pack()
            traceback.print_exc()

    def _add_journey(self):
        """Input form for adding a new Learning Journey."""
        ttk.Label(master=self._add_journey_frame,
                  text="Learning Journey name:").pack()
        self._lj_name_entry = ttk.Entry(master=self._add_journey_frame)
        self._lj_name_entry.pack()
        ttk.Button(master=self._add_journey_frame, text="Add",
                   command=self._handle_add_journey).pack()
        self._add_journey_frame.pack()

    def _display_first_journey_prompt(self):
        """Directs the user to add their first Learning Journey."""

        self._add_journey_frame = ttk.Frame(master=self._root)
        self._first_lj_label = ttk.Label(
            master=self._add_journey_frame,
            text='''Hello there! Let's get you started by beginning
                 your first Learning Journey.''').pack()
        ttk.Label(master=self._add_journey_frame, text="").pack()
        self._add_journey_frame.pack()

        self._add_journey()

    def _display_existing_journeys(self):
        """TODO"""
        pass

    def start(self):
        """Starts the user interface."""

        if learning_journey_service.get_learning_journeys():
            self._display_first_journey_prompt()
            # FEATURE: replace the above with this when feature done:
            # self._display_existing_journeys()
        else:
            self._display_first_journey_prompt()
