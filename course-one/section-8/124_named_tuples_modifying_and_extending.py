
# MODIFIYING TUPLES
from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')

pt = Point2D(10, 20)

print(pt.x, ' ', pt[0])

# The fallowing will give you an error because tuples are immutable
# pt.x = 100

# Instead we can build a new tuple based on the previous one

print(id(pt))

pt = Point2D(100, pt.y)

print(id(pt))

# The above approach can be used for short tuples, but we need another approach for longer tuples. There are a few approches

# Using unpacking

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

print(djia)

*values, _ = djia

print(values)

values.append(266_393)

print(values)

print(*values)

djia = Stock(*values)

print(djia)

# Using slicing

values = djia[:7]

print(values)

print(values+(100,))

djia = Stock(*(values + (100, )))

print(djia)

print(id(djia))

djia = Stock(*values, 1000)

print(djia)

print(id(djia))

# Using replace

djia = djia._replace(year=2019, open=10000)

print(djia)

print(id(djia))

# Using the make method

djia = Stock._make(values + (100,))

print(djia)

# EXTENDING TUPLES

print(Point2D)

print(Point2D._fields)

print(Point2D._fields + ('z',))

Point3D = namedtuple('Point3D', Point2D._fields + ('z', ))

print(Point3D._fields)

pt3d = Point3D(*pt, 100)

print(pt3d)