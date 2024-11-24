a, b, *c = 10, 20, 'a', 'b'

print(a, b, c)

def func1(a, b, *c):
    print(a)
    print(b)
    print(c)

print("########################")
func1(10, 20)
print("########################")

print("########################")
func1(10, 20, 1, 2, 3)
print("########################")

print("########################")
def avg(*args):
    print(args)

avg(10, 20)
print("########################")

def avg(*args):
    count = len(args)
    totol = sum(args)
    return count and totol/ count

print(avg())
print(avg(1,2,3,4,10))
print("########################")

# To force the function to have at least one value, you can do the fallowing

print("########################")

def avg(a, *args):
    count = len(args) + 1
    totol = sum(args) + a
    return totol/ count

print(avg(2))
print(avg(1,2,3,4,10))
print("########################")

print("########################")
def func1(a, b, c):
    print(a)
    print(b)
    print(c)

l = [10, 20 ,30]
func1(*l)
print("########################")
print("########################")

def func(a, b, c, *args):
    print(a)
    print(b)
    print(c)
    print(args)

l = [10, 20, 30, 40, 50]
func(*l)

print("########################")