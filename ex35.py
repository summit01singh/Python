import turtle
wn = turtle.Screen()
wn.bgcolor("Red")

Ran = turtle.Turtle()

for i in (60,-43,270,-97,-43,200,-940,-17,-86):
    Ran.pensize(3)
    Ran.color("green")
    Ran.forward(100)
    Ran.left(i)


turtle.mainloop()
