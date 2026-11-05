import math
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        raise NotImplementedError
    def perimeter(self):
        raise NotImplementedError
    def describe (self):
        return f"{self.name} -> obsah: {self.area():.2f}, obvod: {self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self,r, name = "kruh"):
        super().__init__(name)
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def perimeter(self):
        return math.pi * 2 * self.r

class Rectangle(Shape):
    def __init__(self, a, b, name = "obdelník"):
        super().__init__(name)
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    def perimeter(self):
        return 2 * (self.a + self.b)

class Triangle(Shape):
    def __init__(self, a, b, c, name = "trojúhelník"):
        super().__init__(name)
        if a + b <= c or a + c <= b or c + b <= a or a < 0 or b < 0 or c < 0:
            raise ValueError("Neplatné strany trojúhelníku")
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b+ self.c
    def area(self):
        s = self.perimeter() / 2
        return (s*(s - self.a)*(s - self.b)*(s - self.c))**(1/2)
class Square(Rectangle):
    def __init__(self, a, name = "čtverec"):
        super().__init__(a, a,name)
        self.a = a

shapes = [
    Circle(3),
    Rectangle(4, 5),
    Square(4),
    Triangle(3, 4, 5)
]

total_area = 0
max_perim_shape = shapes[0]

print("Popisy tvarů:")
for shape in shapes:
    print(shape.describe())
    total_area += shape.area()
    if shape.perimeter() > max_perim_shape.perimeter():
        max_perim_shape = shape

print(f"\nCelkový obsah všech tvarů: {total_area:.2f}")
print(f"Tvar s největším obvodem: {max_perim_shape.name} ({max_perim_shape.perimeter():.2f})")
    