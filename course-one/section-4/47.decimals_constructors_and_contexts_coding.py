import decimal
from decimal import Decimal;

print(Decimal(10))
print(Decimal(-10))
print(Decimal('10.1'))
print(Decimal('-3.1415'))
t = (0,(3,1,4,1,5), -4)
t2 = (1,(3,1,4,1,5), -4)
t2 = (1,(3,1,4,1,5), -2)
print(Decimal(t))
print(Decimal(t2))

# Never pass is in float differectly, because it the float you are passing might not have a exact binary representation. For an example 0.1. What you should do is pass 0.1 as a string. This is not a matter with intgers, because integers have an exact representation in binary
print(format(0.1,'.25f'))
print(Decimal(0.1))
print(Decimal('0.1'))
print(Decimal(0.1) == Decimal('0.1'))
print(Decimal(10) == Decimal('10'))

print(decimal.getcontext())
decimal.getcontext().prec = 6
print(decimal.getcontext())
a = Decimal('0.123456789')
b = Decimal('0.12')
print('##################################################################')
print("Decimal a stored ", a)
print("Decimal b stored ", b)

# Precision only effects when you are doing arithmatic operations. If you store a value in a variable with a higher or lower precision it will keep it as it is as shown with variables a and b above


decimal.getcontext().prec = 2
x = Decimal('0.12345')
y = Decimal('0.12345')

print(0.12345 + 0.12345)
print(x + y)

decimal.getcontext().prec = 5
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)
with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print('c within local context: {0}'.format(c))
print('c within global context: {0}. The c is still the same because c was calculated/ created in the local context'.format(c))