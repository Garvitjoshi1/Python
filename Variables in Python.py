Code
Run on IDE
>>> 2 + 3
5
>>> x = 2
>>> x + 3
5
>>> y = 3
>>> x + y
5
>>> x = 9
>>> x + y
12
>>> x
9
>>> abc
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> x + 10
19
>>> _ + y
22
>>> name = 'youtube'
>>> name
'youtube'
>>> mane + ' rocks'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    mane + ' rocks'
NameError: name 'mane' is not defined
>>> name + ' rocks'
'youtube rocks'
>>> name ' rocks'
SyntaxError: invalid syntax
>>> name [0]
'y'
>>> name [6]
'e'
>>> name [8]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    name [8]
IndexError: string index out of range
>>> name [-1]
'e'
>>> name [-2]
'b'
>>> name [-7]
'y'
>>> name [0:2]
'yo'
>>> name [1:4]
'out'
>>> name [1:]
'outube'
>>> name[:4]
'yout'
>>> [3:10]
SyntaxError: invalid syntax
>>> name [3:10]
'tube'
>>> name [0:3] = 'my'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name [0:3] = 'my'
TypeError: 'str' object does not support item assignment
>>> name[0] = 'R'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    name[0] = 'R'
TypeError: 'str' object does not support item assignment
>>> 'my ' + name[3:]
'my tube'
>>> myname = 'Garvit Joshi'
>>> len(myname)
11
>>> num = 5
>>> id(num)
140731200725776
>>> name = 'garvit'
>>> id(name)
2243898937160
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
140731200725936
>>> id(b)
140731200725936
>>> id(10)
140731200725936
>>> k = 10
>>> id(k)
140731200725936
>>> a = 9
>>> id(a)
140731200725904
>>> id(b)
140731200725936
>>> k = a
>>> id(k)
140731200725904
>>> b = 8
>>> PI = 3.14
>>> PI
3.14
>>> PI = 3.15
>>> type(PI)
<class 'float'>
>>>
