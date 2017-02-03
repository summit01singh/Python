#This one is like your scripts with arg.
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


#Ok, that *args is actuallypointless, we can just do this.
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just have one argument
def print_one(arg1):
    print "arg1 %r" % arg1

#This one takes no argument.
def print_none():
    print "I got nothing."

print_two ("Sumit", "Singh")
print_two_again ("Sumit", "Singh")
print_one ("Sumit")
print_none ()
