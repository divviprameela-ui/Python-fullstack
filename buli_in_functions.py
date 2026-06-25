#directory:collection of files
#bulit-in-function
#fromkeys()
a="codegnan"
'''print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))
b=dict.fromkeys(a)
print(b)'''

'''c=dict.fromkeys(a,"vidya")
print(c)
c['n']="sri"
print(c)'''

#eval()
'''while True:
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    print(a+b)'''
'''while True:
    a=float(input("enter the value:"))
    b=float(input("enter the value:"))
    print(a+b)'''

'''while True:
    a=(input("enter the value:"))
    b=(input("enter the value:"))
    print(a+b)'''

'''while True:
    a=eval(input("enter the value:"))
    b=eval(input("enter the value:"))
    print(a+b)'''

#zip()->we can combine multiple collections into one collection

'''a=[10,20,30,40,79]
name=["vidya","sri","divvi"]
print(a+name)'''

#if we gave 5 elements and 4 elemnet in other list than it will
#take only 4 elemt according that the element in the list have to be equal upto that only it take
'''c=list(zip(a,name))
print(c)

c=tuple(zip(a,name))
print(c)'''

#enumerate-> we can give counter to the collection
names=["madhu","nirupam","deekshith","guru prasad"]
'''for i in range(len(name)):
    print(i,name[i])'''

'''b=list(enumerate(names,100))
print(b)

b=tuple(enumerate(names,100))
print(b)

b=set(enumerate(names,100))
print(b)

b=dict(enumerate(names,100))
print(b)'''

