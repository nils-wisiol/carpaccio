import sys


def user_input(name, input_type):
    value = 0
    try:
        value = input_type(input("%s? " % name))
    except ValueError:
        print("could not understand %s" % name)
        exit(1)

    return value


def check_nonnegative(value, name):
    if value < 0:
        print("%s must be non-negative" % name)
        exit(1)
    return value


price = check_nonnegative(user_input("price", float), "price")
print("item price: %.2f" % price)

qty = check_nonnegative(user_input("quantity", float), "quantity")
print("quantity: %.2f" % qty)

state = user_input("state", str)
print("state: %s" % state)

total = price * qty
print("\ntotal price: %.2f" % total)
