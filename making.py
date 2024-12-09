import tkinter 

background_color = input("What color do you wnat the background?: ")

class invitation(Frame): 
    
    def format(self, master):
        Frame.(self, master)
        self.entry = Entry(master, width= 35, font=("Arial", 25))
        self.entry.grid(row=0, column=0, columnspan=6)
        #self.entry.grid(row=0, column=0, columnspan=6, sticky="w")
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground= user)
        self.create_widgets()
        self.bind_buttons(master)
        self.grid()