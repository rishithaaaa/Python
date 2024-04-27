from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def display_game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align='center', font=('Courier', 15, 'bold'))







