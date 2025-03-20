from turtle import Turtle
from bullet import Bullet

DISTANCE = 25
LEFT_LIMIT = -275
RIGHT_LIMIT = 275


class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        #self.screen.addshape("images/spaceship.gif")
        #self.shape("images/spaceship.gif")
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.goto(0, -270)
        self.bullets = []

    def move_left(self):
        if self.xcor() > LEFT_LIMIT:
            self.goto(self.xcor()-DISTANCE, self.ycor())

    def move_right(self):
        if self.xcor() < RIGHT_LIMIT:
            self.goto(self.xcor()+DISTANCE, self.ycor())

    def fire(self):
        new_bullet = Bullet(self.xcor(), self.ycor() + 20, 1)
        self.bullets.append(new_bullet)
