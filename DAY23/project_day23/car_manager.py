from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) :
        super().__init__()
        self.new_car = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
            random_change = random.randint(1,6)
            if random_change == 1:
                cars = Turtle()
                cars.shape('square')
                cars.shapesize(stretch_len=2,stretch_wid=1)
                cars.penup()
                cars.color(random.choice(COLORS))
                        
                random_y = random.randint(-250,250)
                cars.goto(300,random_y)
                self.new_car.append(cars)

    def move_forward(self):
        for cars in self.new_car:
            cars.backward(self.car_speed)
        
    def level_up(self):
        self.car_speed +=MOVE_INCREMENT 
