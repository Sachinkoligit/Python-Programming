from turtle import Turtle
import time
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=-1
        self.hideturtle()
        self.color("white")
        self.goto(x=0,y=270)
        self.incr()
    def incr(self):
        self.clear()
        self.score+=1
        self.write(arg=f"Score: {self.score}",align="center",font=("Courier",15,"normal"))
    def gameover(self):
        self.color("blue")
        self.goto(x=0,y=0)
        self.write(arg=f"GAME OVER",align="center",font=("Courier",30,"normal"))
        self.goto(x=0,y=-30)
        self.write(arg=f"Highest Score: {self.score}",align="center",font=("Courier",30,"normal"))

