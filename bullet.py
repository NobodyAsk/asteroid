from turtle import Turtle
SPEED = 15


class BulletManager():
    def __init__(self) -> None:
        self.bullets = {}
        self.num = 50
        self.x = 0
        self.y = 0
        self.heading_dir = 0
        self.cur_bull = 0
        self.is_reload = True
        self.fire_delay = True
    

    def add_bullet(self, i):
        new_bullet = Turtle()
        new_bullet.resizemode("user")
        new_bullet.shapesize(stretch_wid=0.2, stretch_len=0.2)
        new_bullet.color("white")
        new_bullet.ht()
        new_bullet.shape("circle")
        new_bullet.penup()
        self.bullets[i] = {"bullet":new_bullet, "is_fired":False}
    

    def get_bullets(self):
        for i in range(self.num):
            self.add_bullet(i)
    

    def get_data(self, head_dir, pos_x, pos_y):
        '''Get the current data from the spaceship'''
        self.x = pos_x
        self.y = pos_y
        self.heading_dir = head_dir


    def to_fire(self):
        '''Preparing to fire a bullet'''
        if self.is_reload:
            if self.cur_bull < self.num:
                self.bullets[self.cur_bull]["is_fired"] = True
                self.fire(self.bullets[self.cur_bull]["bullet"])
            else:
                self.cur_bull = 0
    

    def cool_down(self):
        pass


    def fire(self, bullet):
        '''fire the bullet'''
        bullet.showturtle()
        bullet.setheading(self.heading_dir)
        self.cur_bull += 1
    

    def moving(self):
        '''Process of the bullets moving'''
        for i in range(self.num):
            if not self.bullets[i]["is_fired"]:
                self.bullets[i]["bullet"].goto(self.x, self.y)
            else:
                self.bullets[i]["bullet"].forward(SPEED)
                if self.bullets[i]["bullet"].xcor() > 350 or self.bullets[i]["bullet"].xcor() < -350 or self.bullets[i]["bullet"].ycor() > 350 or self.bullets[i]["bullet"].ycor() < -350:
                    self.hit(self.bullets[i])

    def hit(self, bull):
        '''When bullet hit asteroid'''
        bull["bullet"].ht()
        bull["is_fired"] = False
        



