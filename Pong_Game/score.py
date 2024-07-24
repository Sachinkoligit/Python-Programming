from turtle import Turtle

class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score=0
        self.create_score(position)

    def create_score(self,position):
        self.goto(position)
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color("white")
        self.write(f"{self.score}",False,"center",("Courier",80,"normal"))

    def incr(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}",False,"center",("Courier",80,"normal"))
    
    def current_score(self):
        return self.score
    
    def message(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER",False,"center",("Courier",80,"normal"))