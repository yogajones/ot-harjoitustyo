from tkinter import ttk, CENTER
from .base_view import BaseView
from services.objective_service import objective_service


class EvaluateView(BaseView):
    def __init__(self, root, objective_id, objective_name, show_manage_view, show_evaluate_view, selected_journey):
        self._show_manage_view = show_manage_view
        self._show_evaluate_view = show_evaluate_view
        self._objective_id = objective_id
        self._objective_name = objective_name
        self._selected_journey = selected_journey

        self._current_progress = objective_service.get_evaluations(self._objective_id)[
            'progress']
        self._current_challenge = objective_service.get_evaluations(self._objective_id)[
            'challenge']

        super().__init__(root)

        self._evaluate_objective_form()

    def _evaluate_objective_form(self):

        # REFACTOR: extract config: font tuple to ui_config,
        # evaluation boundaries to program_config

        self._progress_field = self._spinbox_frame(
            label_text="Completion: ", current_value=self._current_progress)
        self._challenge_field = self._spinbox_frame(
            label_text="Challenge: ", current_value=self._current_challenge)

        save_button = ttk.Button(
            self._frame, text="Save", command=self._handle_evaluate)
        save_button.pack(side='left', pady=25, padx=10)

        return_button = ttk.Button(
            self._frame, text="Back", command=lambda: self._show_manage_view(self._selected_journey))
        return_button.pack(side='right', pady=25, padx=10)

    def _spinbox_frame(self, label_text, current_value):
        frame = ttk.Frame(self._frame)
        label = ttk.Label(frame, text=label_text, font=("Arial", 12), width=11)
        label.pack(side='left', pady=15)
        entry_field = self._spinbox(frame, current_value)
        entry_field.pack(side='right')
        frame.pack(fill='x')
        return entry_field

    def _spinbox(self, frame, current_value):
        return ttk.Spinbox(
            frame, from_=0, to=10, style="TSpinbox",
            textvariable=current_value, state="readonly",
            font=("Arial", 20), width=2, justify=CENTER)

    def _handle_evaluate(self):
        progress = int(self._progress_field.get())
        challenge = int(self._challenge_field.get())
        objective_service.evaluate_objective(
            self._objective_id, progress, challenge)

        self._show_manage_view(self._selected_journey)

    def _title(self):
        evaluate_label = ttk.Label(
            self._frame, text=f"Evaluate {self._objective_name}", font=("Arial", 12))
        evaluate_label.pack(pady=20)
