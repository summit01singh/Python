import turtle
wn = turtle.Screen()
alex = turtle.Turtle()



#for i in [0,1,2,3]:
for c in ("yellow" , "Red" , "Purple" , "blue", "green", "Black"):
    alex.color(c)
    alex.speed(1)
    alex.shape("turtle")
    alex.forward(50)
    alex.left(90)

turtle.mainloop()
