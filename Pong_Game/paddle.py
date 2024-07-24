from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x1,y1):
        super().__init__()
        self.create_paddle(x1,y1)

    def create_paddle(self,x1,y1):
            self.left(90)
            self.shapesize(1,5)
            self.speed(0)
            self.goto(x=x1,y=y1)
            self.penup()
            self.shape("square")
            self.color("white")

    def up(self):
        if self.distance(x=-380,y=280)>50:
            self.forward(30)

    def down(self):
         if self.distance(x=-380,y=-280)>50:
            self.backward(30)

    def up1(self):
        if self.distance(x=380,y=280)>50:
            self.forward(30)

    def down1(self):
         if self.distance(x=380,y=-280)>50:
            self.backward(30)