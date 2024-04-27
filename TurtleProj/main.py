from turtle import Turtle,Screen

tim = Turtle()
import random
colours = [
    "red", "green", "blue", "cyan", "magenta",
    "yellow", "orange", "purple", "pink", "brown",
     "lightgray", "darkgray"
]


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
tim.speed(0)  # fastest
# dist = [ 10, 25, 30, 40, 50, 60, 90, 15, 35, 23, 21, 22, 12]
for _ in range(100):
    tim.color(random.choice(colours))
    tim.circle(100)
    tim.left(5)

    if tim.heading() == 0.0:
        break



# tim.width(8)
# def Random_walk():
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# for _ in range(50):
#     Random_walk()

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side)







screen = Screen()
screen.exitonclick()