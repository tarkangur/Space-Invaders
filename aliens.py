from turtle import Turtle
from bullet import Bullet
import random

ALIEN_SPEED = 10
ALIEN_DROP = 30
SPECIAL_SHIP_SPEED = 5
SPECIAL_SHIP_SPAWN_RATE = 500
SPECIAL_SHIP_SCORE = 500


class AlienShip(Turtle):
    def __init__(self, x, y, is_special=False):
        super().__init__()
        self.shape("turtle")
        self.color("green" if not is_special else "red")
        self.setheading(270 if not is_special else 0)
        self.penup()
        self.goto(x, y)
        self.is_special = is_special
        self.bullets = []

    def fire(self, aliens):
        if self.is_special:
            return

        if random.randint(1, 100) == 1:
            front_clear = True
            for other in aliens:
                if other.xcor() == self.xcor() and other.ycor() > self.ycor():
                    front_clear = False
                    break

            if front_clear:
                new_bullet = Bullet(self.xcor(), self.ycor() - 20, -1)
                self.bullets.append(new_bullet)


class AliensGroup:
    def __init__(self):
        self.aliens = []
        for row in range(3):
            for col in range(8):
                alien = AlienShip(-200 + col * 50, 200 - row * 50)
                self.aliens.append(alien)

        self.special_ship = None
        self.direction = 1
        self.wall_hits = 0
        self.frame_count = 0

    def move(self):
        move_distance = ALIEN_SPEED * self.direction

        for alien in self.aliens:
            alien.goto(alien.xcor() + move_distance, alien.ycor())

        if self.aliens:
            leftmost_x = min(alien.xcor() for alien in self.aliens)
            rightmost_x = max(alien.xcor() for alien in self.aliens)

            if leftmost_x <= -280 or rightmost_x >= 280:
                self.direction *= -1
                self.wall_hits += 1

                if self.wall_hits % 10 == 0:
                    for alien in self.aliens:
                        alien.sety(alien.ycor() - ALIEN_DROP)

    def fire_bullets(self):
        bullets = []
        for alien in self.aliens:
            alien.fire(self.aliens)
            bullets.extend(alien.bullets)
        return bullets

    def update_special_ship(self):
        self.frame_count += 1

        if self.special_ship is None and self.frame_count % SPECIAL_SHIP_SPAWN_RATE == 0:
            self.special_ship = AlienShip(-280, 280, is_special=True)

        if self.special_ship:
            self.special_ship.forward(SPECIAL_SHIP_SPEED)

            if self.special_ship.xcor() > 280:
                self.special_ship.hideturtle()
                self.special_ship = None
