from tkinter import ttk, constants, StringVar, Text

class CreateRecipeView:
    def __init__(self, root, recipes, service):
        self._root = root
        self._frame = None
        self._show_recipes = recipes
        self._recipe_name = StringVar()
        self._recipe_service = service

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_save(self, ingredients, instructions):
        self._recipe_service.createRecipe(self._recipe_name.get(), ingredients, instructions)

    def _initialize_content(self):

        header_label = ttk.Label(master=self._frame, text='Create recipe')
        help_lbl = ttk.Label(master=self._frame, text='Add each ingredient to seperate line')
        recipe_name_lbl = ttk.Label(master=self._frame, text='Recipe name:')
        recipe_name_ent = ttk.Entry(master=self._frame, textvariable=self._recipe_name)
        recipe_name_ent.focus()

        ingredients_lbl = ttk.Label(master=self._frame, text='Ingredients:')
        ingredients_ent = Text(master=self._frame, width=20, height=10)

        instruction_lbl = ttk.Label(master=self._frame, text='Instructions:')
        instruction_txt = Text(master=self._frame, width=40, height=20)

        button = ttk.Button(
            master=self._frame,
            text='Login',
            command=lambda: self._handle_save(ingredients_ent.get(1.0, 'end'), instruction_txt.get(1.0, 'end')))


        header_label.grid(padx=5, pady=5)
        help_lbl.grid(padx=5, pady=5)
        recipe_name_lbl.grid(padx=5, pady=5)
        recipe_name_ent.grid(row=2, column=1, padx=5, pady=5)
        ingredients_lbl.grid(padx=5, pady=5)
        ingredients_ent.grid(row=3, column=1, padx=5, pady=5)
        instruction_lbl.grid(padx=5, pady=5)
        instruction_txt.grid(row=4, column=1, padx=5, pady=5, columnspan=3)
        button.grid(padx=5, pady=5)

    def _initialize(self):
        self._root.title('Login view')
        self._frame = ttk.Frame(master=self._root)

        # initializing components
        self._initialize_content()

