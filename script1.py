from tkinter import *

window=Tk()
def km_to_miles():
    k= float(e1_value.get()) * 1.6
    t1.insert(END,k)

b1=Button(window,text="Convert",height=1,width=20,command=km_to_miles)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,width=20,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()
