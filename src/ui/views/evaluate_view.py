from tkinter import ttk
from .base_view import BaseView
from services.objective_service import objective_service


class EvaluateView(BaseView):
    def __init__(self, root, objective_id, objective_name, show_manage_view, show_evaluate_view, selected_journey):
        self._show_manage_view = show_manage_view
        self._show_evaluate_view = show_evaluate_view
        self._objective_id = objective_id
        self._objective_name = objective_name
        self._selected_journey = selected_journey

        super().__init__(root)
        self._evaluate_objective_form()

    def _evaluate_objective_form(self):

        # REFACTOR: extract config: font tuple to ui_config,
        # evaluation boundaries to program_config

        progress_label = ttk.Label(
            self._frame, text="Completion:", font=("Arial", 12))
        progress_label.pack()

        progress_label = ttk.Label(
            self._frame, text="Challenge:", font=("Arial", 12))
        progress_label.pack()

        # REFACTOR: replace Spinboxes with a more human-friendly solution:
        #           display current value alongside "+" and "-" buttons,
        #           refresh each time a button is clicked

        self._progress_field = ttk.Spinbox(self._frame, from_=0, to=10)
        self._progress_field.pack()

        self._challenge_field = ttk.Spinbox(self._frame, from_=0, to=10)
        self._challenge_field.pack()

        save_button = ttk.Button(
            self._frame, text="Save", command=self._handle_evaluate)
        save_button.pack()

    def _handle_evaluate(self):
        progress = int(self._progress_field.get())
        challenge = int(self._challenge_field.get())
        objective_service.evaluate_objective(
            self._objective_id, progress, challenge)

        self._refresh()

    def _title(self):
        evaluate_label = ttk.Label(
            self._frame, text=f"Evaluate {self._objective_name}", font=("Arial", 12))
        evaluate_label.pack(pady=20)

    def _return_button(self):
        return_button = ttk.Button(
            self._frame, text="Back", command=lambda: self._show_manage_view(self._selected_journey))
        return_button.pack(pady=10)

    def _refresh(self):
        self._show_evaluate_view(self._objective_id, self._objective_name)
