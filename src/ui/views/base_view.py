import tkinter as tk
from tkinter import ttk, CENTER


class BaseView:
    """Template for views, containing common functionalities."""

    def __init__(self, root):
        self._frame = tk.Frame(root)
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TSpinbox', arrowsize=20)

        self._title()
        self._return_button()

    def _title(self):
        pass

    def _return_button(self):
        pass

    def _list_items(self, items, buttons):
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

    def _form_one_entry(self, label_text, btn_text, handler, pre_filled_value=None):
        label = ttk.Label(self._frame, text=label_text)
        label.pack()

        entry = ttk.Entry(self._frame)
        if pre_filled_value:
            entry.insert(0, pre_filled_value)
        entry.pack()

        button = ttk.Button(
            self._frame, text=btn_text, command=handler)
        button.pack()

        return entry

    def _input_validation_error(self, input=""):
        if len(input.strip()) == 0:
            return "The field cannot be empty. Please try again."
        if len(input.strip()) > 50:
            return "The maximum number of characters for this field is 50."

    def pack(self):
        self._frame.pack()

    def hide(self):
        self._frame.pack_forget()
