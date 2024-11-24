def outer():
    x = "python"
    def inner():
        print(x)
    return inner

fn = outer()

print(fn.__code__.co_freevars)

print(fn.__closure__)

# String interning will give us same address like shown below, eventhough we created a new variable in inner method

def outer():
    x = "python"
    print(hex(id(x)))
    def inner():
        x = "python"
        print(hex(id(x)))
    return inner

fn = outer()

print(fn())

print("####################################")

def outer():
    x = [1, 2, 3]
    print(hex(id(x)))
    def inner():
        y = x
        print(hex(id(y)))
    return inner

fn = outer()

print(fn.__closure__)

print(fn())
print("####################################")
print("####################################")

def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

fn = outer()

print(fn.__code__.co_freevars)
print(fn.__closure__)
print(hex(id(0)))

print(fn())

print(fn.__closure__)

print(hex(id(1)))

print("####################################")
print("####################################")

def outer():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count
    
    def inc2():
        nonlocal count
        count += 1
        return count
    
    return inc1, inc2

fn1, fn2 = outer()

print(fn1.__code__.co_freevars, fn2.__code__.co_freevars)

print(fn1.__closure__, fn2.__closure__)

print(fn1())

print(fn1.__closure__, fn2.__closure__)

print(fn2())

print(fn1.__closure__, fn2.__closure__)

print("####################################")
print("####################################")

def pow(n):
    def inner(x):
        return x ** n
    return inner

square = pow(2)

print(square.__closure__)

print(hex(id(2)))

print(square(5))

cube = pow(3)

print(cube.__closure__)

print(hex(id(3)))

print(cube(5))

print("####################################")
print("####################################")

def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print(add_1.__closure__, add_2.__closure__, add_3.__closure__)

print(add_1(10))

print(add_2(10))

print(add_3(10))

print("####################################")
print("####################################")

adders = []

# In the below code, since we are refering to the global n, no closures are created

for n in range(1, 4):
    adders.append(lambda x: x + n)

print(n)

print(adders[0].__closure__)

print(adders[0](10))
print(adders[1](10))
print(adders[2](10))

print("####################################")
print("####################################")

# Unlike above, since we are creating lambda inside a function, we are creating closures

def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders

adders = create_adders()

print(adders[0].__closure__)

print(adders[1].__closure__)

print(adders[2].__closure__)

print(adders[0](10))
print(adders[1](10))
print(adders[2](10))

print("####################################")
print("####################################")

def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x, y=n: x + y)
    return adders

adders = create_adders()

# No cloures, so no free variables.No cloures are created here because the n is not bounded to any of the functions.

print(adders[0].__closure__)

print(adders[0].__code__.co_freevars)

print(adders[0](10))

print(adders[1](10))

print(adders[2](10))

# If you use a closure, you're going to have a common end.So if you don't want that, don't use a closure. A common trick is to use a default so that you get the assignment at creation time and not a closure,not a free variable that gets evaluated at runtime at call time of the closure.
