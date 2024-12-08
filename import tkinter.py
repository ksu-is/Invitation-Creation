import tkinter
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
        
    def add_chr(self, char, btn=None):
        """
        Concatenates a character passed from a button press (or key type) 
        to a string.
        :param char: string to add passed from a button
        :param btn: button name to use if key is pressed (to flash)
        :return: None
        """
        self.entry.configure(state="normal")
        self.flash(btn) # Flash a button correspond to keystroke
        if self.entry.get() == "Invalid Input":
            self.entry.delete(0,END)
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

root = Tk()
root.geometry()
root.title("Exciting GUI Calculator")
app = Calculator(root)