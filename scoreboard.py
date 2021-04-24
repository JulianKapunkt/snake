from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
       # self.hideturtle()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.goto(0,200)
        self.color("white")
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score +=1
        self.write(f" Score: {self.score}", align="center", font=("Arial",14, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f" Game Over", align="center", font=("Arial", 14, "normal"))
