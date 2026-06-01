Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data types
#interger
x=9
type(X)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
type(x)
<class 'int'>
#string
v='vidya'
type(v)
<class 'str'>
d="vidya"
type(d)
<class 'str'>
e='''vidya'''
type(e)
<class 'str'>
#complex
a=2+4j
type
<class 'type'>
type(a)
<class 'complex'>
#it accept only j
b=6+7i
SyntaxError: invalid decimal literal
#we can write the iamganiary term
c=4j+5
type(c)
<class 'complex'>
#boolean
i=True
type(i)
<class 'bool'>
j=False
type(j)
<class 'bool'>
#data conversions
int(9)
9
int(9.0)
9
int("sri")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int("sri")
ValueError: invalid literal for int() with base 10: 'sri'
int(9+8j)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(9+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(2)
2.0
float(9.8)
9.8
float("sri')
      
SyntaxError: unterminated string literal (detected at line 1)
float("sri")
      
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float("sri")
ValueError: could not convert string to float: 'sri'
float(True)
      
1.0
float(False)
      
0.0
#string:all will be converted
      
string(9)
      
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    string(9)
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> str(9)
...       
'9'
>>> str(9.8)
...       
'9.8'
>>> str9"vidya")
SyntaxError: unmatched ')'
>>> str("vidya")
'vidya'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(9)
(9+0j)
>>> complex(9.8)
(9.8+0j)
>>> complex("vidya")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    complex("vidya")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #Boolean
>>> bool(9)
True
>>> bool(9.0)
True
>>> bool("vidya")
True
>>> bool(True)
True
>>> bool(False)
False
