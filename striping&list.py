Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #striding
>>> a='data science'
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> #positive
>>> a="machine learning"
>>> a[1:6:3]
'ai'
>>> a[1:7:5]
'ae'
>>> a[2:8:6]
'c'
>>> #negative
>>> a="python course"
>>> a[-1:-11:-4]
'eoo'
>>> a[-3:-13:-5]
'rn'
>>> a[-5:-12:-6]
'ot'
>>> a[-2:-9:-1]
'sruoc n'
>>> a[-6:-13:-3]
'coy'
>>> a[-4:-12:-6]
'uh'
>>> a[-2:-3:-6]
's'
>>> #list
>>> a=[3,5.6,'python',9+1j,True,False]
>>> a
[3, 5.6, 'python', (9+1j), True, False]
>>> tyep(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tyep(a)
NameError: name 'tyep' is not defined
>>> type9a0
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    type9a0
NameError: name 'type9a0' is not defined
#list
a=[3,5.9,'python',9+1j,True,False]
a
[3, 5.9, 'python', (9+1j), True, False]
type(a)
<class 'list'>
t=9.0
type(t)
<class 'float'>
t[9.0]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t[9.0]
TypeError: 'float' object is not subscriptable
t=[9.0]
type(t)
<class 'list'>
#append
a=['python','java','c']
a.append('c++')
a
['python', 'java', 'c', 'c++']
#in append it is not possible to add two at a time but it is possible with[]
a.append[["ai","no sal
          
SyntaxError: unterminated string literal (detected at line 1)
a.append[["ai","nosql"]]
          
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.append[["ai","nosql"]]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.append(["ai","nosql"])
          
a
          
['python', 'java', 'c', 'c++', ['ai', 'nosql']]
#instead of that we can use exetend
          
a.extend("vidya","pooja")
          
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.extend("vidya","pooja")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["vidya","pooja"])
          
a
          
['python', 'java', 'c', 'c++', ['ai', 'nosql'], 'vidya', 'pooja']
#insert
          
a.insert(1,"gama")
          
a
          
['python', 'gama', 'java', 'c', 'c++', ['ai', 'nosql'], 'vidya', 'pooja']
#copy()
          
a.cpoy()
          
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.cpoy()
AttributeError: 'list' object has no attribute 'cpoy'
a.copy()
          
['python', 'gama', 'java', 'c', 'c++', ['ai', 'nosql'], 'vidya', 'pooja']
b=a.copy()
          
b
          
['python', 'gama', 'java', 'c', 'c++', ['ai', 'nosql'], 'vidya', 'pooja']
#sort
          
a=["yellow","vidya","ai"]
          
a
          
['yellow', 'vidya', 'ai']
a.sort()
          

a.sort()
          

a
          
['ai', 'vidya', 'yellow']
b=[0,5,6,1,7]
          
b.sort()
          
b
          
[0, 1, 5, 6, 7]
