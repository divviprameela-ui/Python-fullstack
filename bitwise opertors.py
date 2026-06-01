Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Bitwise operator
>>> a=3
>>> b=4
>>> a&b
0
>>> a=9
>>> b=8
>>> a&b
8
>>> a=2
>>> b=7
>>> a&b
2
>>> b&a
2
>>> #Bitwise operator
>>> a=6
>>> b=8
>>> a&b
0
>>> bin(6)
'0b110'
>>> #or
>>> a=7
>>> b=7
>>> a|b
7
>>> b|a
7
>>> a=9
>>> b=8
>>> a|b
9
>>> #not
a=7
~a
-8
a=0
~a
-1
#xor
a=0
b=9
a^b
9
a=9
b=67
a^b
74
#leftshift
a=6
a<<2
24
a=9
a<<5
288
#right shift
a=6
a>>2
1
a=57
a>>2
14
bin(57)
'0b111001'
'0b111001'a=5
SyntaxError: invalid syntax
a>>2
14
a<<2
228
a=5
a>>2
1
