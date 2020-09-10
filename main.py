from tkinter import *

# window set up
window = Tk()
window.title("Rock Paper Scissors by Adolfo López Herrera")

# label header
lbl = Label(window, text = "\nWelcome to Rock Paper Scissors!", font = ("Helvetica Bold",20))
lbl.grid(column = 0, row = 0)
lbl.config(anchor=CENTER)
lbl.pack()

# setting window size
window.geometry('500x500')

# run window
window.mainloop()
