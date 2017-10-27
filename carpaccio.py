import sys


tax_rates = {
    "UT": .0685,
    "NV": .08,
    "TX": .0625,
    "AL": .04,
    "CA": .0825,
}

discount = {
    50000: .15,
    10000: .1,
    7000: .07,
    5000: .05,
    1000: .03,
}

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


def check_isstate(value):
    if value not in tax_rates.keys():
        print("%s was not recognized as a state" % value)
        exit(1)
    return value


def get_discount(total):
    for threshold in discount.keys():
        if total >= threshold:
            return total * discount[threshold]
    return 0
        

price = check_nonnegative(user_input("price", float), "price")
print("item price: %.2f" % price)

qty = check_nonnegative(user_input("quantity", float), "quantity")
print("quantity: %.2f" % qty)

state = check_isstate(user_input("state", str))
print("state: %s" % state)

tax = price * qty * tax_rates[state]
subtotal = price * qty * (1 + tax_rates[state])
discount = get_discount(subtotal)
total = subtotal - discount
print("tax:         %8.2f" % tax)
print("discount:    %8.2f" % discount)
print("total price: %8.2f" % total)
