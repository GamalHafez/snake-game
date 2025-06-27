# Controls the snake object
from turtle import Turtle

class Snake:

    def __init__ (self):
        self.squares = []
        self.xcors = [ x * 20 for x in range (3)]
        self.create_snake()
        self.head = self.squares [-1]

    def create_snake(self):
        for x in range(len(self.xcors)):
            new_square = Turtle (shape = "square")
            new_square.color ("white")
            new_square.penup()
            new_square.goto( self.xcors[x] , 0 )
            self.squares.append(new_square)

    def move(self):
        for x in range (len(self.squares) - 1 ):
            self.squares[x].goto(self.squares[x+1].pos())
        self.head.forward(20)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)
        
    def extend(self):
        new_square = Turtle(shape = "square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(self.squares[0].pos())
        self.squares.insert(0, new_square)