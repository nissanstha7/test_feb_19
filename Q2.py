class Circle:
    PI = 22/7

    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        return Circle.PI * self.radius**2

    def getCircumference(self):
        return 2 * Circle.PI * self.radius

circ_1 = Circle(7)
print(circ_1.getArea())
print(circ_1.getCircumference())
