import tkinter as tk


class BaseView:
    """Template for views, containing common functionalities."""

    def __init__(self, root):
        self._frame = tk.Frame(root)

    def pack(self):
        self._frame.pack()

    def hide(self):
        self._frame.pack_forget()
