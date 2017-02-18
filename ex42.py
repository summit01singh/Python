
import turtle
def make_window(color, ttle):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(ttle)

def make_turtle(t, size):
    for c in ('red', 'yellow','green','black'):
        t.color(c)
        t.forward(size)
        t.left(90)

wn = make_window("lightgreen", "Turtle")

alex= turtle.Turtle()
alex.pensize(3)

for i in range(5):
    make_turtle(alex, 20)
    alex.penup()
    alex.forward(40)
    alex.pendown()

turtle.mainloop()
