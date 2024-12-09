import tkinter as tk
from tkinter import messagebox

def invitation():
    bg_color = input("What color do you want on the background: ")
    name = input("What is your name?: ")
    #root is tk window
    root = tk.Tk() #initializes the window 
    root.title("This invitation is from, " + name)
    #50x50 ellipsis 5000x5000 full screen 
    root.geometry("700x500")
    root.configure(bg=bg_color)
    
    #info for inv 
    title_iv = input("Please enter the title of your invitation: ")
    iv_to = input("Please enter the name of the recipient: ")
    body = input("Please enter the important text for your recipient: ")
   
    #put ontop of the window
    Label = tk.Label(root, text=title_iv, font=("Helvetica", 20), bg=bg_color, fg="black")
    Label.grid(row=0, column=3, pady=10, padx=10) #pady/x is padding 
    
    Label = tk.Label(root, text="To: "+ iv_to, font=("Helvetica", 18), bg=bg_color, fg="black")
    Label.grid(row=6, column=6, pady=10, padx=10) 
    
    Label = tk.Label(root, text=body, font=("Helvetica", 18), bg=bg_color, fg="black")
    Label.grid(row=1, column=1, pady=10, padx=5) 
    
    #The grid 
    root.grid_columnconfigure(0, weight=1) #columns 
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)  
    root.grid_columnconfigure(4, weight=1)
    root.grid_columnconfigure(5, weight=1)
    root.grid_columnconfigure(6, weight=1)
    root.grid_rowconfigure(0, weight=1) #rows 
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_rowconfigure(6, weight=1)
    root.grid_rowconfigure(7, weight=1)

    
    #do i need?
    root.mainloop()
    
invitation()