from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-280, 250)


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.lever = 1
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.lever}",align="left",font=FONT)

    def increase_level(self):
        self.lever += 1
        self.update_scoreboard()
    

    def game_over(self):
        self.goto(0,0)

        self.write("Game Over",align="center",font=FONT)
        