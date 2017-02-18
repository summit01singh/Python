import turtle
wn = turtle.Screen()
wn.bgcolor("black")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("Red")

tess.penup()
size = 20
for i in range(30):
    tess.stamp()
    size = size + 2
    tess.forward(size)
    tess.right(24)


tess.color("green")
tess.pendown()
tess.forward(150)

turtle.mainloop()
