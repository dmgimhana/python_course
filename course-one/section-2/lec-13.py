class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


    @property
    def width(self):
        print("getting width")
        return self._width

    @width.setter
    def width(self, width):
        if width <=0:
            raise ValueError('Width must be positive')

        else:
            self._width = width
    
    @property
    def height(self):
        return self._height


    @height.setter
    def height(self, height):
        if height <=0:
            raise ValueError('Width must be positive')

        else:
            self._height = height
    
  

    def get_width(self):
        return self.width



    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive')
        else:
            self.width = 100

    def __str__(self):
        return "Rectangle: width={0}, height={1}".format(self.width, self.height)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.width, self.height);

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False;
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = Rectangle(20, 30)
r4 = Rectangle(40, 30)
print("width ", r1.width)

print("area ", r1.area())
print("perimeter ", r1.perimeter())

print(str(r1))
print(hex(id(r1)))

print("is not the same obj ", r1 is not r2)
print("is values are the same ", r1 == r2)
print("is r1 area less than r3", r1 < r3)


