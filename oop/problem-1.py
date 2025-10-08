# """
# write OOp classes to handle the following Scenarios:

# 1. A user can create and view 2D coordinates.
# 2. A user can find out the distance between 2 coordinates
# 3. A user can find the distance of a coordinate from origin
# 4. A user can check if a point lies on a given line
# 5. A user can find the distance between a given 2D point and a given line
# """


class Point:

    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
    
    def __str__(self):
        return "<{} ,{}>".format(self.x_cod,self.y_cod)
    
    def distance_btn_two_points(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod))**0.5
    
    def distance_with_Origin(self):
        return self.distance_btn_two_points(Point(0,0))
    
    


class Line:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return "{}X + {}Y + {}".format(self.A,self.B,self.C)
    
    def point_lies_on_line(line,point):
        if((line.A * point.x_cod + line.B * point.y_cod + line.C) == 0):
            return "point lies on the line"
        else:
            return "point doesnot lies on the line"
    
    def shortest_distance(line,point):
        result = abs((line.A*point.x_cod)+(line.B*point.y_cod)+line.C)/(line.A**2 + line.B**2) **0.5
        return result
    
    def intersection_between_lines(line1,line2):
        x = (line2.C - line1.C)/(line1.A-line2.B)
        y = line1.A * x + line1.C

        return "{},{}".format(x,y)


l1 = Line(2,-1,3)
l2 = Line(-1,1,1)
p1 = Point(1,1)
print(l1)

isLies = l1.point_lies_on_line(p1)

intersectionPoints = l1.intersection_between_lines(l2)

print(intersectionPoints)




# p2 = Point(2,3)

# result = p1.distance_btn_two_points(p2)

# resval = p2.distance_with_Origin()

# print(resval)


