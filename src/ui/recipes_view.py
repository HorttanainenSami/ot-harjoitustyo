from tkinter import ttk, constants, Tk

class RecipesView:
    def __init__(self,root, logout, service):
        self._root = root
        self._root.geometry('600x600')
        self._frame = None
        self._recipe_service = service
        self._logout = logout
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_logout(self):
        self._recipe_service.handle_logout()
        self._logout()

    def _initialize_header(self):
        label = ttk.Label(master=self._frame, text='Recipe suggester app', style='Header.TLabel')
        label.grid(padx=20, pady=20, sticky=constants.EW, columnspan=3)
    
        ## Style
        style = ttk.Style()
        style.configure('Header.TLabel', font=('Helvetica', 30))

    def _initialize_navbar(self):
        logout_btn = ttk.Button(master=self._frame, text='Log out', command=self._handle_logout)
        create_recipe_btn = ttk.Button(master=self._frame, text='Create new recipe')

        create_recipe_btn.grid(padx=5, pady=5)
        logout_btn.grid(padx=5, pady=5, row=1, column=1)

    def _initialize(self):
        self._root.title('Recipes view')
        self._frame = ttk.Frame(master=self._root)
        
        ##initialize content
        self._initialize_header()
        self._initialize_navbar()


