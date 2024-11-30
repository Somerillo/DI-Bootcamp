class Circle:
    color = "red"
    list_of_circles = []

    def __init__(self, diameter):
        self.diameter = diameter
        Circle.list_of_circles.append(self)

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

circle1 = Circle(2)
print(circle1.color)
circle1.color = 'blue'
print(circle1.color)
c2 = Circle(4)
print(c2.color)
for circle in Circle.list_of_circles:
    print(circle.diameter)