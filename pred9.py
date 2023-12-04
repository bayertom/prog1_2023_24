path = 'C:/Tomas/Text/test.txt'

#Open file, v1, difficult
f = None
try:
    f = open(path)

except IOError as e:
    print(e)
finally: 
    if f:   
        f.close()
        

#Open, v2, with
path_file = 'C:/Tomas/Text/test.txt'  
try:      
    with open(path_file) as f:
        pass
except IOError as e:
    print(e)
    
print('x')

#from os import *

#Open, v2
#if path.exists(path_file):
#    with open(path_file) as f:
#        pass
    
print('x')

#Read file by characters
path = 'C:/Tomas/Text/test.txt' 
with open(path, 'r') as f:
    data = f.read()
    data2 = f.read(5)
    print(data)
    
#Read file by line by line
with open(path, 'r') as f:
    data = f.readline()
    data2 = f.readline()
    print(data)
    
#Read file to lines
with open(path, 'r') as f:
    data = f.readlines()
    print(data)
print(data[0][0])

#Write
with open(path, 'a') as f:
    f.write('\nThursday')
f.close()

f = open(path, 'w')
f.write('\nSaturday')
