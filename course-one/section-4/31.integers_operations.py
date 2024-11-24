# All arithmatic operations performed on an int will return you a int except for division.Division will result in a float, even the number gets divided exactly. Ex :- 10/2

print(type(1 + 1))
print(type(2 * 3))
print(type(4 - 10))
print(type(3 ** 6))
print(type(2/3))
print(type(10/2))

import math

print(math.floor(7.15))
print(math.floor(-7.15))

# Here is something interesting
print(math.floor(-3.0000001))
print(math.floor(-3.000000000000000000000000000000001))

# The above has to with float having a limited precision in python. The one get droped in -3.000000000000000000000000000000001 

a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))

a = -33
b = 16
print(a/b)
print(a//b)
print("float: ",math.floor(a/b))
print("trunc: ",math.trunc(a/b))

# When dealing with negative numbers the floor and the truncation are not the same thing. It is if you are dealing with positive numbers

# a = b * (a // b) + (a % b)
# The above equation should be satisfied when dividing integers

a = 13
b = 4

print('{0}/{1} = {2}'.format(a,b,a/b))
print('{0}//{1} = {2}'.format(a,b,a//b))
print('{0}%{1} = {2}'.format(a,b,a%b))
print( a == b * (a // b) + (a % b))

a = -13
b = 4

print('{0}/{1} = {2}'.format(a,b,a/b))
print('{0}//{1} = {2}'.format(a,b,a//b))
print('{0}%{1} = {2}'.format(a,b,a%b))
print( a == b * (a // b) + (a % b))

a = 13
b = -4

print('{0}/{1} = {2}'.format(a,b,a/b))
print('{0}//{1} = {2}'.format(a,b,a//b))
print('{0}%{1} = {2}'.format(a,b,a%b))
print( a == b * (a // b) + (a % b))

a = -13
b = -4

print('{0}/{1} = {2}'.format(a,b,a/b))
print('{0}//{1} = {2}'.format(a,b,a//b))
print('{0}%{1} = {2}'.format(a,b,a%b))
print( a == b * (a // b) + (a % b))


