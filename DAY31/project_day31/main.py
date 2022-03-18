from tkinter import *
import pandas
import random
import time


BACKGROUND_COLOR = "#B1DDC6"

#Reading the data from the csv file to the flash card
data = pandas.read_csv("DAY31/project_day31/data/french_words.csv")

#creating a dictonary from the dataframe
to_learn = data.to_dict(orient='records')

#function to get each words at random
def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(title,text='French')
    canvas.itemconfig(word_list,text=f"{current_card['French']}")
            


window = Tk()
window.title("My Flash Card")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
#creating the canvans
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR)

#getting the image for the flash card 
card_front = PhotoImage(file="DAY31/project_day31/images/card_front.png")
card_back = PhotoImage(file="DAY31/project_day31/images/card_back.png")

#getting the image for the button
right_image = PhotoImage(file="DAY31/project_day31/images/right.png")
wrong_image = PhotoImage(file="DAY31/project_day31/images/wrong.png")

#implementing the image to the canvas
canvas.create_image(800/2,526/2,image=card_front)
title = canvas.create_text(400,150,text='Title',font=('Ariel','40','italic'))
word_list=canvas.create_text(400,263,text='Word',font=('Ariel','40','bold'))
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(highlightthickness=0)

#creating buttons
right_button = Button(image=right_image,highlightthickness=0,command=next_card)
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)

right_button.grid(column=1,row=1)
wrong_button.grid(column=0,row=1)

next_card()
window.mainloop()

