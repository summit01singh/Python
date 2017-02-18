import turtle
def draw_triangle(t,sz):
    """draw a triangle of size sz"""
    for i in range(3):
        t.forward(sz)
        t.left(120)

wn = turtle.Screen()
wn.bgcolor("green")
alex = turtle.Turtle()
draw_triangle(alex,150)

turtle.mainloop()
