from turtle import Turtle

BULLET_SPEED = 20


class Bullet(Turtle):
    def __init__(self, x, y, direction):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.color("white" if direction == 1 else "green")
        self.shapesize(stretch_wid=1.0, stretch_len=0.2)
        self.direction = direction

    def move(self):
        new_y = self.ycor() + (BULLET_SPEED * self.direction)
        self.goto(self.xcor(), new_y)

    def destroy(self):
        return self.ycor() > 380 or self.ycor() < -380

    def check_collision(self, objects):
        for obj in objects:
            if self.distance(obj) < 15:
                return obj
        return None
