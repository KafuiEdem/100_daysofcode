from cmath import exp
from tkinter import *
from tkinter import messagebox
from random import shuffle,choice,randint
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = ["".join([choice(letters)]) for _ in range(randint(8, 10)) ]
    password_symbols = ["".join([choice(symbols)]) for _ in range(randint(2, 4)) ]
    password_numbers= ["".join([choice(numbers)]) for _ in range(randint(2, 4)) ]


    password_list = password_letters+password_symbols+password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_input.get()
    password = password_input.get()
    email = email_username_input.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title='ERROR',message="Please don't leave any of the field empty")
    
    else:
       try:
            with open("DAY29/project_day29/data.json",'r') as data_file:
                data =json.load(data_file)
                
       except FileNotFoundError:
             with open("DAY29/project_day29/data.json",'w') as data_file:
                json.dump(new_data,data_file,indent=4)
                
       else:
            data.update(new_data)
            with open("DAY29/project_day29/data.json",'w') as data_file:
                json.dump(data,data_file,indent=4)
       finally:
            web_input.delete(0,END)
            password_input.delete(0,END)

def find_password():
    websit = web_input.get()
    web_input.delete(0,END)
    
    try:
        with open("DAY29/project_day29/data.json",'r') as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title=websit,message="No data available at this time")
    else:
        for word in data:
            if websit in word:
                json_file =data[word]
                email = json_file['email']
                password = json_file['password']
                messagebox.showinfo(title=websit,message=f"Email: {email}\n Password: {password}")
        


  
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Mangager")
#setting padding 
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)

logo_image = PhotoImage(file="DAY29/project_day29/logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

#Labels for the UI
website = Label(text='Website:')
email_username = Label(text='Email/Username:')
password = Label(text='Password:')


website.grid(column=0,row=1)
email_username.grid(column=0,row=2)
password.grid(column=0,row=3)

#input for the UI
web_input = Entry(width=16)
email_username_input = Entry(width=35)
password_input = Entry(width=16)

web_input.grid(column=1, row=1,columnspan=1)
email_username_input.grid(column=1,row=2,columnspan=2)
password_input.grid(column=1,row=3)

web_input.focus()
email_username_input.insert(0,'edem@edem.com')


#Button for the UI
pass_generate = Button(text='Generate Password',command=generate_password)
add = Button(text='Add',width=32,command=save)
search_button = Button(text='Search',command=find_password)


pass_generate.grid(column=2,row=3)
add.grid(column=1,row=4,columnspan=2)
search_button.grid(row=1,column=2)



window.mainloop()