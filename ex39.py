import turtle

def draw_multi_color_square(t,sz):
    '''make turtle draw a multicolor square of size sz'''
    for i in ('red','yellow','green','pink'):
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor('black')

alex = turtle.Turtle()
alex.pensize(3)

size = 20
for i in range(150):
    draw_multi_color_square(alex,size)
    size = size+2
    alex.forward(10)
    alex.right(18)


turtle.mainloop()
