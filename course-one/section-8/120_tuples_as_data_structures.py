a = 'a', 10, 200
print(a[0])

a = 1, 2, 3, 4, 5
print(type(a))
print(a[2:5])

for e in a:
    print(e)


# Unpacking tuples
b = 'b', 20, "30"
x, y, z = b
print(x, " ", y, " ", z)

c = 1, 2, 3, 4, 5
x, *other, y, z = a

print(x, " ", other, " ", y, " ", z)

r = 1, 2, 3, 4, 5
x, *_, y, z = r

print(x, " ", _, " ", y, " ", z)

# Tuples are immutable. So the fallowing will give you an error
# a[0] = "200"

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'{self.__class__.__name__} (x={self.x}, y={self.y})'
    
pt = Point2D(10, 20)

print(pt)
print(id(pt))

pt.x = 100

print(pt)
print(id(pt))

a = Point2D(0, 0), Point2D(10, 20)
print(a)
print(id(a[0]))

a[0].x = 1000
print(a)

s = 'python'

print(id(s))

s = 'python' + 'rocks!'

print(id(s))

z = 1, 2, 3

print(id(z))

z += (4, 5)

print(id(z))

print(z)

pt1 = (0, 0)
pt2 = (10, 20)

london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000

print(london)
print(new_york)
print(beijing)

cities = (london, new_york, beijing)

# Very often you will find that list are homogenous as opposed to tuples, because we want to be able to do same thing over and over to a list of elements. But tuples are generally not homogeneous because we are using them as data structures

# List are typically homogenous, but they can be heterogenous

total = 0
for city in cities:
    total += city[2]
print("total: ", total)

# cleaner way of writting the above code
total = sum([city[2] for city in cities])

print("total generated by the above cleaner code :-): ", total)

record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072

symbol, year, month, day, open_, high, low, close = record

print(symbol, " ", year, " ", month, " ", day, " ", open_, " ", high, " ",low, " ", close )

symbol, *_, close = record

p = symbol,close

print(p)
print(_)

for city, country, population in cities:
    print(city, country, population)

for item in enumerate(cities):
    print(item)

for index, city in enumerate(cities):
    print(index, ":", city)


# The position of the value in a tuple has meaning


from random import uniform
from math import sqrt

def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)


    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False
    
    return random_x, random_y, is_in_circle

num_attempts = 100
count_inside = 0

for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately: {4 * count_inside / num_attempts}')