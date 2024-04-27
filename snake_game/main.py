from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect the food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment_score()
        snake.increase_in_size()

    # Detection of collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.display_game_over()

    # Detection of collision with tail
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            game_is_on = False
            scoreboard.display_game_over()

screen.exitonclick()
