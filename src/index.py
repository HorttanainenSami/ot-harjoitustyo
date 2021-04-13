from tkinter import ttk, Tk
from ui import UI


def main():
    # select UI to show
    window = Tk()
    window.title('Testi')
    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__ == '__main__':
    main()
