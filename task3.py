Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> b=a[0:5]
>>> b
[9, 1, 5, 2, 8]
>>> c=a[5:11]
>>> c
[4, 6, 3, 7, 0]
>>> b.sort()
>>> b.reverse
<built-in method reverse of list object at 0x000001867B71D140>
>>> b.reverse()
>>> b
[9, 8, 5, 2, 1]
>>> c.sort()
>>> c.reverse()
>>> c
[7, 6, 4, 3, 0]
>>> print(f"#{b}{c}")
#[9, 8, 5, 2, 1][7, 6, 4, 3, 0]
>>> print(f"#{c,b}")
#([7, 6, 4, 3, 0], [9, 8, 5, 2, 1])
>>> print("#",(c,b))
# ([7, 6, 4, 3, 0], [9, 8, 5, 2, 1])
>>> print("#",c,d)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print("#",c,d)
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> print("#",(c,b))
# ([7, 6, 4, 3, 0], [9, 8, 5, 2, 1])
>>> d=c+b
>>> d
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
