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
    
    def setY(self, y):
        self.__y = y 
          
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
        
    @x.setter
    def x(self, x):
        self.__x = x
    
    @y.setter
    def y(self, y):
        self.__y = y
                
#Create objects, print amount of objects
p1 = Point(10, 15)
p2 = Point(37, 20)
p3 = Point(12, 14)

#Print properties
p1.print()
p2.print()
p3.print()

#Working with getters
x1 = p1.getX()
y1 = p1.getY()

#Working with setters
p1.setX(13)
p1.setY(26)
p1.print()

#Property, get coordinates
x1 = p1.x
y1 = p1.y
p1.x = 107

#Different algorithms
class Algorithms:
    
    def getMidPoint(self, p1, p2):
        xm = 0.5*(p1.x + p2.x)
        ym = 0.5*(p1.y + p2.y)
        return xm, ym
    
    def getMidPoint2(self, p1, p2):
        xm, ym = self.getMidPoint(p1, p2)
        return Point(xm, ym)
    
    def getMidPoint3(self, l):
        return self.getMidPoint2(l.s, l.e)


#Pass object
a = Algorithms()
xm, ym = a.getMidPoint(p1, p2)

#Pass/return object
print(xm, ym)
M = a.getMidPoint2(p1, p2)
M.print()

#Composition, aggregation
class Line:
    
    def __init__(self, s, e):
        self.s = s
        self.e = e
        
    def print(self):
        print('Line: ')
        self.s.print()
        self.e.print()   
        

l = Line(p1, p2)
l.print()
M2 = a.getMidPoint3(l)
M2.print()

#Inheritance, parent class
class GO:
    def __init__(self, color, style):
        self.color = color
        self.style = style
        
    def print(self):
        print ('GO', self.color, self.style)
        
#Inheritance, derived class
class Point(GO):
    counter = 0
    
    def __init__(self, color, style, x = 0, y = 0):
        super().__init__(color, style)
        self.id = Point.counter
        self.__x = x
        self.__y = y
        Point.counter = Point.counter + 1
    
    def print(self):
        print(self.id, self.__x, self.__y)
        
    
#Inheritance, derived class
class LineG(GO):
    def __init__(self, color, style, p1, p2):
        super().__init__(color, style)
        self.p1 = p1
        self.p2 = p2
        
    def print(self):
        super().print()
        self.p1.print()
        self.p2.print()

#Create objects, print amount of objects
p1 = Point(1, 2, 10, 15)
p2 = Point(2, 3, 37, 20)
p3 = Point(1, 3, 12, 14)      
go = GO(1,2)
l1 = LineG(2, 3, p1, p2)
l1.print()
    