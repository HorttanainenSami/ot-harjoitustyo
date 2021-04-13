from tkinter import ttk, constants

class RegisterView:
    def __init__(self, root, handle):
        self._root = root
        self._frame = None
        self._handle_show_login = handle

        self._initialize()
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def _handle_register(self):
        ## add user to database if there is no user with same username
        print('a')

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._root.title('Register view')
        self._frame = ttk.Frame(master=self._root)

        # initializing components
        
        label = ttk.Label(master=self._frame, text='Register to recipe manager')
        username_label = ttk.Label(master=self._frame, text='Username')
        username_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame, text='Pasword')
        password_entry = ttk.Entry(master=self._frame)
        button = ttk.Button(master=self._frame, text='Register and login', command=self._handle_register)
        register_label = ttk.Label(master=self._frame, text='If you allready have an user')
        register_button = ttk.Button(master=self._frame, text='Login', command=self._handle_show_login)


        label.grid(padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, padx=5, pady=5)
        button.grid(padx=5, pady=5)
        register_label.grid(padx=5, pady=5)
        register_button.grid(row=4, column=1, padx=5, pady=5)

        #self._root.grid_columnconfigure(0, minsize=600)
