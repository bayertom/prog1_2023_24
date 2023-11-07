#Factorial, return one value
def fact(n:int)->int:
    fn = 1
    while n > 1:
        fn *= n
        n -= 1
    return fn

def add_subtract_multiply(a, b):
    #Add, subtract, multiply a and b, V1
    a_ab = a + b
    s_ab = a - b
    m_ab = a * b
    
    return a_ab, s_ab, m_ab

def add_subtract_multiply2(a, b):
    #Add, subtract, multiply a and b, V2
    return a + b, a - b, a * b

def add_subtract_multiply3(a, b):
    #Add, subtract, multiply a and b, V3
    a_ab = a + b
    s_ab = a - b
    m_ab = a * b
    
    print(a_ab, s_ab, m_ab)

#Call a function 1
f = fact(10)
print(f)

#Call a function 2
a = 2 
b = 3

res1, res2, res3 = add_subtract_multiply2(a, b)
print(res1, res2, res3)

#Call a function 3
add_subtract_multiply3(a, b)

#Main function
def main(args):
    add_subtract_multiply3(a, b)
    
#Immutable object
def f1(x):
    print(id(x))
    x = x + 10
    print(x)
    print(id(x))

#Mutable object
def f2(L):
    print(id(L))
    L[0] = 25
    print(L)
    print(id(L))

#Immutable object   
a = 25;
print(id(a))
f1(a)
print(a)
print(id(a))

#Mutable object
L = [1, 2, 3, 4, 5]
print(id(L))
f2(L)
print(L)
print(id(L))

#Default values of parameters
def dist(x1, y1, x2 = 0, y2 = 0):
    dx = x2 - x1
    dy = y2 - y1
    return (dx * dx + dy * dy) **0.5

x1 = 0
y1 = 0
x2 = 10
y2 = 10

d = dist(x1, y1, x2, y2)
print(d)

d = dist(x1, y1, 20)
print(d)

#Combination, pass a function (fact)
def comb(n, k, f):
    num = f(n)
    denom = f(n-k) * f(k)
    return num / denom

#Combination
def comb2(n, k):
    num = fact(n)
    denom = fact(n-k) * fact(k)
    return num / denom

#Combinations
n = 5
k = 3

res = comb(n, k, fact)
print(res)

res = comb2(n, k)
print(res)

#List comprehensions
def sum(*L):
    lsum = 0
    for l in L:
        lsum += l
    return lsum 

L = [1, 2, 3, 4, 5]
res = sum(10, 2, 0, 30)
print(res)

