from tkinter import *
from tkinter import messagebox

pencere=Tk()
pencere.title("HPVitrin Vitrin ve Kutu Sistemleri")
pencere.geometry("300x300")


uygulama=Frame(pencere)
uygulama.grid()


#Buton ekleme bolumu
button1=Button(uygulama, text= "KAPAT", width=7,height=7, command=exit,bg='lightblue')
button1.grid(padx=40, pady=20)
pencere.mainloop()