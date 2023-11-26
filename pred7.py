#Recursion
def f(n):
    print("C(" + str(n)+")")
    #Non-recursive solution
    if (n == 1):
        print("D");
        
    #Recursive approach
    else:
        print("f(" + str(n-1) + ")")
        f(n - 1)
    print("E(" + str(n) + ")")
  
#Recursive call  
#f(1)
f(4)

#Factorial, return one value
def fact(n:int)->int:
    fn = 1
    while n > 1:
        fn *= n
        n -= 1
    return fn

 #Recursive approach
def f(n):
    #Non-recursive solution
    if n==1:
        return 1  
    
    #Recursion
    else:
        return n * f(n-1) 
    
res = f(5)
print(res)

#Fibonacci, recursive approach
def fib(n):
    if n > 1:
        return fib(n-1)+fib(n-2)
    else:
        return 1
    
res = fib(40)
print(res)

#Find maximum
def maximum(X, l, r):
    #Non-recursive solution
    if r - l <=1:
        #if X[l] > X[r]:
        #    return X[l]
        #else:
        #    return X[r]
        return max(X[l], X[r])
    
    #Recursion
    else:
        m = (l + r)//2
        
        maxl = maximum(X, l, m)
        
        maxr = maximum(X, m+1, r)
        
        return max(maxl, maxr)

