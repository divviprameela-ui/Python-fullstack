Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
first name="sri'
SyntaxError: unterminated string literal (detected at line 1)
firstname="sri"
print(firstname)
sri
>>> #delete
>>> x=0
>>> print(x)
0
>>> del x
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> #we can use '()' for arrange the multiple vraible with multiple    values
>>> a,b,c=(1,2,3)
>>> pprint(a,b,c)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pprint(a,b,c)
NameError: name 'pprint' is not defined. Did you mean: 'print'? Or did you forget to import 'pprint'?
>>> print(a,b,c)
1 2 3
