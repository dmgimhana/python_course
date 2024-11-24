help(int)

def my_func(a, b = 1):
    # some comment here
    """ return a * b

    some additional docs here

    Input:

    Outputs:

    """
    return a * b


help(my_func)

print(my_func.__doc__)

def my_func(a: 'annotation for a', b: 'annotation of b') -> 'something with a long annotation':
    """documentation for my_func"""
    return a * b

help(my_func)

print(my_func.__doc__)
print(my_func.__annotations__)

x = 3
y = 5
def my_func(a: 'some characters', b = max(x, y)) -> 'character a repeated ' + str(max(x,y)) + ' times':
    print(b)
    return a * max(x, y)

# The annotations does not changes once they get evaluated. They get evaluated when the function is created
print(my_func('a'))
print(my_func.__annotations__)
x = 10
print(my_func('a'))
print(my_func.__annotations__)

print("########################################")

def my_func(a: str, 
            b: 'int > 0' = 1, 
            *args: "Some extra positional args ", 
            k1: "keyword-only arg 1",
            k2: "keyword-only arg 2" = 100,
            **kwargs: 'some extra keyword-only args') -> 'something':
        print(a, b, args, k1, k2, kwargs)

help(my_func)

print(my_func.__annotations__)

my_func(1, 2, 3, 4, 5, k1=10, k3=300, k4=400)