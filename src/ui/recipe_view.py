from tkinter.messagebox import askyesno
from tkinter import ttk, constants, Text
from sys import exit
import datetime

class RecipeView:
    def __init__(self, root, service, recipes_view, create_recipe_view, edit_recipe, recipe):
        self._root = root
        self._frame = None
        self._recipe_service = service
        self._recipes_view = recipes_view
        self._show_create_recipe_view = create_recipe_view
        self._edit_recipe = edit_recipe
        self._recipe = recipe
        self._ingredients = []
        self._initialize_data()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def show_recipes(self):
        self._recipes_view()

    def edit_recipe(self):
        name = self._recipe[2]
        instructions = self._recipe[3]
        self._edit_recipe(self._recipe[0], name, instructions, self._ingredients)

    def _initialize_data(self):
        ingredients = self._recipe_service.get_ingredients(self._recipe[0])
        for ingredient in ingredients:
            self._ingredients.append(ingredient)

    def _handle_produce(self):
        self._recipe_service.set_recipe_produced(self._recipe[0])

    def _handle_delete(self):
        answer = askyesno(
            title='Confirmation',
            message='Are you sure you want to delete this recipe?'
        )
        if answer:
            self._recipe_service.delete_recipe(self._recipe[0])
            self._recipes_view()

    def _initialize_nav(self):
        back_btn = ttk.Button(
            master=self._frame,
            text='Go back',
            command=self._recipes_view
            )

        produce_btn = ttk.Button(
            master=self._frame,
            text='Produce',
            command=self._handle_produce
            )

        modify_btn = ttk.Button(
            master=self._frame,
            text='Modify',
            command=self.edit_recipe
            )

        delete_btn = ttk.Button(
            master=self._frame,
            text='Delete',
            command=self._handle_delete
            )
        back_btn.grid()
        produce_btn.grid(row=0, column=1)
        modify_btn.grid(row=0, column=2)
        delete_btn.grid(row=0, column=3)

    def _initialize_content(self):
        name_lbl = ttk.Label(master=self._frame, text=self._recipe[2])
        name_lbl.grid(padx=20, pady=20)

        ingredients_lbl = ttk.Label(master=self._frame, text='Ingredients:')
        ingredients_lbl.grid()
        for ingredient in self._ingredients:
            ttk.Label(master=self._frame, text=ingredient[1]).grid(column=1, padx=20, pady=1)

        instructions_lbl = ttk.Label(master=self._frame, text='instructions')
        instructions_lbl.grid()
        instructions_txt = Text(master=self._frame, width=40, height=20)
        instructions_txt.insert('1.0', self._recipe[3])
        instructions_txt['state'] = 'disabled'

        instructions_txt.grid(column=1, columnspan=3)
    def _initialize(self):
        self._root.title('Recipe view')
        self._frame = ttk.Frame(master=self._root)

        ##initialize content
        self._initialize_nav()
        self._initialize_content()
