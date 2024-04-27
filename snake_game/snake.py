from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        new_snake_block = Turtle(shape="square")
        new_snake_block.color("white")
        new_snake_block.penup()
        new_snake_block.setpos(position)
        self.blocks.append(new_snake_block)

    def increase_in_size(self):
        self.add_block(self.blocks[-1].pos())

    def move(self):
        blocks = self.blocks
        for block_num in range(len(blocks) - 1, 0, -1):
            new_x = blocks[block_num - 1].xcor()
            new_y = blocks[block_num - 1].ycor()
            blocks[block_num].goto(new_x, new_y)
        blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.blocks[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.blocks[0].setheading(LEFT)

