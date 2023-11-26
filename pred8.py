from math import *

#Sin(0.5)

a = 0.1
b = sqrt(a)
#c = 1 / 0
#asin(1.00000000001)

x = 1 + 2 + 3 + 4 / 4 
x = (1 + 2 + 3 + 4) / 5 

#No exceptions
def getPerimeter(r):
    #Good data
    if r >= 0:
        return 2 * pi * r
    #Bad data
    else:
        return -1
    
p = getPerimeter(-5)

if ( p < 0):
    print('Error')
    
    
#Exceptions
def getPerimeter2(r):
    #Good data
    if r >= 0:
        return 2 * pi * r
    #Bad data
    else:
       raise ValueError('Negative radius', r)

#No exceptions
def f (a, b):
    #Error code 1
    if b == 0:
        return -1
    
    #Error code 2
    if a * b < 0:
        return -2
    return sqrt(a / b)

#No exceptions
def f2 (a, b):
    #Guarded block
    try:
        return sqrt(a / b)
    
    except ZeroDivisionError:
        return -1
    
    except ValueError:
         return -2    
         
    except:
        return -3
    
#No exceptions
def f3 (a, b):
    #Guarded block
    try:
        return sqrt(a / b)
    
    except ZeroDivisionError:
        raise ZeroDivisionError('Division by zero', b)
    
    except ValueError:
        raise ValueError('a*b is negative', a*b)   
         
    except:
        raise Exception('Error')

def main():
    #p = getPerimeter2(-5)

    a, b = 5 , -4
    r = f(a,b)
    print(r)
    b = 0
    #a = []
    #r = f2(a,b)
    #print(r)
    
    try:
        r = f3(a,b)
        
    except:
         print(e)
        

main()