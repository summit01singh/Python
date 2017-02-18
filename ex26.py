import turtle
colourB = raw_input("Please enter background color:")
colourT = raw_input("Please enter alex color:")
thick = int(input("Please enter pensize:"))
wm = turtle.Screen()
wm.bgcolor(colourB)
wm.title("Hello, Test!")

alex = turtle.Turtle()
alex.color(colourT)
alex.pensize(thick)

alex.forward(50)
alex.left(90)
alex.forward(10)
alex.right(90)
alex.forward(20)

turtle.mainloop()
