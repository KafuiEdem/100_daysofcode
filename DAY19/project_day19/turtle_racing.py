from turtle import Turtle,Screen
import random
import turtle



screen = Screen()
screen.setup(width=500,height=400)
colors= ['red','blue','orange','green','purple','yellow']

is_race_on = False
all_race_turtle = []
user_bet =screen.textinput(title="Make your bet for this turtle ",prompt=f"Which turtle will win the race? Enter a color\n AVAILABLE TURTLES \n [{colors[0]},{colors[1]},{colors[2]},{colors[3]},{colors[4]},{colors[5]}]: ")

y_pos = [-70,-40,-10,20,50,80]

def show_winner(win,user):
    turtle.penup()
    turtle.setx(-230)
    turtle.sety(100)
    if win == user:
        turtle.penup()
        turtle.write(f"You have won! The {win} turtle is the winnner",font=("Verdana",15, "normal"))
        
    else:
        turtle.penup()
        turtle.write(f"You have lost! The {win} turtle is the winnner",font=("Verdana",15, "normal"))
    
   
        
        

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
            
            show_winner(winning_color,user_bet)
       
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

    
screen.exitonclick()