from turtle import Turtle

DISTANCE = 25


class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -270)

    def move_left(self):
        self.backward(DISTANCE)

    def move_right(self):
        self.forward(DISTANCE)

    def fire(self):
        pass

