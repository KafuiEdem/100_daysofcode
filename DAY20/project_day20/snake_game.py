from doctest import FAIL_FAST
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()
score = ScoreBoard()


screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
# y_pos = [-20,-40,-60]
snake = Snake()
food = Food()





screen.listen()
screen.onkey(fun=snake.up,key='Up')
screen.onkey(fun=snake.down,key='Down')
screen.onkey(fun=snake.left,key='Left')
screen.onkey(fun=snake.right,key='Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #dectect collotion with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scores_increase()

    #detecting collosion
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    #detecting snak collosion with tall
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) <10:
            score.reset()
            snake.reset()
        
        
screen.exitonclick()