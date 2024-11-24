class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count
    

a = Averager()

print(a.add(10))

print(a.add(20))

print(a.add(30))

b =  Averager()

print(b.add(10))

print("################################")
print("################################")

def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add

a = averager()

print(a(10))

print(a(20))

print(a(30))

b = averager()

print(b(10))

print(a.__closure__)
print(b.__closure__)

print("################################")
print("################################")

def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1
        return total / count
    return add

a = averager()

print(a.__closure__)

print(a.__code__.co_freevars)

print(a(10))

print(a(20))

# If we were to implmentent the above cloure using a class it would be as fallows.However implementing this using a cloure has less overhead than using a class

class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count
    

print("################################")
print("################################")

from time import perf_counter

print(perf_counter())
print(perf_counter())

class Timer:
    def __init__(self):
        self.start = perf_counter()

    def poll(self):
        return perf_counter() - self.start
    
t1 = Timer()

print(t1.poll())

print(t1.poll())

print("################################")
print("################################")

class Timer:
    def __init__(self):
        self.start = perf_counter()

    # This just says that, It just says that the instance that gets created from this class is a callable.And when it gets called right by putting these parentheses in, it's going to call this method over

    def __call__(self):
        return perf_counter() - self.start
    
t1 = Timer()

print(t1())

print(t1())

print("################################")
print("################################")

def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

t2 = timer()

print(t2())

print(t2())

print("################################")
print("################################")

# Below code is using the class
print(t1()) 

# Below code is using the closure
print(t2())