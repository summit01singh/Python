import turtle
def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Poly")

alex = turtle.Turtle()
alex.color("hotpink")
alex.pensize(2)
draw_poly(alex, 8, 100)
turtle.mainloop()
