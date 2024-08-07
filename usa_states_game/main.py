import turtle
import pandas

x=turtle.Turtle()
y=turtle.Screen()
image='blank_states_img.gif'
y.addshape(image)
x.shape(image)
data=pandas.read_csv('50_states.csv')

final=[]
states=data['state'].to_list()
while len(final)<=50:
    state=y.textinput(title=f"{len(final)}/50 Guess the State",prompt="Enter the State's name:").title()
    if state=='Break':
        break
    else:
        if state in states:
            final.append(state)
            x1=data[data.state==state]
            x_axis=x1.x.item()
            y_axis=x1.y.item()
            t=turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(x=x_axis,y=y_axis)
            t.write(f"{state}",font=("Arial",10,"normal"))

remaining=[]
for s in states:
    if s not in final:
        remaining.append(s)
dict={
    'states':remaining
}
new_data=pandas.DataFrame(dict)
new_data.to_csv('remaining_states.csv')

y.exitonclick()

