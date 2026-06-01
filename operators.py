Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arthematic
a=9
b=9
print(a=b)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(a=b)
TypeError: print() got an unexpected keyword argument 'a'
print(a+b)
18
print(a-b)
0
print(a*b)
81
print(a**b)
387420489
print(a/b)
1.0
primt(a//b)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    primt(a//b)
NameError: name 'primt' is not defined. Did you mean: 'print'?
print(a//b)
1
#assignment operators
a=8
b=9
b+=a
b
17
b-=a
b
9
b*=a
b
72
b/=a
b
9.0
b//=a
b
1.0
b%=a
b
1.0
#comparision
a=6
4
4
b=6
a<b
False
b<a
False
a>b
False
b>a
False
a==b
True
a!=b
False
a=9
b=6
a>b
True
b>a
False
a<b
False
b<a
True
b==a
False

b!=a
True
#logical
a=9
b=10
a<b and b>a
True
b<a and a>b
False
a==b and a
False
a!=b and a==b
False
a>b and b>a
False
b>a and a>b
False
a>b or b>a
True
a>b or b<a
False
a!=b or b!=a
True
a==b or b==a
False
not Flase
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    not Flase
NameError: name 'Flase' is not defined. Did you mean: 'False'?
not False
True
not True
False
not a<b
False
#identify operators
a=6
if type(a) is int:
...     print(" it is a integer')
...           
SyntaxError: unterminated string literal (detected at line 2)
>>> print("it is interger")
...           
it is interger
>>> if type(a) is str:
... 
... # membership
...           a=1,2,3,4,5,6,7,8
... if 4 in a:
...           
SyntaxError: invalid syntax
>>> c=1,2,3,4,5,6
...           
>>> if 4 in a:
...           print("it is there ")
... 
...           
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    if 4 in a:
TypeError: argument of type 'int' is not a container or iterable
>>> if 4 in a:
...           print(4)
... 
...           
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    if 4 in a:
TypeError: argument of type 'int' is not a container or iterable
>>> z=1,2,3,4
...           
>>> if 2 in z
...           
SyntaxError: expected ':'
>>> if 2 in z:
...           print(2)
... 
...           
2
