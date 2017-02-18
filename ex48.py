import turtle

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

def draw_eqtriangle(someturtle, somesize):
    draw_poly(someturtle, 3, somesize)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")

draw_eqtriangle(alex, 100)

turtle.mainloop()
