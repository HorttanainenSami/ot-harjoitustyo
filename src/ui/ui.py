from tkinter import ttk, constants
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.recipes_view import RecipesView
from ui.create_recipe_view import CreateRecipeView
from ui.recipe_view import RecipeView
from ui.edit_recipe_view import EditRecipeView


class UI:
    def __init__(self, root, service):
        self._root = root
        self._current_view = None
        self._service = service

    def start(self):
        self._show_login_view()
        self._pack()

    def _pack(self):
        self._current_view.pack()

    def _show_login_view(self):
        self._current_view = LoginView(self._root, self.handle_register, self.handle_recipes, self._service)

    def _show_register_view(self):
        self._current_view = RegisterView(self._root, self.handle_login, self._service)

    def _show_create_recipe_view(self):
        self._current_view = CreateRecipeView(self._root, self.handle_recipes, self._service)

    def _show_recipes_view(self):
        self._current_view = RecipesView(self._root, self.handle_login, self.handle_create_recipes, self._service, self.handle_recipe)

    def _show_recipe_view(self, recipe_id):
        self._current_view = RecipeView(self._root, self._service, self.handle_recipes, self.handle_create_recipes, self.handle_edit_recipes, recipe_id)

    def _show_edit_view(self, recipe_id, name, instruction, ingredients):
        self._current_view = EditRecipeView(self._root, self.handle_recipes, self._service, recipe_id, name, instruction, ingredients)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def handle_recipe(self, recipe_id):
        self._hide_current_view()
        self._show_recipe_view(recipe_id)
        self._pack()

    def handle_create_recipes(self):
        self._hide_current_view()
        self._show_create_recipe_view()
        self._pack()

    def handle_edit_recipes(self, recipe_id, name, instruction, ingredients):
        self._hide_current_view()
        self._show_edit_view(recipe_id, name, instruction, ingredients)
        self._pack()

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
