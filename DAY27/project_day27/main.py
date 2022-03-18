from cgitb import text
from curses import window
from tkinter import *
from turtle import screensize

from numpy import insert, size

window = Tk()


# window.minsize(width=500,height=300)
window.title('Mile to Km Converter')
window.config(padx=20,pady=20)

input = Entry(width=10)
input.insert(END,string='0')
input.grid(column=1,row=0)

#adding a label for the input
input_label = Label(text='Miles')
input_label.grid(column=2,row=0)

#is equal to 
is_equal = Label(text='is equal to')
is_equal.grid(column=0,row=1)

#total 
total = Label(text=0)
total.grid(column=1,row=1)

#km
km = Label(text='km')
km.grid(column=2,row=1)

#function to convert mil to km
def mile_to_km():
    mile = input.get()
    
    return total.config(text=round(float(mile) * 1.6,2))
    

#calculate button
button = Button(text='Calculate',command=mile_to_km)
button.grid(column=1,row=2)

window.mainloop()