from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = randint(-200, 200)
        rand_y = randint(-200, 200)
        self.goto(rand_x, rand_y)