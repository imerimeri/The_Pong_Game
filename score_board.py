#score_board.py

from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.points = 0
        self.write(f"{self.points}", align="center", font=("Courier", 40, "normal"))

    def update_points(self):
        self.clear()
        self.write(f"{self.points}", align="center", font=("Courier", 40, "normal"))

    def increase_points(self):
        self.points +=1
        self.update_points()

