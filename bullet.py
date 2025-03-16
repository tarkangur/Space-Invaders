from turtle import Turtle

BULLET_SPEED = 20


class Bullet(Turtle):
    def __init__(self, x, y, shooter, bullet_list):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape("triangle")
        self.shapesize(stretch_wid=0.5, stretch_len=1.5)

        if shooter == "player":
            self.color("white")
            self.setheading(90)
        elif shooter == "alien":
            self.color("green")
            self.setheading(270)

        self.shooter = shooter
        self.bullet_list = bullet_list

    def move(self):
        if self.shooter == "player":
            self.goto(self.xcor(), self.ycor() + BULLET_SPEED)

        elif self.shooter == "alien":
            self.goto(self.xcor(), self.ycor() - BULLET_SPEED)

    def destroy(self):
        if self in self.bullet_list:
            self.bullet_list.remove(self)
        self.hideturtle()
        del self
