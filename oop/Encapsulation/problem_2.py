class Rectangle:

    def __init__(self):
        self.__length = 0
        self.__breath = 0
    
    def set_values(self,length,breath):
        self.__length = length
        self.__breath = breath
    
    def area(self):
        return self.__length * self.__breath
    
    def is_Square(self):
        if(self.__length == self.__breath):
            return True
        else:
            return False

rectangle = Rectangle()

rectangle.set_values(3,3)

areaofreactangle = rectangle.area()

print(rectangle.is_Square())

print(areaofreactangle)