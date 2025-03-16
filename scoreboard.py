from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(200, 350)
        self.write(score, align="left", font=("Arial", 30, "normal"))
        self.hideturtle()
