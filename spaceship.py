from turtle import Turtle

ACCEL = 5
MAX_SPEED = 25
TURN = 15
INNERTION = 1
SCREEN_SIZE = {"width": 600, "height": 600}

class SpaceShip(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.cur_vel = 0

    
    def moving(self):
        if self.cur_vel > MAX_SPEED:
            self.cur_vel = MAX_SPEED
        if self.cur_vel > 0:
            self.cur_vel -= INNERTION
        elif self.cur_vel < 0:
            self.cur_vel = 0

        self.forward(self.cur_vel)

        if self.xcor() >=300:
            self.goto(-300, self.ycor())
        elif self.xcor() <= -300:
            self.goto(300, self.ycor())
        if self.ycor() >=300:
            self.goto(self.xcor(), -300)
        elif self.ycor() <= -300:
            self.goto(self.xcor(), 300)
    
    def up(self):
        self.cur_vel += ACCEL

    def turn_left(self):
        self.left(TURN)

    def turn_right(self):
        self.right(TURN)

    def spawn(self):
        self.goto(0,0)

    def game_over(self):
        pass