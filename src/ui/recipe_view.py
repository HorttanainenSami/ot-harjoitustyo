from tkinter import ttk, constants, Text

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

    def _initialize_nav(self):

        back_btn = ttk.Button(
            master=self._frame,
            text='Go back',
            command=self._recipes_view
                )
        modify_btn = ttk.Button(
            master=self._frame,
            text='Modify',
            command=self.edit_recipe
            )
        back_btn.grid()
        modify_btn.grid()


    def _initialize_content(self):
        label = ttk.Label(master=self._frame, text=self._recipe[2])
        label.grid(padx=20, pady=20, sticky=constants.EW, columnspan=3)

        for ingredient in self._ingredients:
            ttk.Label(master=self._frame, text=ingredient[1]).grid()

        guide_txt = Text(master=self._frame)
        guide_txt.insert('1.0', self._recipe[3])
        guide_txt['state'] = 'disabled'

        guide_txt.grid()
    def _initialize(self):
        self._root.title('Recipe view')
        self._frame = ttk.Frame(master=self._root)

        ##initialize content
        self._initialize_nav()
        self._initialize_content()
