from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard
y=Screen()

y.setup(width=600,height=600)
y.bgcolor("black")
y.title("The Snake Game..")
y.tracer(0)
snake=[]
x_axis=0

is_true=True
s=Snake()
food=Food()
score=Scoreboard()
y.listen()
y.onkey(s.up,"Up")
y.onkey(s.down,"Down")
y.onkey(s.left,"Left")
y.onkey(s.right,"Right")
while is_true:
    y.update()
    time.sleep(0.1)
    s.move()
    if s.snake[0].distance(food)<20:
        food.refresh()
        score.incr()
        s.snakeincr()
    if s.snake[0].xcor()>290 or s.snake[0].xcor()<-290 or s.snake[0].ycor()>290 or s.snake[0].ycor()<-290:
        is_true=False
        score.gameover()
    z=s.snake[1:]
    for z1 in z:
        if s.snake[0].distance(z1)<10:
            is_true=False
            score.gameover()

y.exitonclick()