import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.8,stretch_len=0.8)
        self.penup()
        self.color("red")
        self.refresh()
    def refresh(self):
        xcor = random.randint(-280, 280)
        ycor = random.randint(-280, 280)
        self.goto(xcor, ycor)
