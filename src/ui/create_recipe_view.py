from tkinter import ttk, constants, StringVar, Text
from ui.edit_recipe_view import IngredientList, HeaderFrame

class CreateRecipeView:
    def __init__(self, root, recipes, service):
        self._root = root

        self._frame = None
        self._header_frame = HeaderFrame(self._root, '')
        self._ingredients_frame = IngredientList(self._root, [])

        self._show_recipes = recipes
        self._recipe_service = service

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_save(self, instruction):
        recipe_name = self._header_frame.get_recipe_name()
        ingredients = self._ingredients_frame.get_ingredients_list()
        self._recipe_service.create_recipe(recipe_name, ingredients, instruction)

        self._header_frame.destroy()
        self._ingredients_frame.destroy()
        self._show_recipes()

    def _initialize_ingredients(self):
        self._ingredients_frame.pack()

    def _initialize_instruction(self):
        instruction_lbl = ttk.Label(master=self._frame, text='Instructions:')
        instruction_txt = Text(master=self._frame, width=40, height=20)

        button = ttk.Button(
            master=self._frame,
            text='save',
            command=lambda: self._handle_save(instruction_txt.get('1.0', 'end'))
            )
        instruction_lbl.grid(padx=5, pady=5)
        instruction_txt.grid(padx=5, pady=5, columnspan=3)
        button.grid(padx=5, pady=5)

    def _initialize(self):
        self._root.title('Create recipe view')
        self._frame = ttk.Frame(master=self._root)

        # initializing components
        self._header_frame.pack()
        self._initialize_ingredients()
        self._initialize_instruction()
