from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.create_paddle(positions)

    def create_paddle(self, positions):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(positions)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
