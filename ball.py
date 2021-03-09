from turtle import Turtle

MOVE_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + MOVE_SPEED
        new_y = self.ycor() + MOVE_SPEED
        self.goto(new_x, new_y)
