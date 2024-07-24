from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
y=Screen()
y.bgcolor("black")
y.title("Pong Game")
y.setup(width=800,height=600)
y.tracer(0)
x=Turtle()
x.penup()
x.pensize(5)
x.color("white")
x.goto(x=0,y=270)
x.right(90)
x.hideturtle()
for _ in range(25):
    x.pendown()
    x.forward(10)
    x.penup()
    x.forward(10)

s_l=Score((-100,200))
s_r=Score((100,200))
p_l=Paddle(-380,0)
p_r=Paddle(380,0)
game_on=True
y.listen()
y.onkey(p_l.up,"w")
y.onkey(p_l.down,"s")
y.onkey(p_r.up1,"Up")
y.onkey(p_r.down1,"Down")
ball=Ball()

x=0.1
while game_on:
    time.sleep(x)
    y.update()
    ball.move()
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce()

    if(ball.xcor()>350 and ball.distance(p_r)<50) or (ball.xcor()<-350 and ball.distance(p_l)<50):
        ball.bounce1()
        x-=0.005

    if ball.xcor()>380 :
        ball.b_reset()
        s_l.incr()
        x=0.1
    
    if ball.xcor()<-380:
        ball.b_reset()
        s_r.incr()
        x=0.1

    if s_l.current_score()>=6 or s_r.current_score()>=6:
        game_on=False
        s_l.message()
y.exitonclick()