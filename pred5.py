n = 10
fn = 1

#Factorial, V1
while n > 1:
    fn *= n
    n -= 1
print(fn)

#Factorial, V2
n = 5
i = 2
fn = 1
while i <= n:
    fn *= i
    i += 1

print(fn)

#Minimum
M = [2.3, 1.7, 0.9, 4.1, 3.3]
m_min = M[0]

for m in M:
    if m < m_min:
        m_min = m
        
print(m_min)

#Minimum + maximum
M = [2.3, 1.7, 0.9, 4.1, 3.3]
m_min = M[0]
m_max = M[0]
for m in M:
    if m < m_min:
        m_min = m
    elif m > m_max:
        m_max = m
        
print(m_min, m_max)

#List comprehensions
L = [1, 2, 3, 4, 5]
L2 =[2 *l for l in L]
L3 =[0.5 * l for l in L]

#Range
I = range(5)
for i in I:
    print(i)
    
m_min = M[0]
i_min = 0

#Minimum using range
for i in range(len(M)):
    
    if M[i] < m_min:
        m_min = M[i]
        i_min = i

print(m_min, i_min)

#M = [2.3, 4.7, 8.9, 4.1, 3.3]

#Minimum + maximum + indices
m_min = M[0]
m_max = M[0]
i_min = 0
i_max = 0

for i in range(len(M)):
    
    if M[i] < m_min:
        m_min = M[i]
        i_min = i
    
    elif M[i] >m_max:
        m_max = M[i]
        i_max = i

print(m_min, i_min)
print(m_max, i_max)

#Search value
ms = 0.9
found = False
for m in M:
    if ms == m:
        found = True
        break
    
print(found)   