import turtle
wn = turtle.Screen()
wn.bgcolor("Red")

hexa = turtle.Turtle()
hexa.color("green")
hexa.shape("turtle")
hexa.penup()
for i in (0,45):
    hexa.stamp()
    hexa.forward(150)
    hexa.left(i)

turtle.mainloop()
