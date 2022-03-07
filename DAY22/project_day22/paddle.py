from turtle import Turtle

NUM = 20
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)
        


    def create_paddle(self,position):
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(position)
        


    def move_up(self):
        new_y = self.ycor() + NUM
        self.goto(self.xcor(),new_y)
            

    def move_down(self):
        new_y = self.ycor() - NUM
        self.goto(self.xcor(),new_y)