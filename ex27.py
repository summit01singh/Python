import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex & Tess")

tess = turtle.Turtle()
for c in ("yellow" , "Red" , "Purple"):
    tess.color(c)
    tess.pensize(3)

alex = turtle.Turtle()

for i in range(30):
    tess.forward(80)
    tess.left(120)

for i in range(30):
    alex.forward(50)
    alex.left(90)
    tess.forward(80)
    tess.left(120)


for i in range(30):
    alex.forward(50)
    alex.left(90)

turtle.mainloop()
