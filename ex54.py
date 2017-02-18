x = input("Please enter the value for x: ")
def print_square_root(x):
    if x <= 0:
        print("Positive numbers only")
        return
    result = x**0.5
    print("The square root of", x, "is", result)
print_square_root(x)
