Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t = (1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t = (1,1.1,'tryu',[])
t
(1, 1.1, 'tryu', [])
h=(910,20,30,40,50)
h*5
(910, 20, 30, 40, 50, 910, 20, 30, 40, 50, 910, 20, 30, 40, 50, 910, 20, 30, 40, 50, 910, 20, 30, 40, 50)
t = (10,20,30,40,50)
t[1]
20
t[4]
50
t[3]
40
len(t)
5
min(t)
10
sum(t)
150
t.count(10)
1
t.index(10)
0
sorted(h)
[20, 30, 40, 50, 910]
sum(t)
150
sum(h)
1050
t.count(10)
1
t.index(10)
0
t = 12,2,3,4,,5,6,7,7
SyntaxError: invalid syntax
t = 12,2,3,4,5,6,7,7
t
(12, 2, 3, 4, 5, 6, 7, 7)
t.replace(2,3)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t.replace(2,3)
AttributeError: 'tuple' object has no attribute 'replace'
t[2]=4
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
a =  (1,2,3)
x,y,z = a
x
1
y
2
z
3
t = (1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[0]
1
t[2]
3
t[3]
[4, 5, 6]
t[2]=4
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
s = {1,2,3,4}
s
{1, 2, 3, 4}
s= {12,1,1,1,1,1,12,2,2,2,2,2,,82,82,236334,2,3,3,35,2,524,3,63,63
    
SyntaxError: invalid syntax
s= {12,1,1,1,1,1,12,2,2,2,2,2,,82,82,236334,2,3,3,35,2,524,3,63,63}
    
SyntaxError: invalid syntax
s= {12,1,1,1,1,1,12,2,2,2,2,2,82,82,236334,2,3,3,35,2,524,3,63,63}
    
s
    
{1, 2, 3, 35, 12, 524, 236334, 82, 63}
s.add(1)
    
s
    
{1, 2, 3, 35, 12, 524, 236334, 82, 63}
s.add(99)
    
s
    
s
    
{1, 2, 3, 35, 99, 12, 524, 236334, 82, 63}
>>> s.sum()
...     
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s.sum()
AttributeError: 'set' object has no attribute 'sum'
>>> a = {1,2,3,5,6,8,10}
...     
>>> b = {6,7,8,9}
...     
>>> a | b
...     
{1, 2, 3, 5, 6, 7, 8, 9, 10}
>>> a.union(b)
...     
{1, 2, 3, 5, 6, 7, 8, 9, 10}
>>> a.intersection(b)
...     
{8, 6}
>>> a & b
...     
{8, 6}
>>> a
...     
{1, 2, 3, 5, 6, 8, 10}
>>> a <= {1}
...     
False
>>> a >= {1}
...     
True
>>> a >= {6,10,8}
...     
True
>>> b = {8,9,6,7}
...     
>>> b
...     
{8, 9, 6, 7}
