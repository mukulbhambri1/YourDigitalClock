from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("Digital Clock")
def time():
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)
label=Label(root, font=("Times", "24", "bold italic"), width = 15)
label.pack(anchor="center")
time()
mainloop()
