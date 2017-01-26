from sys import argv

script, age, height, weight = argv

print "The script is called:", script
print "Your age is:", age
print "Your height is:", height
print "Your weight is:", weight

age = raw_input ("Is your age correct?")
height = raw_input ("Is your height is correct?")
weight = raw_input ("Is your weight is correct?")

print "So you are %r old, %r tall and %r heavy" %(age, height, weight)
