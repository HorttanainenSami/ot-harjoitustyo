from tkinter import ttk, constants

class RecipesView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._root.title('Recipes view')
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text='Recipes view')

        label.grid()
