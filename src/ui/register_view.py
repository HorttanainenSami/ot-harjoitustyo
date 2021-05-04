from tkinter import ttk, constants, StringVar
from services.recipe_service import UsernameAlreadyInUseError, PasswordTooShortError, UsernameTooShortError

class RegisterView:
    def __init__(self, root, handle, service):
        self._root = root
        self._frame = None
        self._handle_show_login = handle
        self._recipe_service = service
        self._username = StringVar()
        self._password = StringVar()
        self._error = StringVar()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _handle_register(self):
        ## add user to database if there is no user with same username
        try:
            self._recipe_service.create_user(self._username.get(), self._password.get())
            self._handle_show_login()
        except PasswordTooShortError:
            self._error.set('password length must be atleast (3) characters long')
        except UsernameTooShortError:
            self._error.set('username length must be atleast (3) characters long')
        except UsernameAlreadyInUseError:
            self._error.set('Username must be unique')

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._root.title('Register view')
        self._frame = ttk.Frame(master=self._root)

        # initializing components

        label = ttk.Label(master=self._frame, text='Register to recipe manager')
        error_label = ttk.Label(master=self._frame, textvariable=self._error)
        username_label = ttk.Label(master=self._frame, text='Username')
        username_entry = ttk.Entry(master=self._frame, textvariable=self._username)
        username_entry.focus()
        password_label = ttk.Label(master=self._frame, text='Pasword')
        password_entry = ttk.Entry(master=self._frame, textvariable=self._password, show='*')
        button = ttk.Button(
            master=self._frame,
            text='Register and login',
            command=self._handle_register
        )
        register_label = ttk.Label(master=self._frame, text='If you already have an user')

        register_button = ttk.Button(
            master=self._frame,
            text='Login',
            command=self._handle_show_login
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

