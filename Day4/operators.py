Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a=10

a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a%b
0
a**2
400
a**b
10240000000000
-------------------------------------------------------------------------------------------------------------------
SyntaxError: invalid syntax
a>b
True
a<b
False
a<=b
False
a>=b
True
a==b
False
a!=b
True
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
SyntaxError: invalid syntax
y=5
y+=10
y
15
y-=5
y

y
10
y*=4
y
40
y//=10
y
4
y**=2
y
16
y+=4
y
y
20
y%=2
y
0
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SyntaxError: invalid syntax
a and b
10
not a>b
False
a%22==0 or b%20==0 or a<b
False
----------------------------------------------------------------------------------------------------------------------
SyntaxError: invalid syntax
a= 'python programming'
a
'python programming'
'y' in a
True
'g' in a
True
'z' not in a
True
'r' not in a'
SyntaxError: unterminated string literal (detected at line 1)
l = ['java','python','c','c++','mysql','HTML']
l
['java', 'python', 'c', 'c++', 'mysql', 'HTML']
'my sql' in l
False
'mysql' in l
True
d = {'egg':8,'oil':120,'sugar'=40,'salt':30}
SyntaxError: ':' expected after dictionary key
d = {'egg':8,'oil':120,'sugar':40,'salt':30}
d
{'egg': 8, 'oil': 120, 'sugar': 40, 'salt': 30}
'chilli' in d
False
---------------------------------------------------------------------------------------------------------------------------------------------------
SyntaxError: invalid syntax
l = [1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
l is m
False
n is m
True
8  & 14
8
8 &  7
0
8 | 7
15
10^11
1
~12
-13
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 8>>2
2
>>> 15>>2
3
>>> 16<<1
32
>>> 4<<2
16
>>> a=12
>>> b=12.34
>>> c='python'
>>> print('a=',a,'b=',b,'c=',c)
a= 12 b= 12.34 c= python
>>> print('a=',a,'b=',b,'c=',sep='')
a=12b=12.34c=
>>> print('a=',a,'b=',b,'c=',c,sep='')
a=12b=12.34c=python
>>> print('a = {2} b={0} c={1}',format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print('a = {2} b={0} c={1}',format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
>>> print('a = {} b={} c={}',format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print('a = {} b={} c={}',format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
>>> print('a = {} b={} c={}'.format(a,b,c))
a = 12 b=12.34 c=python
>>> print('a = {2} b={0} c={1}'.format(a,b,c))
a = python b=12 c=12.34
>>> KeyboardInterrupt
>>> print('a = {2} b={0} c={1}',format(a,b,c))
