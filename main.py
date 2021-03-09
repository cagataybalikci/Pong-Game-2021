from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

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

# TODO : Collision with Elements (Ball, Paddles, Screen)
# TODO : Create Score UI and Track Score


# Game
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
