print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(100))
print(help(int))

# Underneath Python calls for __bool__() and __len__() dender methods. It first checks for __bool__() and if it is not found then it checks for __len__(). If these methods are not implemented by the class of the object. Then the Truthy value will be always True

print((100).__bool__())
print((0).__bool__())

print(bool(0))
a = []
print(bool(a))
print(a.__len__())
print(bool(a))
print(a.__len__())

print(bool(0.0), bool(0+0j))

import decimal
from decimal import Decimal;
from fractions import Fraction

print(Fraction(0,1), bool(Decimal('0.0')))

print(bool(10.5), bool(1j), bool(Fraction(1,2)), bool(Decimal('10.5')))

a = []
b = ''
c = ()

print(bool(a), bool(b), bool(c))

a = [1,2]
b = 'abc'
c = (1,2)

print(bool(a), bool(b), bool(c))

a = {'a':1}
b = {1,2}

print(a,b)

print(bool(a), bool(b))

print(bool(None))

a = [1,2,3]
if a is not None and len(a) > 0:
    print(a[0])
else:
    print('Nothing to see here...')

a = None
if a:
    print(a[0])
else:
    print('Nothing to see here...')