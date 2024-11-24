from math import trunc, floor, ceil


help(trunc)
print(trunc(10.3), trunc(10.5),trunc(10.9))

help(int)
print(int(10.4),int(10.9), int(10.5))

# Truncation can be done using trunc method in math module or using the int contructor.

print("-----------------------------------------------")

# floor operation is not the same as truncation. When using positive numbers it may seem that way, but to when you use negative numbers it reveals what it really does.

print(trunc(10.3), trunc(10.5),trunc(10.9))
print(trunc(-10.3), trunc(-10.5),trunc(-10.9))
print(floor(10.3), trunc(10.5),trunc(10.9))
print(floor(-10.3), trunc(-10.5),trunc(-10.9))

print("--------------------------------")

print(ceil(10.3), ceil(10.5),ceil(10.9))
print(ceil(-10.3), ceil(-10.5),ceil(-10.9))