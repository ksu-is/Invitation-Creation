import tkinter as tk
from tkinter import messagebox

def invitation():
    bg_color = input("What color do you want on the background: ")
    
    root = tk.Tk()
    root.title("Your letter: ")
    
    root.configure(bg=bg_color)

#color_input = tk.Entry(root, width=20)

invitation()