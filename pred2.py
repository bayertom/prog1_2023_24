Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 5
5
>>> type(5)
<class 'int'>
>>> 5.0
5.0
>>> type(5.0)
<class 'float'>
>>> 0.001
0.001
>>> 0.000000001234
1.234e-09
>>> 5+5
10
>>> 3+3
6
>>> from math import *
>>> sqrt(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> True
True
>>> False
False
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'trunc'?
>>> type(True)
<class 'bool'>
>>> cos(1)
0.5403023058681398
>>> acos(cos(1))
0.9999999999999999
>>> acos(cos(1))==1
False
>>> 'Hello world'
'Hello world'
>>> 'Hello world"
  File "<stdin>", line 1
    'Hello world"
    ^
SyntaxError: unterminated string literal (detected at line 1)
>>> "Hello world"
'Hello world'
>>> 'a'
'a'

>>> 'he\nllo'
'he\nllo'
>>> print('he\nllo')
he
llo
>>> print('he\tllo')
he      llo
>>> print('he'tl'lo')
  File "<stdin>", line 1
    print('he'tl'lo')
          ^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('he \'tl \'lo')
he 'tl 'lo
>>> a=1
>>> type(a)
<class 'int'>
>>> a : int = 1
>>> a=7.0
>>> type(a)
<class 'float'>
>>> a=1
>>> b = 2
>>> a/b
0.5
>>> int(a/b)
0
>>> int(12/5)
2
>>> 12/5
2.4
>>> pi
3.141592653589793
>>> a = 5 + 6
>>> type(a)
<class 'int'>
>>> b = 3.0 * 4.0
>>> type(b) = 3.0 * 4.0
  File "<stdin>", line 1
    type(b) = 3.0 * 4.0
    ^^^^^^^
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> type(b) = 3.0 * 4.0
KeyboardInterrupt
>>> b = 3.0 * 4.0
>>> type(b)
<class 'float'>
>>> c = 3 * 4.0
>>> type(c)
<class 'float'>
>>> b = int(3.0 * 4.0)
>>> b = int(3.0 * 4.6)
>>> print(b)
13
>>> type(b)
<class 'int'>
>>> b = 3 * 4.6
>>> print(b)
13.799999999999999
>>> 2/3
0.6666666666666666
>>> 2//3
0
>>> 12//5
2
>>> 3**2
9
>>> 4**1/2
2.0
>>> 9**1/2
4.5
>>> 9**(1/2)
3.0
>>> 9**0.5
3.0
>>> -9**0.5
-3.0
>>> (-9)**(1/2)
(1.8369701987210297e-16+3j)
>>> 12//5
2
>>> 12%5
2
>>> 13%5
3
>>> 13//8
1
>>> 13//5
2
>>> import math
>>> math.sin(1)
0.8414709848078965
>>> from math import *
>>> r = input()
10
>>> r = input('Input radius: ')
Input radius: 10
>>> O = 2 * pi
>>> O = 2 * pi * r
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
>>> type(r)
<class 'str'>
>>> r= int(r)
>>> r= float(r)
>>> O = 2 * pi * r
>>> S = pi * r * r
>>> print('Obvod: ', O)
Obvod:  62.83185307179586
>>> print('Obsah: ', \s)
  File "<stdin>", line 1
    print('Obsah: ', \s)
                       ^
SyntaxError: unexpected character after line continuation character
>>> print('Obsah: ', S)
Obsah:  314.1592653589793
>>>