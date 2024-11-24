from fractions import Fraction;
print(Fraction(1))
print(Fraction(5,1))
print(Fraction(denominator=1, numerator=5))
print(Fraction( numerator=5,denominator=1))
print(Fraction(0.125))
print(Fraction("0.125"))
print(Fraction("22/7"))
x = Fraction(2, 3)
y = Fraction(3,4)
# All arithmatic operation using fractions returns fraction type
print(x + y)
print(x * y)
print(x / y)

print(Fraction(8/16))
print(Fraction(-1/4))
print(Fraction(1/-4))
x = Fraction(1,-4)
print(x.numerator)
print(x.denominator)

import math

# PI is not a rational number in mathematics. But there PI can only be represented in our computer using only certain number of digits, therefore it can be taken as a rational number. 

# PI is approximated in this case because some of the precition is lost
x = Fraction(math.pi)
print(x)
print(float(x))

y = Fraction(math.sqrt(2))
print(y)
print(float(y))

# Not all floating point numbers can be represent exactly in the computer. This will be covered later
a = 0.125
print(a)
b = 0.3
print(b)

print(Fraction(a))
print(Fraction(b))

print(format(b, "0.5f"))
print(format(b, "0.15f"))
# The below print shows how exctly python stores 0.3. We we print 0.3 is displays 0.3. This is just python making the output pretty. The actual 0.3 representation is something around 0.2999999999999999888977698. Because of this we got the faction that we got
print(format(b, "0.25f"))
print(format(b, "0.100f"))
print(Fraction(b))

x = Fraction(0.3)
print(x)
print(x.limit_denominator(10))

y = Fraction(math.pi)
print(y)
print(y.limit_denominator(10))
print(y.limit_denominator(100))