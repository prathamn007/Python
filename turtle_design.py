import turtle
colors= ['red','purple','blue','green','yellow','orange']
wn= turtle.Screen()
wn.bgcolor("Black")
t= turtle.Turtle()
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
wn.exitonclick()
