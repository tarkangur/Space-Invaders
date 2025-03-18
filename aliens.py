from turtle import Turtle


ALIEN_START_X = -250
ALIEN_START_Y = 250
ALIEN_SPACING_X = 30
ALIEN_SPACING_Y = 30
ALIEN_SPEED = 10
ALIEN_DROP = 30


class AlienShip(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(270)
        self.penup()
        self.goto(x, y)


def create_aliens():
    aliens = []
    for row in range(3):
        for col in range(8):
            x = ALIEN_START_X + col * ALIEN_SPACING_X
            y = ALIEN_START_Y - row * ALIEN_SPACING_Y
            alien = AlienShip(x, y)
            aliens.append(alien)
    return aliens


def move_aliens(aliens, direction):
    for alien in aliens:
        new_x = alien.xcor() + (ALIEN_SPEED * direction)
        alien.goto(new_x, alien.ycor())


def check_wall_collision(aliens, direction):
    for alien in aliens:
        if alien.xcor() > 280 or alien.xcor() < -280:
            return True
    return False
