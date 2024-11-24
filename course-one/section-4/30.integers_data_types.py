print(type(100))
import sys;
print(sys.getsizeof(0))
# It takes at least 28 bytes to store an integer object. Memory space of object = object space + value of the object

print(sys.getsizeof(1))


print(sys.getsizeof(2 ** 1000))
# The number of bits used in the above code is 160. That means 1088 bits. 1088 = (160 - 24) * 8;

import time

def calc(a):
    for i in range(100000):
        a * 2

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
calc(2**1000000)
end = time.perf_counter()
print(end - start)

print(2**2)