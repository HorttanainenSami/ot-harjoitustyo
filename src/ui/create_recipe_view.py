from tkinter import ttk, constants, StringVar, Text

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

class HeaderFrame:

    def __init__(self, root, recipe_name):
        self._root = root
        self._frame = None
        self._recipe_name = StringVar()
        self._recipe_name.set(recipe_name)
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def get_recipe_name(self):
        return self._recipe_name.get()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(master=self._frame, text='Create recipe')

        recipe_name_lbl = ttk.Label(master=self._frame, text='Recipe name:')
        recipe_name_ent = ttk.Entry(master=self._frame, textvariable=self._recipe_name)
        recipe_name_ent.focus()

        header_label.grid(padx=5, pady=5)
        recipe_name_lbl.grid(padx=5, pady=5)
        recipe_name_ent.grid(padx=5, pady=5)

class IngredientList:
    def __init__(self, root, ingredients):
        self._root = root
        self._frame = None
        self._ingredients = ingredients
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def get_ingredients_list(self):
        entry_list = []
        for i, widget in enumerate(self._frame.winfo_children()):
            if i >= 2:
                entry_list.append(widget.get())

        return entry_list

    def _initialize_item(self, item):
        list_item = ttk.Entry(master=self._frame)
        list_item.insert(0, str(item))
        list_item.grid()

    def _add_entry(self):
        ttk.Entry(master=self._frame).grid()

    def _remove_entry(self):
        if len(self._frame.winfo_children()) > 2:
            self._frame.winfo_children()[-1].destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        add_btn = ttk.Button(master=self._frame, text='add new ingredient', command=self._add_entry)
        remove_btn = ttk.Button(master=self._frame, text='remove ingredient', command=self._remove_entry)

        add_btn.grid()
        remove_btn.grid()

        for item in self._ingredients:
            self._initialize_item(item)
