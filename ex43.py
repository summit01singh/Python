import turtle
def make_window(color, ttle):
    w = turtle.Screen()
    w.bgcolor(color)

def make_turtle(t, size):
    for c in ('red', 'yellow','green','black'):
        t.color(c)
        t.forward(size)
        t.left(90)

wn = make_window("lightgreen", "Turtle")

alex= turtle.Turtle()
alex.pensize(3)
sizee = 20
for i in range(5):
    make_turtle(alex, sizee)
    alex.penup()
    alex.right(135)
    alex.forward(20)
    alex.left(135)
    alex.pendown()
    sizee = sizee + 30

turtle.mainloop()
