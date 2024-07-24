from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.shapesize(1,1)
        self.speed(0)
        self.color("white")
        self.x=10
        self.y=10

    def move(self):
        _x=self.xcor()+self.x
        _y=self.ycor()+self.y
        self.goto(x=_x,y=_y)

    def bounce(self):
       self.y*=-1 

    def bounce1(self):
        self.x*=-1

    def b_reset(self):
        self.goto(0,0)
