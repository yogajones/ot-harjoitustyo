from tkinter import ttk
from services.objective_service import objective_service
from .base_view import BaseView


class RenameObjectiveView(BaseView):
    def __init__(self, root, show_manage_view, selected_journey, current_id, current_name):
        self._show_manage_view = show_manage_view
        self._selected_journey = selected_journey
        self._current_name = current_name
        self._current_id = current_id

        super().__init__(root)
        self._rename_form()

    def _rename_form(self):
        self._new_name_entry = self._form_one_entry(f"Rename {self._current_name}",
                                                    "Save",
                                                    self._handle_rename_objective,
                                                    self._current_name)

    def _handle_rename_objective(self):
        new_name = self._new_name_entry.get()
        if new_name:
            objective_service.rename_objective(self._current_id, new_name)
            self._show_manage_view(self._selected_journey)

    def _return_button(self):
        self._return_btn = ttk.Button(
            self._frame, text="Back",
            command=lambda: self._show_manage_view(self._selected_journey))
        self._return_btn.pack(pady=10)
