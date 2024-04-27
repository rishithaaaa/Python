import turtle as t
import random


tim = t.Turtle()
tim.screen.colormode(255)
# tim.color((91, 116, 145))
colors = [(91, 116, 145), (172, 116, 145), (143, 172, 145), (52, 172, 145),(246, 172, 145),(187, 93, 145),(187, 255, 145),(57, 77, 44),(168, 77, 44),(235, 36, 255),(14, 181, 255),(197, 181, 255),(250, 220, 255),(183, 140, 197),(247, 255, 175)]

tim.speed(0)
tim.hideturtle()
tim.penup()
tim.setpos(-230, -175)
print(tim.pos())
i = 0
for _ in range(100):
    i = i+1
    tim.pendown()
    col = random.choice(colors)
    tim.color(col)
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()
    tim.penup()
    if i%20 == 0:
        tim.right(90)
        tim.forward(30)
        tim.right(90)

    elif(i%10 == 0):
        tim.left(90)
        tim.forward(60)
        tim.left(90)
    else:
        tim.forward(50)




screen = t.Screen()
screen.exitonclick()


