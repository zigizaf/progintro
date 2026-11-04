class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        if self.width == self.height:
            return True
        return False

    def scale(self, factor):
        self.width *= factor
        self.height *= factor

    def describe(self):
       return f"Výška obdélníku je {self.height}, šířka obdélníku je {self.width}. Tento obdélník má obsah {self.area()}."

rectangles = [
    Rectangle(3, 4),
    Rectangle(5, 5),
    Rectangle(2.5, 8),
    Rectangle(6, 2)
]
print("Seznam obdélníků:")
for rect in rectangles:
    print(rect.describe())

nejvetsi = rectangles[0]

for rect in rectangles:
    if rect.area() > nejvetsi.area():
        nejvetsi = rect

print(nejvetsi.describe())    
