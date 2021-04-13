from tkinter import ttk, Tk
from ui.ui import UI
from services.recipe_service import RecipeService


def main():
    # select UI to show
    service = RecipeService()
    window = Tk()
    ui = UI(window, service)
    ui.start()
    window.mainloop()

if __name__ == '__main__':
    main()
