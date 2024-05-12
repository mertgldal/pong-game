from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.score = 0
        self.write(self.score, align="center", font=("Courier", 40, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=("Courier", 40, "normal"))
