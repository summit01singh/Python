def distance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

x1 = input("x1 value?")
y1 = input("y1 value?")
x2 = input("x2 value?")
y2 = input("y2 value?")
print distance(x1,y1,x2,y2)
