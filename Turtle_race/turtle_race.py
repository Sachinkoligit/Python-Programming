from turtle import Turtle,Screen
import random
move=[20,10,30,40,50,60,70,80,90]
colors=["red","yellow","blue","green","pink","orange"]
race_on=True
y=Screen()
turtles=[]
l=260
n=""
y.setup(width=1000,height=600)
for z in range(6):
    xz=Turtle()
    xz.shape("turtle")
    xz.color(colors[z])
    xz.penup()
    xz.goto(x=-460,y=l)
    l=l-100
    turtles.append(xz)
z=y.textinput(title="xyz",prompt="Which turtle will win the race?")
while race_on:
    for turtle in turtles:
        turtle.forward(random.choice(move))
        if turtle.xcor()>420:
            race_on=False
            n=turtle.pencolor()
if z==n:
    print(f"You won the game,{n} wins the game..")
else:
    print(f"You lose the game,{n} wins the game..")
y.exitonclick()