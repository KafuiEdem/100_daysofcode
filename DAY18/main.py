from random import random
from turtle import Turtle,Screen
import turtle as t
import random

timmy_the_turtle = Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    new_color = (r,g,b)
    return new_color

# for i in range(4):
#     timmy_the_turtle.fd(100)
#     timmy_the_turtle.rt(90)

# for i in range(10):
#     timmy_the_turtle.fd(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.fd(10)
#     timmy_the_turtle.pendown()

# for u in range(3,1):
#     c = random.choice(colours)
#     for y in range(u):
#         timmy_the_turtle.fd(100)
#         timmy_the_turtle.rt(360/u)
#     timmy_the_turtle.color(c)



# while True:
#     coin = random.randrange(0,2)
#     if coin == 0:
#         timmy_the_turtle.pensize(5-1)
#         timmy_the_turtle.left(90)
#     else:
#         timmy_the_turtle.right(90)
#         timmy_the_turtle.pensize(5+1)

#     timmy_the_turtle.fd(20)
#     timmy_the_turtle.color(random_color())
#     # timmy_the_turtle.pensize(5)
#     timmy_the_turtle.speed(1)

# for _ in range(200):
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.left(5)
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.speed(_)

# for i in range(100):
#     timmy_the_turtle.circle(10,18)
#     timmy_the_turtle.fd(i)
#     timmy_the_turtle.lt(i)

for _ in range(100):
    timmy_the_turtle.circle(50)
    timmy_the_turtle.penup()
    timmy_the_turtle.setpos(10,90)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.left(50)
    timmy_the_turtle.pendown()
    timmy_the_turtle.setpos(50,10)
    timmy_the_turtle.color(random_color())


screen = Screen()
screen.exitonclick()