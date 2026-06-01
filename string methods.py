Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#length()
a="sri vidya'
SyntaxError: unterminated string literal (detected at line 1)
a="sri vidya"
len(a)
9
b="sri vidya is python fyllstack trainee at codegnan vijayawada"
len(b)
60
#count
a="johny johny yes papa"
a.count("j)
        
SyntaxError: unterminated string literal (detected at line 1)
a.count("j")
        
2
a.count("johny")
        
2
a.count('y')
        
3
a.count("a,h,n')
        
SyntaxError: unterminated string literal (detected at line 1)
a.count('a,h,n')
        
0
a.count('n')
        
2
2
        
2
#find a string
        
a="vidya'
        
SyntaxError: unterminated string literal (detected at line 1)
a='vidya'
        
a.find('y)
       
SyntaxError: unterminated string literal (detected at line 1)
a.find('y')
       
3
a.find('d')
       
2
a.find('a')
       
4
a.find('v')
       
0
a.find('i')
       
1
a.find(w')
       
SyntaxError: unterminated string literal (detected at line 1)
a.find('w')
       
-1
#escape sequences
       
#\n=new line
       
#\t=new tab
       
#one tab =4 space
       
a="name:sri vidya\nemail:divvisri@gmail.com\nmobile:9063071289"
       
print(a)
       
name:sri vidya
email:divvisri@gmail.com
mobile:9063071289

#replace
       
a='work until you suceed'
       
a.replace("work","much watch")
       
'much watch until you suceed'
a.replace
       
<built-in method replace of str object at 0x00000258F3620B70>
a,replace("must watch until you suceed
          
SyntaxError: unterminated string literal (detected at line 1)
a.replace("must watch until you suceed","wait for my sucees")
          
'work until you suceed'
a.replace("work","wait")
          
'wait until you suceed'
#upper
          
a='sri vidya'
          
a.upper()
          
'SRI VIDYA'
#lower
          
a="codegnan'
          
SyntaxError: unterminated string literal (detected at line 1)
a="codegnan"
          
a.lower()
          
'codegnan'
#if starting must be captial means we use captiaze
          
a="sri vidya"
          
a.capticalize()
          
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.capticalize()
AttributeError: 'str' object has no attribute 'capticalize'. Did you mean: 'capitalize'?
a,capitalize()
          
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a,capitalize()
NameError: name 'capitalize' is not defined
a.capitalize()
          
'Sri vidya'
a.title()
          
'Sri Vidya'
'Sri Vidya'
          
'Sri Vidya'
#rules and conditions
          
a='hello"
          
SyntaxError: unterminated string literal (detected at line 1)
a="hello"
          
a.isupper()
          
False
a.islower()
          
True
a.digit()
          
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.digit()
AttributeError: 'str' object has no attribute 'digit'. Did you mean: 'isdigit'?
a.isdigit()
          
False
b="srividya is a trainee"
          
b.isdigit()
          
False
#digit
          
a=4567899
          
a.isdigit()
          
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
#the string doesn't have digit in it that why we have to add ''to that numbers
          
a='12334'
          
a.isdigit()
          
True
a.alpha()
          
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.alpha()
AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
a="srividya"
          
a.alpjha()
          
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.alpjha()
AttributeError: 'str' object has no attribute 'alpjha'
a.alpha()
          
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.alpha()
AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
a.isalpha()
          
True
a='srividya123'
          
a.isalnum()
          
True
b="srividya@123"
          
b.isalnum()
          
False
#start with
          
c="python"
          
c.startswith("p")
          
True
c.startswith("y)
             
SyntaxError: unterminated string literal (detected at line 1)
c.startswith('y')
             
False
#endswith
             
a.endswith('n')
             
False
c.endswith('n')
             
True
#strip()
             
#if we wnat to remove the space on both sides
             
a="  python  "
             
>>> a.strip()
...              
'python'
>>> #rstrip is a type strip it is useful for removing the right side space
...              
>>> a.rstrip()
...              
'  python'
>>> #lstrip is a type of strip it is used for removing the left side space
...              
>>> a.lstrip()
...              
'python  '
>>> #split
...              
>>> a=
...              
SyntaxError: invalid syntax
>>> a="python c c++ java html
...              
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> a="i am learning python"
...              
>>> a.split()
...              
['i', 'am', 'learning', 'python']
>>> a=
...              
SyntaxError: invalid syntax
>>> a='python'
...              
>>> a.split()
...              
['python']
