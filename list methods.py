Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #reverse
>>> a=[2,3,4,5,6,7]
>>> a.reverse()
>>> a
[7, 6, 5, 4, 3, 2]
>>> b=["a","b","c"]
>>> b
['a', 'b', 'c']
>>> b.reverse()
>>> b
['c', 'b', 'a']
>>> #pop
>>> b.pop()
'a'
>>> b.pop(0)
'c'
>>> b,pop(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b,pop(b)
NameError: name 'pop' is not defined. Did you mean: 'pow'?
>>> b.pop(b)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b.pop(b)
TypeError: 'list' object cannot be interpreted as an integer
>>> # in this case we cant pop the elemnt directly for that we have to use remove
>>> b.remove("b")
>>> b
[]
>>> #length
>>> a="hello"
>>> len.a()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    len.a()
AttributeError: 'builtin_function_or_method' object has no attribute 'a'
>>> len(a)
5
>>> b=["hello"]
>>> len(b)
1
>>> #that mean in list we consider one string as 1
>>> #clear=empty list
b.clear()
b
[]
b.append("pooja")
b
['pooja']
#tuple
t=(3,4.9,"python",True,False)
print(t)
(3, 4.9, 'python', True, False)
type(t)
<class 'tuple'>
t.count("python")
1
len(t)
5
t.index(True)
3
