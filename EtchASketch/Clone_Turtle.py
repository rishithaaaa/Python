from turtle import Turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


class CloneTurtle:

    def __init__(self):
        self.tim = Turtle(shape="turtle")

    def assign_color(self, col):
        self.color(col)

    def setPos(self,x,y):
        self.goto(x,y)