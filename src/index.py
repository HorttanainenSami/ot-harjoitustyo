from tkinter import Tk
from sys import exit
from ui.ui import UI
from services.recipe_service import RecipeService

def main():
    service = RecipeService()
    window = Tk()
    user_interface = UI(window, service)
    user_interface.start()
    window.mainloop()



if __name__ == '__main__':
    main()
