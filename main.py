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
        lbl = Label(window, text="\nWelcome to Rock Paper Scissors!", height=2, font=("Helvetica Bold", 32))
        lbl.config(anchor=CENTER)
        lbl.pack()

        # setting window size
        window.geometry('500x500')

        # initial output isn't set to anything
        output = "??"

        # output label
        output_lbl = Label(window, text="\n" + output, font=("Helvetica Bold", 80))
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

    def Rock(self):
        """when user selects Rock"""

    def Paper(self):
        """when user selects Paper"""

    def Scissor(self):
        """when user selects Scissor"""


if __name__ == "__main__":
    window = tk.Tk()
    MainApplication(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
