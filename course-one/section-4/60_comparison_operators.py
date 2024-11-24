import decimal
from decimal import Decimal
from fractions import Fraction;


# returns true because there is an exact binary representation
print(10.0 == Decimal('10.0'))

# returns false because there is no exact binary representation
print(0.1 == Decimal('0.1'))

print(Decimal('0.125') == Fraction(1,8))

print(True == 1)

print(True == Fraction(3,3))

print(1 < 3.14)

import math

print(Fraction(22, 7) > math.pi)

print(Decimal('0.5') <= Fraction(2,3))

print(True < Decimal('3.14'))

print(Fraction(2, 3) > False)

# Chained Comparisons
print("############ CHAINED COMPARISONS ############")

# a == b == c is equivalent to a == b and b == c
# a < b < c is equivalent to a < b and b < c

print(1 == Decimal('1.0') == Fraction(1, 1)) 

print(1 == Decimal('1.5') == Fraction(3, 2)) 

# Below is equivalent to 1 < 2 and 2 < 3
print(1 < 2 < 3) 

# Below is equivalent to 1 < math.pi and math.pi < Fraction(22, 7)
print(1 < math.pi < Fraction(22, 7))

a = 10
b = 20
c = 30
d = 70
# Below is equivalent to a < b and b > c
print(a < b > c) 

# Below is equivalent to a < b and b > c and c < d
print(a < b > c < d) 

print("************************************")
import string
print('A' < 'a' < 'z' > 'Z' in string.ascii_letters)
print("************************************")

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
min = 0
max = 100
age = 34
print(min < age < max)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


print(0.1 is (3+4j))
print(3 is 3)
print([1,2] is [1,2])
print('a' is 'this is a test')
print(3 in [1,2,3])
print(3 not in [1,2,3])
print('key1' in {'key1':1})
print(1 in {'key1':1})

print("#################################")

print(4 < Decimal('10.5'))
print(Fraction(2,3) < Decimal('0.5'))

# Below. For equality testing you can use complex numbers, but not for ordering
print(4 == 4 + 0j)
# print(4 < 4 + 0j) This is not supported

print(True == Fraction(2,2))

print(True < Fraction(3,2))