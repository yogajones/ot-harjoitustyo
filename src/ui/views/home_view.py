from tkinter import messagebox
from services.learning_journey_service import learning_journey_service
from .base_view import BaseView


class HomeView(BaseView):
    """Allows the user to add a new Learning Journey and redirects them to manage existing ones."""

    def __init__(self, root, show_manage_view, show_home_view, update_selected_journey):
        super().__init__(root)
        self._show_manage_view = show_manage_view
        self._show_home_view = show_home_view
        self._update_selected_journey = update_selected_journey

        self._add_new_journey_form()
        self._list_journeys()

    def _add_new_journey_form(self):
        self._new_journey_entry = self._form_one_entry("Add new Learning Journey",
                                                       "Add",
                                                       self._handle_add_new_journey)

    def _list_journeys(self):
        journeys = learning_journey_service.get_learning_journeys()
        buttons = {"Manage Objectives": self._show_manage_view}
        self._list_items(journeys, buttons)

    def _handle_add_new_journey(self):
        journey_name = self._new_journey_entry.get().strip()
        if self._input_validation_error(journey_name):
            messagebox.showerror(title="Input validation error",
                                 message=self._input_validation_error(journey_name))
            self._refresh()
        else:
            try:
                learning_journey_service.create_learning_journey(journey_name)
            except Exception as e:
                messagebox.showerror(title="Application error", message=str(e))
            self._refresh()

    def _refresh(self):
        self._show_home_view()
