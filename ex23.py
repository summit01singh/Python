def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "Substracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def devide(a, b):
    print "Deviding %d / %d" % (a, b)
    return a / b

print "Lets do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print "Age : %d, Height : %d, Weight : %d, IQ : %d" %(age, height, weight, iq)

# Apuzzle for extra credit , type it anyway

what = add(age, substract(height, multiply(weight, devide(100/2, 2))))

print "That becomes", what ,"Can you do it by hand"
