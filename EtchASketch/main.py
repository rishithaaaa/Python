from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
userBet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False

y_cords = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_cords[i])
    all_turtles.append(new_turtle)

if userBet:
    is_race_on = True



while is_race_on:

    for turtle in all_turtles:
        random_num = random.randint(0, 10)
        turtle.forward(random_num)

        if turtle.xcor() >= 250:
            is_race_on = False
            if turtle.color() == userBet:
                print(f"you Win. The winner is {turtle.color()[0]} turtle." )
            else:
                print(f"you loose. The winner is {turtle.color()[0]} turtle.")
        i +=1
























#
# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def move_clockwise():
#     tim.right(10)
# def move_anti_clockwise():
#     tim.left(10)
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_anti_clockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c",fun=clear_screen)


screen.exitonclick()