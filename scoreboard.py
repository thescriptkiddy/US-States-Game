from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 300)
        self.write(f"Your Score {self.user_score} / 50", align="center", font=("Courier", 30, "normal"))

    def increase_score(self):
        self.user_score += 1
        self.clear()
        self.update_scoreboard()
