from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import time  # Added for smoother motion

from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()

score_boardR = ScoreBoard(-20, 250)

score_boardL = ScoreBoard(20, 250)


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.01)  # slows movement for smoother visuals
    screen.update()
    ball.move()

    # Bounce off top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # use method to reverse direction

    # Bounce off right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_x()  # use method to reverse direction

    # Bounce off left paddle
    if ball.distance(l_paddle) < 40 and ball.xcor() < -350:
        ball.bounce_x()

    # Reset if ball goes too far (off-screen)
    if ball.xcor() > 400:
        score_boardR.increase_points()
        score_boardR.update_points()
        ball.reset_position()

    if ball.xcor() < -380:
        score_boardL.increase_points()
        score_boardL.update_points()
        ball.reset_position()


screen.exitonclick()
