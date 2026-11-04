import math
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return ((self.x**2)+(self.y**2))**(1/2)
    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def scale(self, k):
        return Vector2D(self.x * k, self.y * k)
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    def angle_to(self, other):
        cos_uhlu = self.dot(other) / (self.length() * other.length())
        return math.degrees(math.acos(cos_uhlu))
    def __str__(self):
        return f"({self.x}, {self.y})"


u = Vector2D(3, 4)
v = Vector2D(1, 0)
print(u, u.length())
print(u.add(v))
print(v.angle_to(Vector2D(0, 1))) 