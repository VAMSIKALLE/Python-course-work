Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = '    hello     world    '
s
'    hello     world    '
s.strip()
'hello     world'
s.replace(" ","")
'helloworld'
s.lstrip()
'hello     world    '
s.rstrip()
'    hello     world'
s = "strings.py"
s
'strings.py'
s.startswith("str")
True
s.startswith("s")
True
s.startswith("tri")
False
s.endswith('Py')
False
s.endswith('py')
True
"wertyui".islower()
True
'ASDFGHJU234567YGCSQ@#$%^yh'.isupper()
False
'Vertyu'.istitle()
True
'sdfghytrf'.isalpha()
True
'werty12345@'.isalpha()
False
'wertyuio'.isalnum()
True
l = []
l = list()
type(l)
<class 'list'>
l = [1,2,3,4]
m = [7,5,4,3]
l+m
[1, 2, 3, 4, 7, 5, 4, 3]
l*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l = [10,20,30,40,50]
l[4]
50
l[1:4]
[20, 30, 40]
l[::-1]
[50, 40, 30, 20, 10]
l[-3::-1]
[30, 20, 10]
l
[10, 20, 30, 40, 50]
20 in l
True
l[70]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    l[70]
IndexError: list index out of range
l[20]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l[20]
IndexError: list index out of range
l[1]
20
l[4]=400
l
[10, 20, 30, 40, 400]
l.append(120)
l
[10, 20, 30, 40, 400, 120]
l.append(78)
l
[10, 20, 30, 40, 400, 120, 78]
l
[10, 20, 30, 40, 400, 120, 78]
l.extend([80,90,110])
l
[10, 20, 30, 40, 400, 120, 78, 80, 90, 110]
l.intert(4,6000)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    l.intert(4,6000)
AttributeError: 'list' object has no attribute 'intert'. Did you mean: 'insert'?
l.insert(4,6000)
l
[10, 20, 30, 40, 6000, 400, 120, 78, 80, 90, 110]
l.pop()
110
l.pop(3)
40
l.remove(400)
l
[10, 20, 30, 6000, 120, 78, 80, 90]
del l[1]
l
[10, 30, 6000, 120, 78, 80, 90]
>>> del l[2]
>>> l
[10, 30, 120, 78, 80, 90]
>>> l.clear()
>>> l
[]
>>> id(1)
140725420147832
>>> l =[10, 20, 30, 40, 400, 120]
... l
SyntaxError: multiple statements found while compiling a single statement
>>> l =[10, 20, 30, 40, 400, 120]
>>> l
[10, 20, 30, 40, 400, 120]
>>> l.sorted()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    l.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> sorted(l)
[10, 20, 30, 40, 120, 400]
>>> l.sort()
>>> l
[10, 20, 30, 40, 120, 400]
>>> l.reverse()
>>> l
[400, 120, 40, 30, 20, 10]
>>> max(l)
400
>>> min(l)
10
>>> l.index(120)
1
>>> l.count(30)
1
>>> sum(l)
620
>>> len(l)
6
