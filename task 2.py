Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #task
>>> a="cloud computing"
>>> a[::4]
'cdmi'
>>> a[::3]
'cucpi'
>>> a[::6]
'cci'
>>> a[3:6]
'ud '
>>> a[:9]
'cloud com'
>>> a[7:]
'omputing'
>>> #by using number
>>> a="python course"
>>> a[1:6:1]
'ython'
>>> a[2:9:3]
'tno'
>>> a[5:9:1]
'n co'
>>> #negative intexing
>>> b="python course'
SyntaxError: unterminated string literal (detected at line 1)
>>> b='python course"
SyntaxError: unterminated string literal (detected at line 1)
>>> b=[1:-3:1]
SyntaxError: invalid syntax
>>> b[-1:-3:-1]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b[-1:-3:-1]
NameError: name 'b' is not defined
>>> b="pythone course"
>>> b[-1:-2:-1]
'e'
>>> #tuple
>>> #list
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a.pop()
0
>>> a
[9, 1, 5, 2, 8, 4, 6, 3, 7]
#list
a=[9,1,5,2,8,4,6,3,7]
a.index(1)
1
a.(8,6)
SyntaxError: invalid syntax
a.index(8,6)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.index(8,6)
ValueError: list.index(x): x not in list
a.index([8,6])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.index([8,6])
ValueError: list.index(x): x not in list
