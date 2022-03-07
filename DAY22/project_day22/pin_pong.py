from turtle import Screen, goto
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()    
#setting the heigt of the screen
screen.setup(width=800,height=600)
screen.title('Pong')
screen.tracer(0)
screen.bgcolor('black')
ball = Ball()
ball_speed = 10

paddle_1 = Paddle((300,0))
paddle_2 = Paddle((-300,0))
paddle_1_score = 0
paddle_2_score = 0
score = Scoreboard()





screen.listen()
screen.onkey(fun=paddle_1.move_up,key="Up")
screen.onkey(fun=paddle_1.move_down,key='Down')
screen.onkey(fun=paddle_2.move_up,key="s")
screen.onkey(fun=paddle_2.move_down,key='a')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #detecting collosion
    if ball.ycor() > 280 or ball.ycor()< -280 :
        # print("ROCK BOTTOM")
        ball.bounce_y()
    
    #detect collosion with right paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 280 or ball.distance(paddle_2) < 50 and ball.xcor() > -280:
        ball.bounce_x()
        ball_speed +1
        ball.speed(ball_speed)
        print(ball.speed())


    #detect when the ball gose out the edge of the screen
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() <- 380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()

