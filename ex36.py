import turtle
wn = turtle.Screen()
wn.bgcolor("Yellow")
watch = turtle.Turtle()
watch.shape("turtle")
watch.color("red")
turtle.stamp()
angle = 30
for i in range(12):
    watch.penup()
    watch.forward(100)
    watch.pendown()
    watch.forward(25)
    watch.penup()
    watch.forward(15)
    watch.stamp()
    watch.home()
    watch.right(angle)
    angle = angle + 30

turtle.mainloop()
