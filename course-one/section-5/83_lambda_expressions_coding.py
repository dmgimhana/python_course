def sq(x):
    return x ** 2

print(type(sq))

lambda x: x ** 2

print(type(lambda x, y : x + y))

f = sq

print(id(f), id(sq))

f(3)

sq(3)

f = lambda x: x ** 2

print(f(3))

g = lambda x, y = 10 : x + y

print(g(1,2))

print(g(1))

f = lambda x, *args, y, **kwargs:(x, args, y, kwargs)

print(f(1, 'a', 'b', y=100, a=10, b=20))

def appy_func(x, fn):
    return fn(x)

print(appy_func(5, lambda x: x**2))

print(appy_func(5, lambda x: x**3))

def appy_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

print(appy_func(sq, 3))

print(appy_func(lambda x: x ** 2, 3))

print(appy_func(lambda x, y : x + y, 1,2))

print(appy_func(lambda x, *, y: x + y, 1, y = 20))

print(appy_func(lambda *args: sum(args), 1,2,3,4,5))

print(appy_func(sum ,(1,2,3,4,5)))

print(sum((1,2,3,4,5)))