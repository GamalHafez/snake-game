# Scoreboard logic
from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__ (self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,340)
        self.update_scoreboard()

    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 18, "bold"))

    def increase_score(self):
        self.undo()
        self.score +=1
        self.update_scoreboard()

    def end_game(self):
        self.screen.bgcolor("dark blue")
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over !!\nFinal Score: {self.score}", align= "center", font = ("Arial", 22, "bold"))
        self.goto(0,-100)
        self.write(f"Wait for another chance....", align= "center", font = ("Arial", 16, "bold"))
        self.screen.update()
        time.sleep(2)

    def welcoming(self):
        self.screen.bgcolor("dark blue")
        self.clear()
        self.goto(0,0)
        self.write(f"Welcome to Gamal's game.....", align= "center", font = ("Arial", 22, "bold"))
        self.screen.update()
        time.sleep(2)