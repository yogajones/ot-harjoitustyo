from tkinter import ttk
from services.objective_service import objective_service
from .base_view import BaseView


class RenameObjectiveView(BaseView):
    def __init__(self, root, show_manage_view, selected_journey, current_id, current_name):
        super().__init__(root)
        self._show_manage_view = show_manage_view
        self._selected_journey = selected_journey

        self._rename_form(current_id, current_name)
        self._return_to_manage_view()

    def _rename_form(self, current_id, current_name):
        self._rename_label = ttk.Label(
            self._frame, text=f"Rename {current_name}")
        self._rename_label.pack()

        self._new_name_entry = ttk.Entry(self._frame)
        self._new_name_entry.pack()

        self._save_button = ttk.Button(
            self._frame, text="Save",
            command=lambda: self._handle_rename_objective(current_id))
        self._save_button.pack()

    def _handle_rename_objective(self, current_id):
        new_name = self._new_name_entry.get()
        if new_name:
            objective_service.rename_objective(current_id, new_name)
            self._show_manage_view(self._selected_journey)

    def _return_to_manage_view(self):
        self._return_btn = ttk.Button(
            self._frame, text="Back",
            command=lambda: self._show_manage_view(self._selected_journey))
        self._return_btn.pack(pady=10)
