x = 0.1
print(format(x, '0.25f'))

x = 0.125
print(format(x, '0.25f'))

x = 0.125 + 0.125 + 0.125
y = 0.375
print(x == y)
# This is true because 0.125 and 0.375 have finite binary representations

x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)
# This is false because 0.1 and 0.3  does not have finite binary representations, therefore they only be stored as approxiamations in the float data type

print(format(x, '0.25f'))
print(format(y, '0.25f'))
print(round(x, 3) == round(y,3))

x = 10000.01
y = 10000.02
print(y/x)

x = 0.01
y = 0.02
print(y/x)

print(round(x, 1) == round(y, 1))

x = 10000.01
y = 10000.02

print(round(x, 1) == round(y, 1))

from math import isclose
help(isclose)

x = 0.1 + 0.1 + 0.1
y = 0.3

print(isclose(x, y))
print(x == y)

x = 123456789.01
y = 123456789.02
print(isclose(x, y, rel_tol=0.01))

x = 0.01
y = 0.02
print(isclose(x, y, rel_tol=0.01))

x = 0.0000001
y = 0.0000002
print(isclose(x, y, rel_tol=0.01))
print(isclose(x, y, rel_tol=0.01, abs_tol=0.01))

print("-------------------------")

x = 0.0000001
y = 0.0000002

a = 123456789.01
b = 123456789.02

print(isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
print(isclose(a, b, abs_tol=0.0001, rel_tol=0.01))