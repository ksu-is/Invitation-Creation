import tkinter as tk
from tkinter import messagebox

def invitation():
    bg_color = input("What color do you want on the background: ")
    #root is tk window
    root = tk.Tk() #initializes the window 
    root.title("Your letter: ")
    root.geometry("5000x5000")
    root.configure(bg=bg_color)

#color_input = tk.Entry(root, width=20)
    root.mainloop()
    
invitation()