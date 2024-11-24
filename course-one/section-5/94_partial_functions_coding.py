from functools import partial

def my_func(a, b, c):
    print(a, b, c)


my_func(10, 20, 30)

def f(x, y):
    return my_func(10, x, y)


f(20, 30)

f(100, 200)

f = lambda x, y: my_func(10, x, y)

f(100, 200)

f = partial(my_func, 10)

f(20, 30)

f = partial(my_func, 10, 20)

f(30)

print("######################################")

def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

my_func(10, 20, 100, 200, k1='a', k2='b', k3=1000, k4=2000)

def f(x, *vargs, kw, **kwargs):
    return my_func(10, x, *vargs, k1="a", k2="b", **kwargs)

f(20, 100, 200, kw="b", k3=1000, k4=2000)

f = partial(my_func, 10, k1="a")

f(20, 100, 200, k2='b', k3=1000, k4=2000)

def pow(base, exponent):
    return base ** exponent

sq = partial(pow, 2)

print(sq(10))

sq = partial(pow, exponent = 2)
print(sq(5))

cu = partial(pow, exponent = 3)
print(cu(5))

print(cu(base = 5))

print(cu(5, exponent = 2))

a = 2
sq = partial(pow, exponent = a)
print(sq(5))

a = 3
print(sq(5))

def my_func(a, b):
    print(a, b)

a = [1, 2]
f = partial(my_func, a)

f(100)

a.append(3)

print(a)

f(100)

print("################################")

# DOUBT
# I did not get the below example

origin = (0,0)
l = [(1,1), (0,2), (-3,2),(0,0),(10,10) ]
dist2 = lambda a, b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
print(dist2((1, 1), origin))

print(sorted(l))

f = partial(dist2, origin)

print(f((1, 1)))

print(sorted(l, key = f))

f = lambda x: dist2(origin, x)

print(sorted(l, key = f))

print(sorted(l, key = lambda x: dist2(origin, x)))

print(sorted(l, key = partial(dist2, origin)))


