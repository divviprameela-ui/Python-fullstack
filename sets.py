Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set{}
a={1,2,3,4}
print(a)
{1, 2, 3, 4}
type(a)
<class 'set'>
#add()
a.add(12)
a
{1, 2, 3, 4, 12}
a.add(13,14)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.add(13,14)
TypeError: set.add() takes exactly one argument (2 given)
#issubset()
a={1,2,3,4,5,6,7,8}
b={5,6,7}
b.issubset(a)
True
a.isubset(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.isubset(b)
AttributeError: 'set' object has no attribute 'isubset'. Did you mean: 'issubset'?
a.issubset(b)
False
#issuperset()
a.issuperset(b)
True
b.issuperset(a)
False
#union
a={10,11,12,13,14,1,5}
b={10,12,1,13,1,9,8}
a.union(b)
{1, 5, 8, 9, 10, 11, 12, 13, 14}
b.union(a)
{1, 5, 8, 9, 10, 11, 12, 13, 14}
b.union(b)
{1, 8, 9, 10, 12, 13}
#intersection
a={1,3,5,7,9}
b={1,3,4,6,8,9}
a.intersection(b)
{1, 3, 9}
b.intersection(a)
{1, 3, 9}
b.intersection(b)
{1, 3, 4, 6, 8, 9}
#update
a=[1,2,3,4,5}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
b={1,2,3,4,5}
c={6,7,8,9}
b.update(a)
a
{1, 3, 5, 7, 9}
b
{1, 2, 3, 4, 5, 7, 9}
a.update(b)
a
{1, 2, 3, 4, 5, 7, 9}
a.update(a)
a
{1, 2, 3, 4, 5, 7, 9}
c={1,2,3,4}
c.update(C)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.update(C)
NameError: name 'C' is not defined. Did you mean: 'c'?
NameError: name 'C' is not defined. Did you mean: 'c'?
SyntaxError: invalid syntax
#difference
a={12,1,3,14,15}
b={12,13,14,15,16}
a.difference(b)
{1, 3}
b.difference(a)
{16, 13}
#symmetric differenc
a={1,2,3,45,6}
b={1,2,3,4,5,6,7}
a.symmetric_difference(b)
{4, 5, 7, 45}
b.symmetric_difference(a)
{4, 5, 7, 45}
b.symmetric_difference(b)
set()
#difference_update
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
b.difference_update(a)
b
{7, 8, 9, 10}
a.difference_update(b)
a.difference_update(a)
a
set()
#intersect_update
a={5,6,7,8,9,20}
b={9,10,11,12,13,14}
a.intersection_update(b)
a
{9}
b.intersection_update(a)
b
{9}
#symmertic_difference_update
a={1,2,3,4,5,6}
b={2,3,4,5,6,7,8,9}
a.symmetric_difference_update(b)
a
{1, 7, 8, 9}
b.symmetric_difference_update(a)
b
{1, 2, 3, 4, 5, 6}
#copy and clear
a={12,13,14,15]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a={1,2,4,5,6,7,8}
a.copy()
{1, 2, 4, 5, 6, 7, 8}
b=a.copy()
b
{1, 2, 4, 5, 6, 7, 8}
b.clear()
b
set()
a
{1, 2, 4, 5, 6, 7, 8}
>>> a.clear()
>>> 
>>> a
set()
>>> #pop
>>> a={1,2,3,4,5}
>>> a.pop()
1
>>> a.pop(0)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a.pop(0)
TypeError: set.pop() takes no arguments (1 given)
>>> a.pop()
2
>>> a
{3, 4, 5}
>>> #discard
>>> a={1,2,3,4,5,6]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> a={1,2,3,4,5}
>>> a.discard(3)
>>> a
{1, 2, 4, 5}
>>> #count is in valid in set()
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
>>> #length is valid
>>> len(a)
4
>>> #isdisjoint
>>> a={1,2,3,4}
>>> b={3,4,5,6}
>>> a.isdisjoint(b)
False
>>> #in isdisjoint no repatitions are occured in the set
>>> a={1,2,3,4}
>>> b={5,6,7,8}
>>> a.isdisjoint(b)
True
>>> b.isdisjoint(a)
True
