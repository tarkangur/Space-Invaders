from turtle import Turtle

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

    def move_left(self):
        if self.xcor() > LEFT_LIMIT:
            self.goto(self.xcor()-DISTANCE, self.ycor())

    def move_right(self):
        if self.xcor() < RIGHT_LIMIT:
            self.goto(self.xcor()+DISTANCE, self.ycor())

    def fire(self):
        pass

