import tkinter as tk
from tkinter import messagebox

def invitation():
    bg_color = input("What color do you want on the background: ")
    name = input("What is your name?")
    #root is tk window
    root = tk.Tk() #initializes the window 
    root.title("Your letter: ")
    #50x50 ellipsis 5000x5000 full screen 
    root.geometry("700x500")
    root.configure(bg=bg_color)
    #do i need?
    root.mainloop()
    #put ontop of the window
    labe1 = tk.labe1(root, text=name, font=("Helvetica", 18), bg="black")
    labe1.pack(side="top", pady=10)
    
invitation()