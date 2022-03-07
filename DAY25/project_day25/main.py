import pandas
import turtle
import csv

data = pandas.read_csv("DAY25/project_day25/50_states.csv")



screen = turtle.Screen()
screen.title("U.S. States")

image ="DAY25/project_day25/blank_states_img.gif"
screen.addshape(image,)
screen.setup(width=750,height=500)

turtle.shape(image)



correct_state = []
all_states = data['state'].to_list()


while len(correct_state) < 50:
    answere_state = turtle.textinput(f"Guss the State {len(correct_state)}/{50} STATES","What's another State's name?").title()
    
    #check and exit
    if answere_state == "Exit":
        break

    if answere_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answere_state]
        
        if answere_state in correct_state:
            pass
        else:
            t.goto(state_data.x.item(),state_data.y.item())
            t.write(f"{state_data.state.item()}",font=('Arial',10,'normal'))
            correct_state.append(state_data.state.item())


#states_to_learn.csv
states_to_learn = set(all_states )- set(correct_state)

learn_data = pandas.DataFrame(states_to_learn)
learn_data.to_csv("DAY25/project_day25/states_to_learn.csv")
