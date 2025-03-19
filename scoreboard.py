from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 360)
        self.write(f"Lives: {self.lives}  Score: {self.score}", font=("Arial", 14, "normal"))

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()

    def decrease_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-50, 0)
        self.write("GAME OVER", font=("Arial", 24, "bold"))
