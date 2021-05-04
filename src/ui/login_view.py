from tkinter import ttk, constants, StringVar
from services.recipe_service import InvalidLoginError

class LoginView:
    def __init__(self, root, register, recipes, service):
        self._root = root
        self._frame = None
        self._show_register = register
        self._show_recipes = recipes
        self._username = StringVar()
        self._password = StringVar()
        self._error = StringVar()
        self._recipe_service = service

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_login(self):
        try:
            self._recipe_service.handle_login(self._username.get(), self._password.get())
            self._show_recipes()
        except InvalidLoginError:
            self._error.set('Invalid username or password')


    def _initialize(self):
        self._root.title('Login view')
        self._frame = ttk.Frame(master=self._root)

        # initializing components

        label = ttk.Label(master=self._frame, text='Login to recipe manager')
        error_label = ttk.Label(master=self._frame, textvariable=self._error)
        username_label = ttk.Label(master=self._frame, text='Username')
        username_entry = ttk.Entry(master=self._frame, textvariable=self._username)
        username_entry.focus()

        password_label = ttk.Label(master=self._frame, text='Password')
        password_entry = ttk.Entry(master=self._frame, textvariable=self._password, show='*')

        button = ttk.Button(
            master=self._frame,
            text='Login',
            command=self._handle_login
        )

        register_label = ttk.Label(master=self._frame, text='If you dont have user')
        register_button = ttk.Button(
            master=self._frame,
            text='Register new user',
            command=self._show_register
            )


        label.grid(padx=5, pady=5)
        error_label.grid(padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=2, column=1, padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=3, column=1, padx=5, pady=5)
        button.grid(padx=5, pady=5)
        register_label.grid(padx=5, pady=5)
        register_button.grid(row=5, column=1, padx=5, pady=5)

