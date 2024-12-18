from tkinter import *

root=Tk()


e=Entry(root,width=30)
e.pack()
e.insert(0,"Enter your name")

def myClick():
    hello=" Hello" + e.get()
    myLabel=Label(root,text=hello)
    myLabel.pack()

myButton=Button(root,text="Enter Your Name",command=myClick)
myButton.pack()


root.mainloop()