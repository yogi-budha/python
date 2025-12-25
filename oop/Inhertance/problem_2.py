class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y



class Location():
    def __init__(self,location,destination):
        self.location = location
        self.destination = destination
    
    def print_reflection_on_x_axis(self):
        reflected_x = self.destination.x
        reflected_y = -self.destination.y
        print(f"Reflection on destination X axis: ({reflected_x},{reflected_y})")

location = Point(3,4)
destination = Point(5,2)

place = Location(location,destination)
place.print_reflection_on_x_axis()