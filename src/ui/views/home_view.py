import tkinter as tk
from tkinter import ttk
from services.learning_journey_service import learning_journey_service


class HomeView:
    """Allows the user to add a new Learning Journey and redirects them to manage existing ones."""

    # BUG: When the user adds a certain number of journeys, they overflow out of sight.
    #      A scrollbar or other solution is needed.

    def __init__(self, root, show_manage_view, show_home_view, update_selected_journey):
        self._frame = tk.Frame(root)
        self._show_manage_view = show_manage_view
        self._show_home_view = show_home_view
        self._update_selected_journey = update_selected_journey

        self._add_new_journey_form()
        self._list_journeys()

    def _add_new_journey_form(self):
        self._add_new_journey_label = ttk.Label(
            self._frame, text="Add new Learning Journey")
        self._add_new_journey_label.pack()

        self._new_journey_entry = ttk.Entry(self._frame)
        self._new_journey_entry.pack()

        self._add_button = ttk.Button(
            self._frame, text="Add", command=self._handle_add_new_journey)
        self._add_button.pack()

    def _list_journeys(self):
        journeys = learning_journey_service.get_learning_journeys()
        for journey in journeys:
            journey_frame = tk.Frame(self._frame)

            label = ttk.Label(
                journey_frame, text=journey['name'], font=("Arial", 12))
            label.pack(side='left', padx=20, pady=10)

            manage_button = ttk.Button(journey_frame, text="Manage Objectives",
                                       command=lambda journey=journey: self._show_manage_view(journey))
            manage_button.pack(side='right')

            journey_frame.pack(fill='x')

    def _handle_add_new_journey(self):
        journey_name = self._new_journey_entry.get()
        if journey_name:
            learning_journey_service.create_learning_journey(journey_name)
            self._refresh()

    def _refresh(self):
        self._show_home_view()

    def pack(self):
        self._frame.pack()

    def hide(self):
        self._frame.pack_forget()
