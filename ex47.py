import turtle

def draw_SC2(t, angle):
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length+2

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")
#alex.penup()
#alex.backward(110)
#alex.pendown()

draw_SC2(alex, 89)

turtle.mainloop()
