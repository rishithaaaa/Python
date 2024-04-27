import time
from turtle import Screen
from paddle import Paddle

from ball import Ball
from scoreboard import ScoreBoard, draw_dashed_line

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

draw_dashed_line()


r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
scoreboard = ScoreBoard()
ball = Ball()

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.update()


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect when ball goes out of bounds on right
    if ball.xcor() > 400:
        ball.recenter()
        scoreboard.r_point()

    # Detect when ball goes out of bounds on right
    if ball.xcor() < -400:
        ball.recenter()
        scoreboard.l_point()

    # Detect the collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

screen.exitonclick()
