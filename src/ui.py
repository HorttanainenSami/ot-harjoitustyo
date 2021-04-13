from tkinter import ttk, constants
from login_view import LoginView
from register_view import RegisterView
from recipes_view import RecipesView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()
        self._pack()

    def _pack(self):
        self._current_view.pack()
    def _show_login_view(self):
        self._current_view = LoginView(self._root, self.handle_register, self.handle_recipes)

    def _show_register_view(self):
        self._current_view = RegisterView(self._root, self.handle_login)

    def _show_recipes_view(self):
        self._current_view = RecipesView(self._root)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def handle_recipes(self):
        self._hide_current_view()
        self._show_recipes_view()
        self._pack()

    def handle_register(self):
        self._hide_current_view()
        self._show_register_view()
        self._pack()

    def handle_login(self):
        self._hide_current_view()
        self._show_login_view()
        self._pack()
