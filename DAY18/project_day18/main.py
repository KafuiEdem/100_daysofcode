from time import time_ns
from turtle import Turtle,Screen
import turtle as tr 
import random

color_list = [(244, 242, 239), (227, 243, 231), (247, 232, 238), (235, 68, 45), (215, 230, 67), (210, 158, 79), (47, 188, 118), (226, 51, 80), (231, 234, 241), (110, 200, 117), (57, 104, 165), (220, 128, 146), (189, 46, 99), (104, 111, 182), (202, 42, 30), (105, 175, 198), (41, 173, 189), (27, 131, 110), (42, 45, 123), (154, 214, 169), (18, 99, 80), (233, 167, 183), (194, 19, 30), (218, 155, 26), (181, 28, 24), (235, 170, 161), (183, 186, 209), (225, 211, 19), (149, 211, 217), (26, 25, 88), (249, 11, 28), (6, 76, 61)]

tim = Turtle()
tr.colormode(255)

tim.setheading(225)
tim.penup()
tim.fd(255)
tim.pendown()
tim.setheading(0)

for i in range(1,101):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.fd(50)
    tim.pendown()
    
    if i % 10 ==0:
        tim.setheading(90)
        tim.penup()
        tim.fd(50)
        tim.pendown()
        tim.setheading(180)
        tim.penup()
        tim.fd(500)
        tim.pendown()
        tim.setheading(0)

screen = Screen()
screen.exitonclick()