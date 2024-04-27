from turtle import Turtle

def draw_dashed_line():
    draw_line = Turtle()
    draw_line.speed(0)
    draw_line.hideturtle()
    draw_line.color("white")
    draw_line.penup()
    draw_line.goto(0, 300)
    draw_line.setheading(270)
    for _ in range(800 // 10):
        draw_line.pendown()
        draw_line.forward(10)
        draw_line.penup()
        draw_line.forward(10)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 220)
        self.write(f"{self.l_score}", align="center", font=("Arial", 50, "normal"))
        self.goto(100, 220)
        self.write(f"{self.r_score}", align="center", font=("Arial", 50, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(f"{self.l_score}", align="center", font=("Arial", 50, "normal"))
        self.goto(100, 220)
        self.write(f"{self.r_score}", align="center", font=("Arial", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
