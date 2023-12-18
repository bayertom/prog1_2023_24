'''#Inheritance, parent class
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
'''

#Abstract method implementation
from abc import ABC, abstractmethod
from math import *

#Base abstract class
class AGO(ABC):
    def __init__(self, color = 0, style = 0):
        self._color = color
        self._style = style
    
    @abstractmethod
    def print(self):
        pass

#Derived class
class Point(AGO):
    counter = 0

    def __init__(self, color = 0, style = 0, x = 0, y = 0):
        #Initialize members of base class
        super().__init__(color, style)

        #Initialize members of derived class
        self._id = Point.counter 
        self._x = x
        self._y = y
        Point.counter = Point.counter + 1
    
    def print(self):
        print('Point:')
        print('C:', self._color, 'W:', self._style)  
        print(self._id, self._x, self._y)

class Line(AGO):
    def __init__(self, color, style, p1, p2):
        #Initialize members of base class
        super().__init__(color, style)

        #Initialize members of derived class
        self._p1 = p1
        self._p2 = p2
    
    def print(self):
        print('Line:')
        self._p1.print()
        self._p2.print()

#Impossible, abstract class 
#go = AGO(1, 2, 3)

#Create two points
p1 = Point(1,2, 15, 15)
p2 = Point(1,3, 27, 35)
p1.print()

#Create line
l1 = Line(1,2, p1, p2)
l1.print()

#Polymorphism, do not use an abstract class
#Polymorphism
go = GO(1, 2, 3)
go.print()
p1 = Point(1, 2, 3, 10, 20)
p1.print()

#Common handling 
G = [go, p1]
#G = [go, p1, 12] # Leads to exception, no print method for int

for g in G:
    g.print()

#Mutable vs Immutable
L1 = [1, 2, 3]
print(id(L1))
L2 = L1
print(id(L2))

#Shallow copy
from copy import deepcopy

print(id(p1))
p2 = p1
print(id(p2))
p1.x = 25
p1.print()
p2.print()

#Deep copy
p3 = deepcopy(p1)
print(id(p3))
p1.x=105   
p3.y=-12
p1.print()
p3.print()

#Derived class
class Point(GO):
    counter = 0

    def __init__(self, color = 0, style = 0, x = 0, y = 0):
        #Initialize members of base class
        super().__init__(color, style)

        #Initialize members of derived class
        self._id = Point.counter 
        self._x = x
        self._y = y
        Point.counter = Point.counter + 1
    
    def print(self):
        print('Point:')
        print('C:', self._color, 'W:', self._style)  
        print(self._id, self._x, self._y)
        
    #Define operators <, >, ==
    def __lt__(self, other):
        return self.__x < other.__x
    
    def __gt__(self, other):
        return self.__x > other.__x

    def __eq__(self, other):
        return (self.__x == other.__x) and (self.__y == other.__y)


#Comparison, operators <, >, ==
print(p1 < p3)
print(p1 > p3)

p4 = deepcopy(p1)
print(p1 == p4)

#Sort a list
L = [5, 4, 9]
L.sort()
print(L)
LS = sorted(L)
print(LS)

#Sort by x, ascendent order
LP = [p1, p2, p3]
LP.sort()
LP[0].print()
LP[2].print()
#LSP = sorted(LP)


