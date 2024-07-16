from turtle import Turtle,Screen,colormode
import random
colormode(255)

x=Turtle()
x.hideturtle()
x.speed(10)
x.setheading(225)
x.penup()
x.forward(300)
x.setheading(0)
def color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    z=[r,g,b]
    #z=random.choice(color_list)
    return z

def dot():
    for _ in range(10):
        x.dot(15,color())
        x.penup()
        x.forward(50)

def bend():
    x.left(90)
    x.forward(50)
    x.left(90)

def forward():
    for _ in range(10):
        x.forward(50)
    x.left(180)

for _ in range(10):
    dot()
    bend()
    forward()

y=Screen()
y.exitonclick()