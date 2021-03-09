from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

UP_BOTTOM_BOUNDS = 280

# TODO : Create Game Scene ✔
# Screen configs
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# TODO : Create Paddles and movement ✔
paddle_player = Paddle("player")
paddle_cpu = Paddle("cpu")

# Input Manager
screen.listen()
screen.onkey(paddle_player.move_up, "Up")
screen.onkey(paddle_player.move_down, "Down")
screen.onkey(paddle_cpu.move_up, "w")
screen.onkey(paddle_cpu.move_down, "s")

# TODO : Create Ball ✔
ball = Ball()
is_game_on = True


# TODO : Create Score UI and Track Score


# Game
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # TODO : Collision with Elements (Ball, Paddles)
    # Detection between walls and ball
    if ball.ycor() > UP_BOTTOM_BOUNDS or ball.ycor() < -UP_BOTTOM_BOUNDS:
        ball.bounce_y()

    # Detection between ball and paddles
    if ball.distance(paddle_player) < 50 and ball.xcor() > 320 or ball.distance(paddle_cpu) < 50 and ball.xcor() < -320:
        ball.bounce_x()
screen.exitonclick()
