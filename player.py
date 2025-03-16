from turtle import Turtle

DISTANCE = 25
LEFT_LIMIT = -280
RIGHT_LIMIT = 280


class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -270)
        self.shape("images/spaceship.gif")

    def move_left(self):
        if self.xcor() > LEFT_LIMIT:
            self.backward(DISTANCE)

    def move_right(self):
        if self.xcor() < RIGHT_LIMIT:
            self.forward(DISTANCE)

    def fire(self):
        pass

