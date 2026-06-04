Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dect
>>> s={"name":"vidya","age":19}
>>> print(s)
{'name': 'vidya', 'age': 19}
>>> type(s)
<class 'dict'>
>>> s.keys()
dict_keys(['name', 'age'])
>>> s.values()
dict_values(['vidya', 19])
>>> s.items()
dict_items([('name', 'vidya'), ('age', 19)])
>>> #update
>>> a={"college":"MLEW","Branch":"AI&DS"}
>>> a.update("year":2)
SyntaxError: invalid syntax
>>> a
{'college': 'MLEW', 'Branch': 'AI&DS'}
>>> a.({"year":2})
SyntaxError: invalid syntax
>>> a
{'college': 'MLEW', 'Branch': 'AI&DS'}
>>> a.update({"year":2})
>>> a
{'college': 'MLEW', 'Branch': 'AI&DS', 'year': 2}
>>> #setdegault
>>> #setdefault
>>> a.setdefault('batch',3)
3
>>> a
{'college': 'MLEW', 'Branch': 'AI&DS', 'year': 2, 'batch': 3}
>>> #get()
>>> b={'father':'suresh',"mother":"latha"}
>>> b.get("father")
'suresh'
>>> b.["mother']
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> b.['mother"
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> b.["mother"]
...    
SyntaxError: invalid syntax
b["mother"]
   
'latha'
#pop
   
c={"teacher Name":Rosaiah,"subject":"hindi","experince":15}
   
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c={"teacher Name":Rosaiah,"subject":"hindi","experince":15}
NameError: name 'Rosaiah' is not defined
c={"teacher Name":"Rosaiah,""subject":"hindi","experince":15}

SyntaxError: invalid syntax
SyntaxError: invalid syntaxc={"teacher Name":Rosaiah,"subject":"hindi","experince":15}
c={"teacher Name":"Rosaiah","subject":"hindi","experince":15}
   
SyntaxError: invalid syntax


c={"teacher":"rosaiah","subject":"hindi","experince":15}
   
c.pop("experince")
   
15
c
   
{'teacher': 'rosaiah', 'subject': 'hindi'}
c.popitems()
   
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    c.popitems()
AttributeError: 'dict' object has no attribute 'popitems'. Did you mean: 'popitem'?
c.popitem()
   
('subject', 'hindi')
c
   
{'teacher': 'rosaiah'}
#copy()
   
d={"date":4,"month":6,"year":10}
   
d.copy()
   
{'date': 4, 'month': 6, 'year': 10}
e
   
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    e
NameError: name 'e' is not defined
e=d.copy()
   
e
   
{'date': 4, 'month': 6, 'year': 10}
d
   
{'date': 4, 'month': 6, 'year': 10}
d.clear()
   
e
   
{'date': 4, 'month': 6, 'year': 10}
e.clear()
   
e
   
{}
d
   
{}
#adding many values at a time
   
f={"id_no":[10,11,12],"names":["vidya","hirshi","bhavya"]}
   
f
   
{'id_no': [10, 11, 12], 'names': ['vidya', 'hirshi', 'bhavya']}
type(f)
   
<class 'dict'>
f.values()
   
dict_values([[10, 11, 12], ['vidya', 'hirshi', 'bhavya']])
f.items()
   
dict_items([('id_no', [10, 11, 12]), ('names', ['vidya', 'hirshi', 'bhavya'])])
f.keys()
   
dict_keys(['id_no', 'names'])
