def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        """
        this is the inner closure
        """
        nonlocal count
        count += 1
        print("Function {0} (id={1}) was called {2} times".format(fn.__name__,id(fn), count))
        return fn(*args, **kwargs)
    return inner


def add(a:int, b:int = 0):
    """
    adds two values
    """
    return a + b

help(add)

print(id(add))

add = counter(add)

print(id(add))

help(add)

print(add(10, 20))

print(add(20, 30))

print(add(10))

def mult(a: int, b:int, c: int = 1, *, d):
    """
    multiplies four values
    """
    return a * b * c * d

print(mult(1,2,3,d=4))

print(mult(1, 2, d=3))

mult = counter(mult)

help(mult)

print(mult(1,2,3,d=4))

print(mult(1,2,d=3))

@counter
def my_func(s:str, i:int) -> str:
    return s * i

help(my_func)

print(my_func('a', 10))

help(my_func)

print(mult.__name__)

print(mult.__doc__)

help(mult)

print("###########################################")

from functools import wraps

def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        """
        this is the inner closure
        """
        nonlocal count
        count += 1
        print("Function {0} (id={1}) was called {2} times".format(fn.__name__,id(fn), count))
        return fn(*args, **kwargs)
    inner = wraps(fn)(inner)
    return inner


def mult(a: int, b:int, c: int = 1, *, d):
    """
    multiplies four values
    """
    return a * b * c * d

mult = counter(mult)

help(mult)