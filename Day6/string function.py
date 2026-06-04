Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s ='python programming'
s
'python programming'
min(2)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    min(2)
TypeError: 'int' object is not iterable
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
char(65)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    char(65)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(65)
'A'
min(s)
' '
max(s)
'y'
ord("A")
65
chr(35)
'#'
ord(35)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ord(35)
TypeError: ord() expected string of length 1, but int found
chr(37)
'%'
s.upper()
'PYTHON PROGRAMMING'
s.capitalize()
'Python programming'
s.swapcase()
'PYTHON PROGRAMMING'
s.centre(38,'*')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.centre(38,'*')
AttributeError: 'str' object has no attribute 'centre'. Did you mean: 'center'?
s.center(38,'*')
'**********python programming**********'
s.center(28,'-')
'-----python programming-----'
s.ljust(28,'#')
'python programming##########'
s.rjust(28,'#)
        
SyntaxError: unterminated string literal (detected at line 1)
s.rjust(28,'#')
        
'##########python programming'
s = ('vamsi')
        
s.zfill(10)
        
'00000vamsi'
s.zfill(25)
        
'00000000000000000000vamsi'
s.center(99,'=')
        
'===============================================vamsi==============================================='
s = 'python programming'
        
s
        
'python programming'
s.find('g)
       
SyntaxError: unterminated string literal (detected at line 1)
s.find('g')
       
10
s.rfind('o')
       
9
s.index('o')
       
4
>>> count('p)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> count('p')
...       
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    count('p')
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> s.count('p')
...       
2
>>> s.replace('python','java')
...       
'java programming'
>>> s.replace(s[0],'s')
...       
'sython srogramming'
>>> s 'java,python,javascript,c,c++'
...       
SyntaxError: invalid syntax
>>> s= 'java,python,javascript,c,c++'
...       
>>> s'
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> s
...       
'java,python,javascript,c,c++'
>>> s.split(',')
...       
['java', 'python', 'javascript', 'c', 'c++']
>>> s.split(',',2)
...       
['java', 'python', 'javascript,c,c++']
>>> s.rsplit(',',2)
...       
['java,python,javascript', 'c', 'c++']
>>> t = 'hello 
KeyboardInterrupt
