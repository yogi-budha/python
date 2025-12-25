from abc import ABC, abstractmethod

class Polygon:
    @abstractmethod
    def getDimension(self):
        pass

    @abstractmethod
    def area(self):
        pass 

class Rectangle(Polygon):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def getDimension(self):
        print(f"Length:{self.length},Breadth:{self.breadth}")
    
    def area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def getDimension(self):
        print(f"Base:{self.base},Height:{self.height}")

    def area(self):
        return 0.5 * self.base * self.height
    
rectangle = Rectangle(5,10)
rectangle.getDimension()
print("Area of Rectangle :" , rectangle.area())
triangle = Triangle(5,10)
triangle.getDimension()
print("Area of Triangle :" , triangle.area())