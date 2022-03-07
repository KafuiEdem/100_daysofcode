from turtle import Turtle

FILE = "./project_day20/data.txt"
class ScoreBoard(Turtle):

    def __init__(self) :
        super().__init__()
        self.game_score = 0
        with open(FILE) as data:
            self.high_score = int(data.read())
        self.penup()
        self.color('white')
        self.goto(-80,270)
        self.hideturtle()
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.game_score}  High Score: {self.high_score}",font=('Arial',24,'normal'))


    def reset(self):
        if self.game_score > self.high_score:
            self.high_score = self.game_score
            with open(FILE, mode='w') as data:
                data.write(f"{self.high_score}")
        self.game_score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(-80,0)
    #     self.write("Game Over",font=('Arial',24,'normal'))

    def scores_increase(self):
        self.game_score +=1
        self.update_score()
    
    # def get_high_score(self):
      