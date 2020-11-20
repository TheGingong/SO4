import math
import tkinter as tk

class main(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        window.title("Menu")
        window.geometry("1000x666")
        self.theHub()
        self.pack()

    def theHub(self):
        self.differentiering  = tk.Button(self)
        self.differentiering ["text"] = "Differentiering"
        #self.differentiering["command"] = differential
        self.differentiering .pack(side=tk.TOP)

        self.integration = tk.Button(self)
        self.integration["text"] = "Integration"
        #self.integration["command"] = integralregning
        self.integration.pack(side=tk.TOP)

window = tk.Tk()
app = main(master=window)
app.mainloop()