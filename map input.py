#list using map
'''a=list(map(int, input("enter the number:").split(",")))
print(a)'''

#tuple using map

'''a=tuple(map(int, input("enter the number:").split(",")))
print(a)'''

#eval using map

'''a=tuple(map(eval, input("enter the number:").split(",")))
print(a)'''

#str

'''a=tuple(map(str, input("enter the number:").split(",")))
print(a)'''

#dict
'''a=input("enter the data:")
b=dict(i.split(":") for i in a.split(","))
print(b)'''

'''#ASCII
#chr-we must give only number
print(chr(56))
print(chr(89))'''
#ord()-we must give only letters
'''print(ord("a"))
print(ord("b"))'''


#task: to print A to Z
'''for i in range(65,91):
    print(chr(i),end=" ")'''
    
#task 2:to print a to z

'''for i in range(97,123):
    print(chr(i),end=" ")'''


#ascii fo name
'''a="srividya"
for i in a:
    print(i,ord(i))'''

'''a=map(str,input("enter the data:").split(" "))
for i in a:
    print(i,ord(i))'''

