class RectangleGeometry:
     def __init__(self,length,breadth):
         self.length = length
         self.breadth = breadth

     def getArea(self):
         return self.length * self.breadth

     def getPerimeter(self):
         return 2 * (self.length + self.breadth)


rect = RectangleGeometry(4,5)
print(rect.getArea())
print(rect.getPerimeter())
