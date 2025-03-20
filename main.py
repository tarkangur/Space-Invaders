import turtle
from player import Spaceship
from aliens import AliensGroup
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.bgpic("images/space.gif")
screen.setup(600, 800)
screen.title("Space Invaders")
screen.tracer(0)

player = Spaceship()
screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(player.fire, "space")

scoreboard = Scoreboard()
aliens_group = AliensGroup()

game_running = True

while game_running:
    for bullet in player.bullets[:]:
        bullet.move()
        hit_alien = bullet.check_collision(aliens_group.aliens)

        if hit_alien:
            bullet.hideturtle()
            hit_alien.hideturtle()
            player.bullets.remove(bullet)
            aliens_group.aliens.remove(hit_alien)
            scoreboard.increase_score(50)

        if aliens_group.special_ship and bullet.check_collision([aliens_group.special_ship]):
            bullet.hideturtle()
            aliens_group.special_ship.hideturtle()
            player.bullets.remove(bullet)
            scoreboard.increase_score(500)
            aliens_group.special_ship = None

        if bullet.destroy():
            bullet.hideturtle()
            player.bullets.remove(bullet)

    aliens_group.move()

    aliens_group.update_special_ship()

    alien_bullets = aliens_group.fire_bullets()

    for bullet in alien_bullets[:]:
        bullet.move()

        for player_bullet in player.bullets[:]:
            if bullet.check_collision([player_bullet]):
                bullet.hideturtle()
                player_bullet.hideturtle()
                time.sleep(0.01)
                player.bullets.remove(player_bullet)
                time.sleep(0.01)
                alien_bullets.remove(bullet)

        if bullet.check_collision([player]):
            bullet.hideturtle()
            scoreboard.decrease_life()

            if scoreboard.lives == 0:
                scoreboard.game_over()
                game_running = False
                break

        if bullet.destroy():
            bullet.hideturtle()
            alien_bullets.remove(bullet)

    if not aliens_group.aliens:
        time.sleep(1)
        aliens_group = AliensGroup()

    screen.update()
    time.sleep(0.15)

screen.mainloop()
