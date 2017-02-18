import turtle
def draw_star(t, sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")
for i in range(5):
    draw_star(alex, 100)
    #alex.penup()
    alex.forward(350)
    #alex.pendown()
    alex.right(144)

turtle.mainloop()
