Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> f=5.5
>>> f
5.5
>>> type(f)
<class 'float'>
>>> int(f)
5
>>> complex(f)
(5.5+0j)
>>> str(f)
'5.5'
>>> bool(f)
True
>>> str='ramsh'
>>> int(str)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(str)
ValueError: invalid literal for int() with base 10: 'ramsh'
>>> t=(1,2,3,5)
>>> t
(1, 2, 3, 5)
>>> str(t)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    str(t)
TypeError: 'str' object is not callable
>>> list(t)
[1, 2, 3, 5]
>>> bool=True
>>> int(bool)
1
