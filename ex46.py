import turtle
def draw_SC(t,angle):
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length+2

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color('blue')
alex.penup()
alex.pensize(2)
alex.speed(2)
alex.backward(110)
alex.pendown()

draw_SC(alex, 90)

turtle.mainloop()
