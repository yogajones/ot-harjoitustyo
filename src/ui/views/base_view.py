import tkinter as tk
from tkinter import ttk


class BaseView:
    """Template for views, containing common functionalities."""

    def __init__(self, root):
        self._frame = tk.Frame(root)

    def list_items(self, items, buttons):
        for item in items:
            item_frame = tk.Frame(self._frame)

            label = ttk.Label(item_frame,
                              text=item['name'], font=("Arial", 12))
            label.pack(side='left', padx=20, pady=10)

            for text, command in buttons.items():
                button = ttk.Button(item_frame, text=text,
                                    command=lambda item=item, cmd=command: cmd(item))
                button.pack(side='right')

            item_frame.pack(fill='x')

    def form_add_new(self, label_text, add_handler):
        add_label = ttk.Label(self._frame, text=label_text)
        add_label.pack()

        new_entry = ttk.Entry(self._frame)
        new_entry.pack()

        add_button = ttk.Button(self._frame, text="Add", command=add_handler)
        add_button.pack()

        return new_entry

    def pack(self):
        self._frame.pack()

    def hide(self):
        self._frame.pack_forget()
