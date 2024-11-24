# example for a number with infinite binary representation
from fractions import Fraction;
print(0.1)
print(Fraction(0.1))
print(format(0.1, ".15f"))
print(format(0.1, ".25f"))

# example for a number with finite binary representation
print(0.125)
print(Fraction(0.125))
print(format(0.125, ".15f"))
print(format(0.125, ".25f"))

# We need to watch out for this because the fallowing can happen

a = 0.1 + 0.1 + 0.1
b = 0.3

print(a == b)

print(format(a, ".25f"))
print(format(b, ".25f"))

# And as you can see, they're not exactly equal. And that's because we have these approximate representations for our floating point numbers, even though they have an exact representation in base ten.0.3 is exact in base ten.0.1 is exact in base ten.They are, however, not exact when you use base two representations.