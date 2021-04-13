from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, register, recipes):
        self._root = root
        self._frame = None
        self._show_register = register
        self._show_recipes = recipes
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_login(self):
        print('login')
        self._show_recipes()

    def _initialize(self):
        self._root.title('Login view')
        self._frame = ttk.Frame(master=self._root)

        # initializing components

        label = ttk.Label(master=self._frame, text='Login to recipe manager')
        username_label = ttk.Label(master=self._frame, text='Username')
        username_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame, text='Pasword')
        password_entry = ttk.Entry(master=self._frame)
        button = ttk.Button(master=self._frame, text='Login', command=self._handle_login)
        register_label = ttk.Label(master=self._frame, text='If you dont have user')
        regiter_button = ttk.Button(master=self._frame, text='Register new user', command=self._show_register)


        label.grid(padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, padx=5, pady=5)
        button.grid(padx=5, pady=5)
        register_label.grid(padx=5, pady=5)
        regiter_button.grid(row=4, column=1, padx=5, pady=5)
        

