from turtle import Turtle,Screen

class Snake:
    def __init__(self):
        self.snake=[]
        self.x_axis=0
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            self.add()
            

    def add(self):
        self.x=Turtle()
        self.x.shape("square")
        self.x.color("white")
        self.x.penup()
        self.x.goto(x=self.x_axis,y=0)
        self.x_axis=self.x_axis-20
        self.snake.append(self.x)

    def snakeincr(self):
        self.add()

    def move(self):
            for x in range(len(self.snake)-1,0,-1):
                new_x=self.snake[x-1].xcor()
                new_y=self.snake[x-1].ycor()
                self.snake[x].goto(new_x,new_y)
            self.snake[0].forward(20)

    def up(self):
         if self.snake[0].heading()!=270:
            self.snake[0].setheading(90)
    def down(self):
         if self.snake[0].heading()!=90:
            self.snake[0].setheading(270)
    def left(self):
         if self.snake[0].heading()!=0:
            self.snake[0].setheading(180)
    def right(self):
         if self.snake[0].heading()!=180:
            self.snake[0].setheading(0)

    
