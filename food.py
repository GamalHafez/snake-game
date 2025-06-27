# Controls food appearance
from turtle import Turtle
import random

class Food(Turtle):
    def __init__ (self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.random_appear()


    def random_appear(self):
        self.random_x = random.randint(-370,370)
        self.random_y = random.randint(-370,370)
        self.goto(self.random_x, self.random_y)

    def remove_from_screen(self):
        self.hideturtle()
        self.clear()

