Code

>>> x = sqrt(25)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x = sqrt(25)
NameError: name 'sqrt' is not defined
>>> import math
>>> x = math.sqrt(25)
>>> x
5.0
>>> x = math.sqrt(15)
>>> x
3.872983346207417
>>> print(math.floor(2.9))
2
>>> print(math.ceil(2.2))
3
>>> 3 ** 2
9
>>> print(math.pow(3,2))
9.0
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> m.sqrt(25)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    m.sqrt(25)
NameError: name 'm' is not defined
>>> import math as m
>>> math.sqrt(25)
5.0
>>> m.sqrt(25)
5.0
>>> 
=============================== RESTART: Shell ===============================
>>> math.sqrt(25)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
  math.sqrt(25)
NameError: name 'math' is not defined
>>> from math import sqrt, pow
>>> pow(4,5)
1024.0
>>> help('math')
>>>
