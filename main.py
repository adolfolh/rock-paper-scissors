import tkinter as tk
from tkinter import *
from tkmacosx import Button
import random


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # window set up
        window.resizable(False, False)
        window.title("Rock Paper Scissors by Adolfo López Herrera")

        # label header
        lbl = Label(window, text="\nWelcome to Rock Paper Scissors!", height=2, font=("Helvetica Bold", 28))
        lbl.config(anchor=CENTER)
        lbl.pack(pady=10)

        # setting window size
        window.geometry('500x500')

        # initial output isn't set to anything
        self.output = tk.StringVar()
        self.output.set("??")

        # output label
        output_lbl = Label(window, textvariable=self.output, font=("Helvetica Bold", 100), height=2)
        output_lbl.config(anchor=CENTER)
        output_lbl.pack()

        # buttons
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(4, weight=1)

        btn1 = Button(window, text="✊", bg="black", width=100, height=100, borderless=1, font=("Helvetica", 40),
                      command=self.Rock)
        btn1.grid(row=0, column=1)
        btn1.pack(padx=33.3333333333, pady=0, side=tk.LEFT)

        btn2 = Button(window, text="✋", bg="black", width=100, height=100, borderless=1, font=("Helvetica", 40),
                      command=self.Paper)
        btn2.grid(row=0, column=2)
        btn2.pack(padx=33.3333333333, pady=0, side=tk.LEFT)

        btn3 = Button(window, text="✌️", bg="black", width=100, height=100, borderless=1, font=("Helvetica", 40),
                      command=self.Scissor)
        btn3.grid(row=0, column=3)
        btn3.pack(padx=33.3333333333, pady=0, side=tk.LEFT)

    def RandomOutput(self):
        # random output generator
        outputNum = random.randint(1, 3)
        if outputNum == 1:
            out = "✊"
        elif outputNum == 2:
            out = "✋"
        else:
            out = "✌️"

        return self.output.set(out)

    def Rock(self):
        """when user selects Rock"""
        MainApplication.RandomOutput(self)


    def Paper(self):
        """when user selects Paper"""
        MainApplication.RandomOutput(self)



    def Scissor(self):
        """when user selects Scissor"""
        MainApplication.RandomOutput(self)




if __name__ == "__main__":
    window = tk.Tk()
    MainApplication(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
