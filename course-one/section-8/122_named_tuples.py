class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


from collections import namedtuple
# Namedtuple is a function, it is not a class. It is a class factory

# namedtuple function returns a class. That class can be instantiated to create objects

Point2D = namedtuple('Point2D', ['x', 'y'])
pt1 = Point2D(10, 20)

print(pt1)

pt3d_1 = Point3D(10 , 20 ,30)

# the fallowing will print the object, but if you need it to look nice you need to implement __repr__ method. If you are using the tuple approach(using namedtuple function) this is already implemented.
print(pt3d_1)

p = Point2D(y=30, x=100)
print(p)

print(isinstance(p, tuple))

# The fallowing code gives me true, but in the video it is False
g1 = (10, 20)
g2 = (10, 20)

print("This should give me false: ", g1 is g2)

print("Checking equality: ", g1 == g2)

pt1 = Point2D(10, 20)
pt2 = Point2D(10, 20)

print("This should give me false, and it does: ", pt1 is pt2)

print("Checking equality: ", pt1 == pt2)

pt1 = Point3D(10, 20, 30)
pt2 = Point3D(10, 20, 30)


print("Checking for object equality: ", pt1 is pt2)

# For the below code to return true you should implement __repr__ and __eq__ methods
print("Checking for value equality: ", pt1 == pt2)

# implemeting the __repr and __eq__ methods

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False


pt1 = Point3D(10 , 20, 30)
pt2 = Point3D(10 , 20, 30)

print(pt1)
print(pt2)

print(pt1 == pt2)

# taking look at the Point2D class

print(Point2D._source)