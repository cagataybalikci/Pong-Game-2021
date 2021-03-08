from turtle import Screen
from paddle import Paddle

# TODO : Create Game Scene ✔
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# TODO : Create Paddles and movement ✔
paddle_player = Paddle("player")
paddle_cpu = Paddle("cpu")

screen.listen()
screen.onkey(paddle_player.move_up, "Up")
screen.onkey(paddle_player.move_down, "Down")

is_game_on = True

while is_game_on:
    screen.update()

# TODO : Create Ball
# TODO : Collision with Elements (Ball, Paddles, Screen)
# TODO : Create Score UI and Track Score

screen.exitonclick()
