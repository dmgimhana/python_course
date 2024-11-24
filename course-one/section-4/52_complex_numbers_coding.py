help(complex)
# real and imaginary parts are stored as floats in complex numbers

a = complex(1,2)
b = 1 + 2j


print(a == b)
print(a.real, type(a.real))
print(a.imag, type(a.imag))
print(a.conjugate())

a = 1 + 2j
b = 10 + 8j

print(a + b)
print(a * b)
print(a / b)
print(a ** 2)

# certains operations are not supported for complex numbers in python, like the div operator(//), mod operator(%), divmod.

a = 0.1j
print(format(a.imag, '.25f'))
print(a + a + a == 0.3j)
print((a + a + a).imag, '.25f')
print((0.3j).imag, '.25f')
import math
print(math.sqrt(2))
print(math.pi)

import cmath

print(cmath.pi)
print(type(cmath.pi))

# PI that we have in the math module and cmath module are the same. 
# Functions you have in the math module will not work with complex numbers

a = 1 + 2j
# print(math.sqrt(a))
# The above code will fail because math module does not support complex numbers
print(cmath.sqrt(a))

a = 1 + 1j
print(cmath.phase(a))
print(cmath.pi/4)
print(abs(a))
print(cmath.rect(math.sqrt(2), math.pi/4))
RHS = cmath.exp(complex(0, math.pi)) + 1
print(RHS)
print(cmath.isclose(RHS, 0))
print(cmath.isclose(RHS, 0, abs_tol=0.0001))

  

