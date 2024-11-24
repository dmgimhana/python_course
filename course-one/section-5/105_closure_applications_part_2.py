def counter(initial_value = 0):
    def inc(increment = 1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

counter1 = counter()

print(counter1())

counter2 = counter();

print(counter2())

print('############################')
print('############################')

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

counter_add = counter(add)

print(counter_add.__closure__)

print(counter_add.__code__.co_freevars)

result = counter_add(10, 20)

print(result)

counter_mult = counter(mult)

result = counter_mult(2, 5)

print(result)

print('############################')
print('############################')

counters = dict()

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

counted_add = counter(add)
counted_mult = counter(mult)

print(counted_add(10, 20))

print(counted_add(20, 30))

print(counters)

print(counted_mult(2, 5))

print(counters)

print('############################')
print('############################')

def counter(fn,counters):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

c = dict()

counted_add = counter(add, c)
counted_mult = counter(mult, c)

print(counters)

print(counted_add(10, 20))

print(counted_mult(2, 5))

print(counted_mult(3, 6))

print(counters)

print(c)

print('############################')
print('############################')

def fact(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

print(fact(3))

print(fact(5))

counted_fact = counter(fact, c)

print(counted_fact(5))

print(c)

fact = counter(fact,c)

print(fact.__closure__)

print(fact(3))

print(fact(5))

print(c)

print(fact(10))

print(c)

add = counter(add, c)

mult = counter(mult, c)

print(add(10, 20))