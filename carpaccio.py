import sys

def user_input(name):
    value = 0
    try:
        value = float(input("%s? " % name))
    except ValueError:
        print("could not understand %s" % name)
        exit(1)

    if value < 0:
        print("%s must be non-negative" % name)
        exit(1)

    return value


price = user_input("price")
print("item price: %.2f" % price)

qty = user_input("quantity")
print("quantity: %.2f" % qty)
