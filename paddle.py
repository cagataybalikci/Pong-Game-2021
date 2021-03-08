from turtle import Turtle

PADDLE_POSITIONS = {"player": (350, 0), "cpu": (-350, 0)}
MOVE_AMOUNT = 20
MOVE_LIMITS = 235


class Paddle(Turtle):
    def __init__(self, paddle_owner):
        super().__init__()
        self.paddle_owner = paddle_owner
        self.create_paddle(self.paddle_owner)

    def create_paddle(self, which_paddle):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=PADDLE_POSITIONS[which_paddle][0], y=PADDLE_POSITIONS[which_paddle][1])
        self.speed("fastest")

    def move_up(self):
        if self.ycor() < MOVE_LIMITS:
            self.goto(self.xcor(), self.ycor() + MOVE_AMOUNT)

    def move_down(self):
        if self.ycor() > (-MOVE_LIMITS + 20):
            self.goto(self.xcor(), self.ycor() - MOVE_AMOUNT)
