""" #Class definition
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def print(self):
        print(self.x, self.y)
        
#Create thing
p1 = Point(1,1)
p2 = Point(10,10)
p3 = Point(-5,4)
p4 = Point()

#Apply method
p1.print()
p2.print()
p3.print() """

""" #Class definition
class Point:
    id = 0
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Point.id = Point.id + 1
    
    def print(self):
        print(Point.id, self.x, self.y)

#Create thing
p1 = Point(1,1)
p1.print()

p2 = Point(10,10)
p2.print()

p3 = Point(-5,4)
p3.print()

p1.print()
p2.print()
p3.print() 
print(p1.x)
"""

#Class definition, getter, setter
class Point:
    counter = 0
    
    def __init__(self, x = 0, y = 0):
        self.id = Point.counter
        self.__x = x
        self.__y = y
        Point.counter = Point.counter + 1
    
    def print(self):
        print(self.id, self.__x, self.__y)
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    

    def setX(self, x):
        self.__x = x
        

p1 = Point(1,1)
p1.print()

p2 = Point(10,10)
p2.print()

p3 = Point(-5,4)
p3.print()

p1.print()
p2.print()
p3.print() 

#print(p1.__x)
x1 = p1.getX()
y1 = p1.getY()

p1.setX(1234)
p1.print()
