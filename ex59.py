import turtle
def graph(t, height):
    if(height > 200):
        tess.color('green')
    elif(height >= 100 and height <= 200):
        tess.color('yellow')
    else:
        tess.color('blue')

    t.begin_fill()
    t.left(90)
    t.forward(height)
    if(height > 0):
        t.write('   ' + str(height))
    t.right(90)
    t.forward(40)
    if(height < 0):
        t.write('   ' + str(height))
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor('red')

tess = turtle.Turtle()

xs = [48,117,200,240,160,260,-220]

for a in xs:
    graph(tess, a)

turtle.mainloop()
