import sys

price = 0
try:
    price = float(input("item price? "))
except ValueError:
    print("could not understand price")
    exit(1)

if price < 0:
    print("price must be non-negative")
    exit(1)

print("item price: %.2f" % price)
