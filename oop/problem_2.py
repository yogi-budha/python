# Rectangle Class
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

class Rectangel:
    def __init__(self,l,w):
        self.length = l
        self.width = w
        self.peremeter = self.peremeter()
        self.area = self.area()
    
    def peremeter(self):
        return 2*(self.width+self.length)
    
    def area(self):
        return self.width*self.length
    
    def display(self):
        print("The length of the rectangle: ", self.length)
        print("The width of the rectangle: ", self.width)
        print("The peremeter of the rectangle: ", self.peremeter)
        print("The area of the rectangle: ", self.area)


r1 = Rectangel(10,3)

r1.display()
        