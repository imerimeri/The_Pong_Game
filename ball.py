#ball.py

import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("black")


    def move(self):
        rand_direction = random.randint(0,360)
        self.setheading(rand_direction)
        self.forward(self.move_speed)




