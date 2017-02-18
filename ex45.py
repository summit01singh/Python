import turtle
def draw_SC(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color('blue')
alex.pensize(2)
for i in range(20):
    draw_SC(alex,100)
    alex.left(18)

turtle.mainloop()
