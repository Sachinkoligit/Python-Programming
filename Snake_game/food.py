from turtle import Turtle,Screen
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        _x=random.randint(-290,290)
        _y=random.randint(-290,290)
        self.goto(x=_x,y=_y)
        
        