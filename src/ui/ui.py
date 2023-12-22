from ui.views.home_view import HomeView
from ui.views.manage_view import ManageView
from ui.views.evaluate_view import EvaluateView
from ui.views.rename_objective_view import RenameObjectiveView


class UI:
    """Coordinates views and keeps track of the selected Learning Journey to manage."""

    def __init__(self, root):
        self._root = root
        self._selected_journey = {}
        self._current_view = None

    def start(self):
        self._show_home_view()

    def _show_home_view(self):
        self._update_view(HomeView(
            self._root, self._show_manage_view, self._show_home_view, self._update_selected_journey))

    def _show_rename_view(self, current_id, current_name):
        self._update_view(RenameObjectiveView(
            self._root, self._show_manage_view, self._selected_journey, current_id, current_name))

    def _show_manage_view(self, journey):
        self._update_selected_journey(journey)
        self._update_view(ManageView(
            self._root, self._show_home_view, self._show_manage_view, self._show_evaluate_view, self._show_rename_view, self._selected_journey))

    def _show_evaluate_view(self, objective_id, objective_name):
        self._update_view(EvaluateView(self._root, objective_id,
                          objective_name, self._show_manage_view, self._show_evaluate_view, self._selected_journey))

    def _update_view(self, new_view):
        if self._current_view:
            self._current_view.hide()
        new_view.pack()
        self._current_view = new_view

    def _update_selected_journey(self, journey):
        self._selected_journey = journey
