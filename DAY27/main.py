from tkinter import * 

window = Tk()
window.title('My first GUI Program')


window.minsize(width=500,height=300)

my_label =Label(text='My Lable',font=('Arial',24,'bold'))

input = Entry()
def button_clicked():
    word= input.get()
    my_label['text'] = word
    return my_label



button = Button(text='Click me',command=button_clicked)

my_label.pack()
button.pack()
input.pack()



window.mainloop()