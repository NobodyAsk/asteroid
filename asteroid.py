from turtle import Turtle
import random

MIN_RAD = 20
MAX_RAD = 100
SCREEN_SIZE = {"width": 600, "height": 600}
SPEED = 2


class AsterManager():
    def __init__(self) -> None:
        self.orion = {}
        self.num = 8
        self.shapes = ["rect", "aster"]

    def add_aster(self, i, maxim_rad):
        new_aster = Turtle()
        new_aster.color("white")
        new_aster.ht()
        new_aster.penup()
        rad = random.randint(MIN_RAD, maxim_rad)
        turn_speed = random.randint(2, 10)
        direction = random.randint(0, 1)
        aster_shape = random.choice(self.shapes)
        self.orion[i] ={"aster": new_aster, "rad":rad, "turning": turn_speed, "direction": direction, "shape": aster_shape}
        

    def random_spawn(self, aster):
        aster["aster"].penup()
        aster["aster"].setheading(random.randint(0,359))
        i = random.randint(0, 1)
        if i:
            aster["aster"].goto(-350, random.randint(-350, 350))
        else:
            aster["aster"].goto(random.randint(-350, 350), -350)
        aster["rad"] = random.randint(MIN_RAD, MAX_RAD)
        aster["turning"] = random.randint(2, 10)
        aster["direction"] = random.randint(0, 1)

    def spawn_asters(self):
        for i in range(self.num):
            self.add_aster(i, MAX_RAD)
            self.random_spawn(self.orion[i])
    

    def dest_spawn(self, aster):
        up_rad = aster["rad"]
        pos_x = aster["aster"].xcor()
        pos_y = aster["aster"].ycor()
        aster["rad"] /= 2
        aster["aster"].setheading(random.randint(0,359))
        for i in range(random.randint(0, 1)):
            self.num += 1
            self.add_aster(self.num-1, int(up_rad))
            self.orion[self.num-1]["aster"].goto(pos_x, pos_y)
            self.orion[self.num-1]["aster"].setheading(random.randint(0,359))


    def destroyed(self, aster):
        if aster["rad"] < 40:
            self.random_spawn(aster)
        else:
            self.dest_spawn(aster)
            
    
    def draw_rect(self, i):
        if i["direction"] == 0:
            i["aster"].left(i["turning"])
        else:
            i["aster"].right(i["turning"])
        i["aster"].forward(i["rad"])
        i["aster"].pendown()
        i["aster"].left(120)
        for j in range(6):
            i["aster"].forward(i["rad"])
            i["aster"].left(60)
        i["aster"].left(60)
        i["aster"].penup()
        i["aster"].forward(i["rad"])
        i["aster"].left(180)
        if i["direction"] == 0:
            i["aster"].right(i["turning"])
        else:
            i["aster"].left(i["turning"])
        i["turning"] += 5


    def draw_aster(self, i):
        r = i["rad"]
        if i["direction"] == 0:
            i["aster"].left(i["turning"])
        else:
            i["aster"].right(i["turning"])
        i["aster"].forward(r)
        i["aster"].left(90)
        i["aster"].pendown()
        i["aster"].forward(r/2)
        i["aster"].left(60)
        i["aster"].forward(r)
        i["aster"].left(120)
        i["aster"].forward(r/2)
        i["aster"].right(90)
        i["aster"].forward(r/2)
        i["aster"].right(60)
        i["aster"].forward(r/2)
        i["aster"].left(120)
        i["aster"].forward(r)
        i["aster"].left(30)
        i["aster"].forward(r/2)
        i["aster"].left(60)
        i["aster"].forward(r)
        i["aster"].left(120)
        i["aster"].forward(r/2)
        i["aster"].right(90)
        i["aster"].forward(r/2)
        i["aster"].right(60)
        i["aster"].forward(r/2)
        i["aster"].left(120)
        i["aster"].forward(r)
        i["aster"].left(120)
        i["aster"].penup()
        i["aster"].forward(r)
        i["aster"].left(180)
        if i["direction"] == 0:
            i["aster"].right(i["turning"])
        else:
            i["aster"].left(i["turning"])
        i["turning"] += 5


    
    def moving(self):
        for i in range(self.num):
            self.orion[i]["aster"].clear()
            self.orion[i]["aster"].forward(SPEED)
            if self.orion[i]["shape"] == "rect":
                self.draw_rect(self.orion[i])
            elif self.orion[i]["shape"] == "aster":
                self.draw_aster(self.orion[i])
            if self.orion[i]["aster"].xcor() > 400 or self.orion[i]["aster"].xcor() < -400 or self.orion[i]["aster"].ycor() > 400 or self.orion[i]["aster"].ycor() < -400:
                self.random_spawn(self.orion[i])
                self.orion[i]["rad"] = random.randint(MIN_RAD, MAX_RAD)
