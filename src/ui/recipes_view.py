from tkinter import ttk, constants

class RecipesView:
    def __init__(self, root, logout, createRecipeView, service, recipeView):
        self._root = root
        self._frame = None
        self._recipe_service = service
        self._logout = logout
        self._show_create_recipe_view = createRecipeView
        self._recipe_list = None
        self._show_recipe_view = recipeView
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_logout(self):
        self._recipe_list.destroy()
        self._recipe_service.handle_logout()
        self._logout()

    def _handle_add_recipe(self):
        self._recipe_list.destroy()
        self._show_create_recipe_view()

    def show_recipe(self, recipe_id):
        self._show_recipe_view(self._recipe_service.get_recipe(recipe_id))

    def _initialize_header(self):
        label = ttk.Label(master=self._frame, text='Recipe suggester app')
        label.grid(padx=20, pady=20, sticky=constants.EW, columnspan=3)

    def _initialize_navbar(self):
        logout_btn = ttk.Button(master=self._frame, text='Log out', command=self._handle_logout)
        create_recipe_btn = ttk.Button(master=self._frame, text='Create new recipe', command=self._handle_add_recipe)
        create_recipe_btn.grid(padx=5, pady=5)
        logout_btn.grid(padx=5, pady=5, row=0, column=1)

    def handle_button(self, recipe_id):
        self._recipe_list.destroy()
        print(f'recipe_id in RecipeView class {recipe_id}')
        self._show_recipe_view(recipe_id)

    def _initialize(self):
        self._root.title('Recipes view')
        self._frame = ttk.Frame(master=self._root)

        ##initialize content
        self._initialize_navbar()
        self._recipe_list = RecipeList(self._root, self._recipe_service.get_all_recipes(), self.handle_button)

class RecipeList:
    def __init__(self, root, recipes, show_recipe):
        self._root = root
        self._frame = None
        self._recipes = recipes
        self._show_recipe = show_recipe

        self._initialize()
    def _pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_button(self, recipe_id):
        print(f'recipe id in recipes_view.py {recipe_id}')
        self._show_recipe(recipe_id)

    def _initialize_list_item(self, item):
        item_frame = ttk.Frame(master=self._frame)
        recipe_button = ttk.Button(
            master=item_frame,
            text=f'{item[2]} made in {item[4]}',
            command=lambda: self._handle_button(item)
                )
        recipe_button.grid()

        item_frame.pack(fill=constants.X)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for recipe in self._recipes:
            self._initialize_list_item(recipe)

        self._pack()

