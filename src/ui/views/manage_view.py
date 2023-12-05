import tkinter as tk
from tkinter import ttk
from services.objective_service import objective_service


class ManageView:
    """Allows the user to view or add Learning Objectives to the selected Learning Journey."""

    def __init__(self, root, show_home_view, show_manage_view, selected_journey):
        self._frame = tk.Frame(root)
        self._show_home_view = show_home_view
        self._show_manage_view = show_manage_view
        self._selected_journey = selected_journey

        # REFACTOR: find a better place for these widgets
        self._manage_label = ttk.Label(
            self._frame, text=f"Manage {self._selected_journey['name']}", font=("Arial", 12))
        self._manage_label.pack(pady=20)

        self._return_button = ttk.Button(
            self._frame, text="Return to Home", command=self._show_home_view)
        self._return_button.pack(pady=10)

        self._add_new_objective_form()
        self._list_objectives()

    def _list_objectives(self):
        objectives = objective_service.get_objectives(
            self._selected_journey['id'])
        for objective in objectives:
            objective_frame = tk.Frame(self._frame)

            label = ttk.Label(
                objective_frame, text=objective['name'], font=("Arial", 12))
            label.pack(side='left', padx=20, pady=10)

            objective_frame.pack(fill='x')

    def _add_new_objective_form(self):
        self._add_new_objective_label = ttk.Label(
            self._frame, text="Add new Learning Objective")
        self._add_new_objective_label.pack()

        self._new_objective_entry = ttk.Entry(self._frame)
        self._new_objective_entry.pack()

        self._add_button = ttk.Button(
            self._frame, text="Add", command=self._handle_add_new_objective)
        self._add_button.pack()

    def _handle_add_new_objective(self):
        objective_name = self._new_objective_entry.get()
        if objective_name:
            objective_service.create_objective(
                objective_name, self._selected_journey['id'])
            self._refresh()

    def _refresh(self):
        self._show_manage_view(self._selected_journey)

    def pack(self):
        self._frame.pack()

    def hide(self):
        self._frame.pack_forget()
