Code
-->> Run in Python IDE
>>> tup = (21,36,14,25)
>>> tup
(21, 36, 14, 25)
>>> tup[1]
36
>>> tup[1] = 33
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup[1] = 33
TypeError: 'tuple' object does not support item assignment
>>> s = {22,25,14,21,5}
>>> s
{5, 14, 21, 22, 25}
>>> s = {25,14,98,63,75,98}
>>> s
{98, 75, 14, 25, 63}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>>
