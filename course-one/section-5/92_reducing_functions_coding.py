l = [5, 8, 6, 10, 9]

_max = lambda x, y: x if x > y else y

print(_max(1, 4))

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

print(max_sequence(l))

_min = lambda a, b: a if a < b else b

def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result

print(min_sequence(l))

_add = lambda a, b: a + b
def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result

print(add_sequence(l))

from functools import reduce

print(reduce(_max, l))

print(reduce(_add, l))

print(reduce(_max, {1,3,4,5}))

print(min(l))

print(min({1,2,3}))

print(max(l))

print(sum(l))

print(sum({1, 2, 3}))

s = {True, 1, 0, None}

s2 = {True, 1, "s"}

print(all(s))

print(all(s2))

print(any(s))

print(any(s2))

s3 = {False, 0, '', None}

print(any(s3))

print(reduce(lambda a, b: bool(a) and bool(b), s))

print(reduce(lambda a, b: bool(a) and bool(b), s3))

l = [1, 2, 3, 4]

print(reduce(lambda a, b: a* b, l))

print(list(range(5)))

print(list(range(1, 5 + 1)))

print(reduce(lambda a, b: a * b, range(1, 5 + 1)))

def fact(n):
    return 1 if n < 2 else n * fact(n - 1)

print(fact(5))

def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))

print(fact(5))

print(fact(2))

def _reduce(fn, sequence, initial):
    result = initial
    for x in sequence:
        result = fn(result, x)
    return result

print(_reduce(lambda a, b: a + b, l, 0))

print(_reduce(lambda a, b: a + b, l, 100))

print(_reduce(lambda a, b: a + b, {1, 2, 3, 4}, 100))

print(reduce(lambda a, b: a + b, l, 100))

