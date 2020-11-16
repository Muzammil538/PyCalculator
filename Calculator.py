import tkinter
from tkinter import *

root = tkinter.Tk()
root.geometry("250x400+300+300")
#root.resizable(0,0)
root.title("Calculator")



btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand=True,fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True,fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True,fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True,fill="both")

#First Coloum

btn1 = Button(
    btnrow1,
    text=1,
    font=("Verdana",22),
)
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(
    btnrow1,
    text=2,
    font=("Verdana",22),
)
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(
    btnrow1,
    text=3,
    font=("Verdana",22),
)
btn3.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(
    btnrow1,
    text=4,
    font=("Verdana",22),
)
btn4.pack(side=LEFT,expand=True,fill="both")

#Second Coloum

btn1 = Button(
    btnrow2,
    text=1,
    font=("Verdana",22),
)
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(
    btnrow2,
    text=2,
    font=("Verdana",22),
)
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(
    btnrow2,
    text=3,
    font=("Verdana",22),
)
btn3.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(
    btnrow2,
    text=4,
    font=("Verdana",22),
)
btn4.pack(side=LEFT,expand=True,fill="both")

#Third Coloum

btn1 = Button(
    btnrow3,
    text=1,
    font=("Verdana",22),
)
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(
    btnrow3,
    text=2,
    font=("Verdana",22),
)
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(
    btnrow3,
    text=3,
    font=("Verdana",22),
)
btn3.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(
    btnrow3,
    text=4,
    font=("Verdana",22),
)
btn4.pack(side=LEFT,expand=True,fill="both")

#Fourth Coloum 

btn1 = Button(
    btnrow4,
    text=1,
    font=("Verdana",22),
)
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(
    btnrow4,
    text=2,
    font=("Verdana",22),
)
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(
    btnrow4,
    text=3,
    font=("Verdana",22),
)
btn3.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(
    btnrow4,
    text=4,
    font=("Verdana",22),
)
btn4.pack(side=LEFT,expand=True,fill="both")


root.mainloop()




