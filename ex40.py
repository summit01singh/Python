import turtle
__import__('turtle').__traceable__ = False

def drawmulticolor(t, sz):
    for i in ['black', 'green','hotpink','blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor('red')


tess = turtle.Turtle()
tess.speed(10)
tess.pensize(3)

size = 20
for i in range(15):
    drawmulticolor (tess, size)
    size = size + 10
    tess.forward(10)
    tess.right(18)

wn.exitonclick()
