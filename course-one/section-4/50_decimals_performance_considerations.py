import decimal
from decimal import Decimal;
import sys

a = 3.1415
b = Decimal('3.1415')

print(sys.getsizeof(a))
print(sys.getsizeof(b))

# So as you can see, there's quite a larger memory footprint required for decimal objects.

import time

print('############### EXAMPLE ONE ###############')
def run_float(n = 1):
    for i in range(n):
        a = 3.1415

def run_decimal(n = 1):
    for i in range(n):
        a = Decimal('3.1415')


n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)

print('############### EXAMPLE TWO ###############')
def run_float(n = 1):
    a = 3.1415
    for i in range(n):
        a + a

def run_decimal(n = 1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a


n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)


print('############### EXAMPLE THREE ###############')
import math

def run_float(n = 1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)

def run_decimal(n = 1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()


n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)