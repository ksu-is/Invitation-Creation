from tkinter import *
match_color = input("What color: ")

class Calculator(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.entry = Entry(master, width=36, font=("Arial",25))
        self.entry.grid(row=0, column=0, columnspan=6, sticky="w")
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground= match_color)
        self.create_widgets()
        self.bind_buttons(master)
        self.grid()

root = Tk()
root.geometry()
root.title("Exciting GUI Calculator")
app = Calculator(root)