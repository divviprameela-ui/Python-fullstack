Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variable
a=10
print(a)
10
b=20
print(b)
20
X=100
print(x)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined. Did you mean: 'X'?
print(X
      0
      
SyntaxError: '(' was never closed
print(X)
      
100
z=50
      
print(z)
      
50
#dont start with the number
      
5=7
      
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
#we can use letter first later number
      
a7=10
      
print(a7)
      
10
a0123456789=90
      
print(a0123456789)
      
90
#we can start with set if letters
      
name="srividya"
      
print(name)
      
srividya
place="pedanandipadu"
      
print(place)
      
pedanandipadu
country='india"
      
SyntaxError: unterminated string literal (detected at line 1)
country="india"
      
print(country)
      
india
#special character are not valid
      
@=90
      
SyntaxError: invalid syntax
$=89
      
SyntaxError: invalid syntax
#underscore will be valid
      
_=90
      
print(_)
      
90
#the space will not valid in the variable
      
 x=90
      
SyntaxError: unexpected indent
#instand of space we can use '_'
      
_t=90
      
print(_t)
      
90
#keywords are not valid
      
if=90
      
SyntaxError: invalid syntax
else=00
SyntaxError: invalid syntax
#we can arrage the multiple valus in single line
a=1,2,3,4,5,6
print(a)
(1, 2, 3, 4, 5, 6)
#it is not posiible to arrange the assign the multipli value for  multiple variables
a,b,c=9,8,7
print(a+B+c)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(a+B+c)
NameError: name 'B' is not defined. Did you mean: 'b'?
print(a+b+c)
24
#we can assign the single value for multiple variables
a=b=c=34
print(a,b,c)
34 34 34
#it is possible to arrange multuple variable with multiple values in single line
a=0,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=0:b=9
SyntaxError: invalid syntax
a=0;b=0
print=a,b
print(a,b)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(a,b)
TypeError: 'tuple' object is not callable
a=0;b=9
>>> print(a,"",b)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(a,"",b)
TypeError: 'tuple' object is not callable
>>> print(a+""+b)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print(a+""+b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(a+" "+b)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(a+" "+b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(a,b)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(a,b)
TypeError: 'tuple' object is not callable
