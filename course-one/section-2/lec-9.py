from math import sqrt
import math;

s = [1,2,3]

print(len(s));

print(sqrt(4));

print(math.pi)

def func_1():
    print('running func_1')


print("prints function obj in memory ",func_1)

def func_2(a:int, b:int):
    return a * b


print("value ",func_2(2, 3))

print("string a into 3 ", func_2("a", 3))

def func_3():
    return func_4()

def func_4():
    return 'running func_4'

print(func_4())

print(type(func_4))

fn1 = lambda x: x ** 2;

print(fn1(3))