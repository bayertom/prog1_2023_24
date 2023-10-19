#Create list
L=[]
L.append(1)
L
L.append(2)
L.append(3)
L.append(4)
L.append(5)
L

L=[1, 2, 3, 4, 5, 6]
L

#List properties
print(L)
len(L)
n = len(L)
n
type(n)

#List, indices
L[0]
L[2]
L[5]
L[-1]
L[-2]
L[-1]==L[5]
True
L[-6]
L[-7]
L[6]

#List, slices
L[0:2]
L[0:3]
L2 = L[0:3]
L2

L.append(20)
L[1:5]
L[1]=47
L2 = L[0:3]
L2
L[:5]
L[0:]
L[2:]

L[0:5:1]
L[0:5:2]

#List, other operations
5 in L
68 in L
L
L2
L3 = L + L2
L3
L[1]='bye'
L
[1, 'bye', 3, 4, 5, 6, 20]
L[1]=L2
L

#String, slices
S='Hello world'
S[0]
'H'
len(S)
S[11]
S[10]
S[4:]
S[3:]
S[:8]
S[-2]
S[0:10:2]
S[0:10:3]
S[::3]
S[::1]
S[::-1]
S[::-2]

#Stack, properties
S=[]
S.append('Monday')
S.append('Tuesday')
S.append('Wednesday')
S.append('Thursday')
S

item = S.pop()
item
S
item = S.pop()
item
S
item = S.pop()
S
item = S.pop()
item
S
item = S.pop()


#Queue, properties
Q=[]
Q.append('Monday')
Q.append('Tuesday')
Q.append('Wednesday')
Q.append('Thursday')
Q
item = Q.pop(0)
item
Q
item = Q.pop(0)
item
Q
item = Q.pop(0)
item
Q
item = Q.pop(0)
item
Q
item = Q.pop(0)

#Priority queue
import queue
PQ = queue.PriorityQueue()
PQ.put((1, 'Monday'))
PQ
PQ.put((3, 'Tuesday'))
PQ.put((0, 'Wednesday'))
item = PQ.get()
item
item = PQ.get()
item
item = PQ.get()
item

#Tuple
N=(1,2,3,4,5,6)
N[0]
N[5]
N[0]=1


#Set
S={'Jan','Lukas','Jana','Petra', 'Marketa'}
S
S[0]
S1 = S
S1
S2 = {'Lukas', 'Jan','Teodor'}
S2
len(S2)
3
'Jan' in S2
'Jan' in S1
'Jana' in S1
'Jana' in S2

S2.insert('Olivie')
S2

#Set, boolean operations
U = S1.union(S2)
U
S1
S2
U2 = S2.union(S1)
U2
I = S1.intersection(S2)
I
D1 = S1.difference(S2)
D1
D2 = S2.difference(S1)
D2


#Dictionary
D={1234:['Jan', 'Novak'], 4567:['Eliska','Novotna']}
D
len(D)
2
1234 in D
True
D.get(1234)
