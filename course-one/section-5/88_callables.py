print(callable(print))
print('hello')

print("CALLABLES ALWAYS RETURN A VALUE")
result = print('hello')
print(result)

l = [1, 2, 3]

print(callable(l.append))

result = l.append(4)

print(l)
print(result)

s = 'abc'
print(callable(s.upper))

s = 'abc'
result = s.upper()
print(result)

from decimal import Decimal

print(callable(Decimal))

a = Decimal('10.5')

print(type(a))

print(callable(a))

class MyClass:
    def __init__(self, x = 0):
        print('initializing...')
        self.counter = x

print(callable(MyClass))

a = MyClass(100)

print(a.counter)

print(callable(a))

class MyClass:
    def __init__(self, x = 0):
        print('initializing...')
        self.counter = x

    def __call__(self, x = 1):
        print('updating counter...')
        self.counter += x

b = MyClass()
MyClass.__call__(b, 10)

print(b.counter)

print(callable(b))

b()

print(b.counter)

b(100)

print(b.counter)

print('ADDING THE __call__ METHOD TO b, MADE IT CALLABLE .THIS IS HOW YOU MAKE INSTANCES OF YOUR CLASSES CALLABLE AS WELL')