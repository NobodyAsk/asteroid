import turtle as t
from spaceship import SpaceShip
from asteroid import AsterManager
from bullet import BulletManager
from scoreboard import ScoreBoard
import time

##Scoreboard variables
velocity = 0
combo = False

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

score_board = ScoreBoard()
score_board.set_scoreboard()
rocket = SpaceShip()
rocket.spawn()
bullets = BulletManager()
bullets.get_bullets()
asteroids = AsterManager()
asteroids.spawn_asters()

screen.listen()
screen.onkeypress(rocket.up, "Up")
screen.onkeypress(rocket.turn_left, "Left")
screen.onkeypress(rocket.turn_right, "Right")
screen.onkey(bullets.to_fire, "space")
screen.update()
              
game_is_on = True

while game_is_on:
    bullets.get_data(rocket.heading(), rocket.xcor(), rocket.ycor())
    asteroids.moving()
    rocket.moving()
    bullets.moving()
    if combo:
        velocity += 1
        print(velocity)
        score_board.hit(pos_x, pos_y + velocity)
        if velocity > 50:
            velocity = 0
            combo = False
            score_board.hit_number.clear()
    for i in range(asteroids.num):
        if asteroids.orion[i]["aster"].distance(rocket) < asteroids.orion[i]["rad"]:
            game_is_on = False
            score_board.game_over()
        for n in range(bullets.num):
            if asteroids.orion[i]["aster"].distance(bullets.bullets[n]["bullet"]) < asteroids.orion[i]["rad"]:
                pos_x = asteroids.orion[i]["aster"].xcor()
                pos_y = asteroids.orion[i]["aster"].ycor()
                combo = True
                bullets.hit(bullets.bullets[n])
                asteroids.destroyed(asteroids.orion[i])
                score_board.score += 1
                score_board.update_score()
    
    
    time.sleep(0.02)
    screen.update()


screen.exitonclick()