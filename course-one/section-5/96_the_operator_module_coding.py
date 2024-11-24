import operator
print(dir(operator))

print(operator.add(2,3))
print(operator.mul(7,2))
print(operator.truediv(3,2))
print(operator.floordiv(13, 2))


from functools import reduce

print(reduce(lambda x, y : x * y, [1, 2, 3, 4]))

print(reduce(operator.mul, [1,2,3,4]))

print(operator.lt(10, 3))

from operator import is_ 

print(is_('abc', 'def'))

print(is_('abc', 'abc'))

print(operator.is_('abc', 'def'))

print(operator.is_('abc', 'abc'))

print(operator.truth([]))

print(operator.truth([1]))

my_list = [1, 2, 3, 4]

print(my_list[1])

print(operator.getitem(my_list, 1))

my_list[1] = 100

print(my_list)

del my_list[3]

print(my_list)

my_list = [1, 2, 3, 4]

operator.setitem(my_list, 1, 100)

print(my_list)

operator.delitem(my_list, 3)

print(my_list)

# Using the partial function itemgetter

f = operator.itemgetter(2)

# Below is of type function eventhough it prints <class 'operator.itemgetter'>
print(type(f))

my_list = [1, 2, 3, 4]

print(f(my_list))

s = 'python'
print(f(s))

f = operator.itemgetter(2, 3)
print(type(f))

my_list = [1, 2, 3, 4]

print(f(my_list))

print(f('python'))

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('text method running...')

obj = MyClass()

print(obj)

print(obj.a)

print(obj.b)

print(obj.test)

print(obj.test())

print("####################")

prop_a = operator.attrgetter('a')
print(prop_a(obj))

my_var = 'b'

prop_b = operator.attrgetter(my_var)
print(prop_b(obj))

print(operator.attrgetter(my_var)(obj))

my_var = 'c'
print(prop_b(obj))

operator.attrgetter('a', 'b')(obj)

items = operator.attrgetter('a','b','test')(obj)
print(items)

a, b, test = operator.attrgetter('a','b','test')(obj)
print(items)

print(a)
print(b)
print(test)
print(test())

f = lambda x: x.a
print(f(obj))

f = lambda x: x[2]
x = [1, 2, 3, 4]
print(f(x))

f = lambda x: (x[2],  x[3])
x = [1, 2, 3, 4]
print(f(x))

a = 5 + 10j

print(a)

print(a.real)

l = [5-10j, 3+3j, 2-100j]

print(sorted(l, key=lambda x: x.real))

print(sorted(l, key = operator.attrgetter('real')))

l = [(2, 3, 4), (1, 3, 5), (6,),(4, 100) ]

print(sorted(l, key = lambda x: x[0]))

print(sorted(l, key = operator.itemgetter(0)))

print("#####################################")

obj = MyClass()

f = operator.attrgetter('test')

print(f(obj))

print(f(obj)())

f = operator.methodcaller('test')

print(f(obj))

print("###############################")

class MyClassTwo:
    def __init__(self):
        self.a = 10
        self.b = 20

    def test(self, c):
        print(self.a, self.b, c)
    
    def test2(self, c, d):
        print(self.a, self.b, c, d)

    def test3(self, c, d, *, e):
        print(self.a, self.b, c, d, e)


obj = MyClassTwo()

print(obj.a)

print(obj.b)

print(obj.test(100))

print(operator.methodcaller('test',100)(obj))

print(operator.methodcaller('test2',100,200)(obj))

print(operator.methodcaller('test3', 100, 200, e = 300)(obj))

f = operator.attrgetter('test3')

print(f(obj)(10, 20, e = 100))

