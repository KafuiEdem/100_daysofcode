import imp
from turtle import Turtle,Screen
import random
import turtle



screen = Screen()
screen.setup(width=500,height=400)

is_race_on = False
all_race_turtle = []
user_bet =screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors= ['red','blue','orange','green','purple','yellow']
y_pos = [-70,-40,-10,20,50,80]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_pos[turtle_index])
    all_race_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_race_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winnner")
            else:
                print(f"You have lost! The {winning_color} turtle is the winnner")
                
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

    
screen.exitonclick()