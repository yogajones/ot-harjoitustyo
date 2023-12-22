from tkinter import ttk, messagebox
from services.objective_service import objective_service
from .base_view import BaseView


class ManageView(BaseView):
    """Allows the user to view or add Learning Objectives to the selected Learning Journey."""

    def __init__(self, root, show_home_view, show_manage_view, show_evaluate_view, show_rename_view, selected_journey):
        self._show_home_view = show_home_view
        self._show_manage_view = show_manage_view
        self._show_rename_view = show_rename_view
        self._show_evaluate_view = show_evaluate_view
        self._selected_journey = selected_journey

        super().__init__(root)
        self._add_new_objective_form()
        self._list_objectives()

    def _list_objectives(self):
        objectives = objective_service.get_objectives(
            self._selected_journey["id"])
        buttons = {
            "Delete": lambda objective: self._handle_delete_objective(objective["id"]),
            "Rename": lambda objective: self._show_rename_view(objective["id"], objective["name"]),
            "Evaluate": lambda objective: self._show_evaluate_view(objective["id"], objective["name"])
        }
        self._list_items(objectives, buttons)

    def _handle_delete_objective(self, obj_id):
        objective_service.delete_objective(obj_id)
        self._refresh()

    def _add_new_objective_form(self):
        self._new_objective_entry = self._form_one_entry("Add new Learning Objective",
                                                         "Add",
                                                         self._handle_add_new_objective)

    def _handle_add_new_objective(self):
        objective_name = self._new_objective_entry.get().strip()
        if self._input_validation_error(objective_name):
            messagebox.showerror(title="Input validation error",
                                 message=self._input_validation_error(objective_name))
            self._refresh()
        else:
            try:
                objective_service.create_objective(
                    objective_name, self._selected_journey["id"])
            except Exception as e:
                messagebox.showerror(title="Application error", message=str(e))
            self._refresh()

    def _title(self):
        manage_label = ttk.Label(
            self._frame, text=f"Manage {self._selected_journey['name']}", font=("Arial", 12))
        manage_label.pack(pady=20)

    def _return_button(self):
        return_button = ttk.Button(
            self._frame, text="Return to Home", command=self._show_home_view)
        return_button.pack(pady=10)

    def _refresh(self):
        self._show_manage_view(self._selected_journey)
