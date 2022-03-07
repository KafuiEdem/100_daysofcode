import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(fun=player.move_up, key="Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_forward()

    #Detect collossion 
    for cars in car.new_car:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()
    
    #Detect successful crossing
    if player.is_successful_finish():
        player.go_to_start()
        car.level_up()
        score.increase_level()

    



screen.exitonclick()