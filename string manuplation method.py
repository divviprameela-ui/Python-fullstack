Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#join()
a='python','java','c'
"".join(a)
'pythonjavac'
" ".join(a)
'python java c'
b=1234567
",".join(A)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ",".join(A)
NameError: name 'A' is not defined. Did you mean: 'a'?
",".join(a)
'python,java,c'
#formatting
c=10
d=20
print("the output is ",a)
the output is  ('python', 'java', 'c')
print("the output is ",c+d)
the output is  30
e="malineni"
print("i am from malineni",e)
i am from malineni malineni
#concantenation
a='sri'
b='vidya'
print(a+b)
srividya
print(a+' '+b)
sri vidya
print((a+" "+b).title())
Sri Vidya
print(a.title)
<built-in method title of str object at 0x00000190B8B1AAC0>
print(a.title())
Sri
c=a.title()
print(c)
Sri
d=b.title()
print(d)
Vidya
print(c+d)
SriVidya
print(c+" "+d)
Sri Vidya
#format method
a='motu
SyntaxError: unterminated string literal (detected at line 1)
a="motu"
b='patlu"
SyntaxError: unterminated string literal (detected at line 1)
b='patlu'
print("hello {} {}".format())
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print("hello {} {}".format())
IndexError: Replacement index 0 out of range for positional args tuple
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello{}".format(a,b))
hello motu hellopatlu
>>> print("hello {}+"\n"+hello {}".format(a,b))
SyntaxError: unexpected character after line continuation character
>>> print("hello {} hello {}".format(a+'\n'+b))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print("hello {} hello {}".format(a+'\n'+b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("hello { }+\n+hello { }".format(a,b))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print("hello { }+\n+hello { }".format(a,b))
KeyError: ' '
>>> print("hello { }\n hello { }".format(a,b))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print("hello { }\n hello { }".format(a,b))
KeyError: ' '
>>> print("hello {}\nhello {}".format(a,b))
hello motu
hello patlu
>>> #f string
>>> a="micky"
>>> b="mouse"
>>> print(f"hello {a} {b}")
hello micky mouse
>>> print(f"hello {a} {b}")
hello micky mouse
>>> print(f"hello {a} hello{b}")
hello micky hellomouse
>>> print(f"hello {a} \nhello{b}")
hello micky 
hellomouse
>>> print(f"hello {a} \nhello {b}")
hello micky 
hello mouse
