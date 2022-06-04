from turtle import Turtle

class ScoreBoard():
    def __init__(self) -> None:
        self.score = 0
        self.tim = Turtle()
        self.tim.color("white")
        self.tim.penup()
        self.tim.ht()
        self.hit_number = Turtle()
        self.hit_number.color("white")
        self.hit_number.penup()
        self.hit_number.ht()
    
    def set_scoreboard(self):
        self.tim.goto(0, 250)
        self.tim.write(f"Score: {self.score}")

    def update_score(self):
        self.tim.clear()
        self.set_scoreboard()
    
    def hit(self, pos_x, pos_y):
        self.hit_number.clear()
        self.hit_number.goto(pos_x, pos_y)
        self.hit_number.write("1")
    
    def game_over(self):
        self.tim.goto(0, 0)
        self.tim.write(f"Your final score: {self.score}\n Game over.")
