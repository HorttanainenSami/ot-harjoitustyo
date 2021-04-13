from tkinter import ttk, constants

class RecipesView:
    def __init__(self, root, service):
        self._root = root
        self._frame = None
        self._recipe_service = service

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._root.title('Recipes view')
        self._frame = ttk.Frame(master=self._root)
        welcome_label = ttk.Label(master=self._frame, text=f'welcome {self._recipe_service.get_logged_user()}' )
        label = ttk.Label(master=self._frame, text='Recipes view')
        

        label.grid(padx=5, pady=5)
        welcome_label.grid(padx=5, pady=5)
