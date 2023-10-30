#Local and global variables
a = 10
print(a)
b = 7
print(a)
c = 1
if a < 0:
    c = 7
    
def test():
    global d
    d = 10
    print(d)

print(c)
test()
print(d)

#Condition
x = -5   
if x > 0:
    x += 10
else:
    x -= 10

print(x)
    
#Quadratic equation
a = 1 
b = 4
c = 1 

#Discriminant
D = b *b - 4 * a *c

#D > 0
if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    
    print('Two different roots: ',x1, x2)

#D = 0
elif D == 0:
    x1 = -b / (2 * a)
    print('Double root: ', x1)
    
#D < 0
else:
    print('No solution in R ')

#Complex condition
y = 0
if y == 0:
    y = y +10
elif y == 10:
    y = y -10
else:
    y = y * 10
    
    
match y:
    case 0:
        y = y +10
    case 10:
        y = y -10
    case _:
        y = y * 10
        
