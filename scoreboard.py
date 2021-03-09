from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.cpu_score = 0
        self.update_ui()

    def update_ui(self):
        self.goto(100, 200)
        self.write(self.player_score, align="center", font=("Courier", 88, "normal"))
        self.goto(100, 190)
        self.write("P2", align="center", font=("Courier", 10, "normal"))
        self.goto(-100, 200)
        self.write(self.cpu_score, align="center", font=("Courier", 88, "normal"))
        self.goto(-100, 190)
        self.write("P1", align="center", font=("Courier", 10, "normal"))

    def player_point(self):
        self.player_score += 1
        self.clear()
        self.update_ui()

    def cpu_point(self):
        self.cpu_score += 1
        self.clear()
        self.update_ui()

    def game_over(self):
        if self.player_score == 10 or self.cpu_score == 10:
            if self.player_score == 10:
                self.home()
                self.write("Player 2 is won!", align="center", font=("Courier", 30, "normal"))
                return False
            elif self.cpu_score == 10:
                self.home()
                self.write("Player 1 is won!", align="center", font=("Courier", 30, "normal"))
                return False
        else:
            return True
