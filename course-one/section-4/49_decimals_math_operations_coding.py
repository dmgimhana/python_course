import decimal
from decimal import Decimal;


print("########### using floats ############")
x = 10
y = 3

print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

print("########### using decimals ############")
x = Decimal(10)
y = Decimal(3)

print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

# Results are identical for positive numbers

print("########### using floats ############")
x = -10
y = 3

print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

print("########### using decimals ############")
x = Decimal(-10)
y = Decimal(3)

print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

print(help(Decimal))

# If you are using the math module on decimals, the math module first convert your number to a float. So you might lose some precision due to this convertion. So better if you can avoid using the math module with decimals. Try to use the arithmatic methods defined in the decimal class.

a = Decimal('0.1')
print(a.ln())
print(a.exp())
print(a.sqrt())

import math
math.sqrt(a)

print("######################## EXAMPLE ONE ###########################")
x = 2
x_dec = Decimal(2)
root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float,'1.27f'))
print(format(root_mixed,'1.27f'))
print(root_dec)

print(format(root_float * root_float,'1.27f'))
print(format(root_mixed * root_mixed,'1.27f'))
print(root_dec * root_dec)


print("######################## EXAMPLE TWO ###########################")
x = 0.01
x_dec = Decimal('0.01')
print(format(x, '.27f'))
print(format(x_dec, '.27f'))

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float,'1.27f'))
print(format(root_mixed,'1.27f'))
print(root_dec)

print(format(root_float * root_float,'1.27f'))
print(format(root_mixed * root_mixed,'1.27f'))
print(root_dec * root_dec)