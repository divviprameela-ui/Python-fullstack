#if codition
#comparision
a=10
if a>1:
    print("true")

a=10
if a<=10:
    print("equal")
    
a=20
b=90
if a<=b:
    print("greater")
    
a=20
b=90
if a>=b:
    print("greater")
    
a=20
b=90
if a<b:
    print("greater")

a=20
b=90
if a>b:
    print("greater")

a=20
b=90
if a!=b:
    print("true")
    
a=int(input("enter the value"))
b=int(input("enter the value"))
if a==b:
    print("equal")
    

a=int(input("enter the value"))
b=int(input("enter the value"))
if a<=b:
    print("true")

a=int(input("enter the value"))
if a==90:
    print("equal")

a=int(input("enter the value"))
b=int(input("enter the value"))
if a>=b:
    print("equal")

a=int(input("enter the value"))
b=int(input("enter the value"))
if a!=b:
    print("equal")

#if condition by suing logical operators

#and

a=10
b=90
if a<b and b>a:
    print("true")

a=2
b=4
if a<b and b<a:
    print("true")

a=5
b=7
if a!=b and b==a:
    print("true")

a=8
b=12
if a<=b or b<=a:
    print("true")

a=5
b=10
if not a<b:
    print("true")

a=5
b=10
if not a>b:
    print("true")

a=5
b=10
if not a<b and b>a:
    print("true")

a=10
b=10
if not a<b or a==b:
    print("true")

a=int(input("a value"))
b=int(input("b value"))
if a<b and b>a:
    print("true")

a=4
b=9
if not a<b or a!=b:
    print("true")
    
#if condition by using identify operators
#is ,isnot
a=2
if type(a) is int:
    print("it is int")

a=int(input("enter the value"))
if type(a) is int:
    print("true")

a=2.9
if type(a) is float:
    print("true")
    
a=2.9
if type(a) is not float:
    print("true")

a=float(input("enter the value"))
if type(a) is float:
    print("true")

a="python"
if type(a) is str:
    print("it is a string")
    
a=input("enter the data")
if type(a) is str:
    print("It is a String")

#if condition using membership operators

a=[10,20,30,40,50]
if 50 in a:
    print("true")

a=[10,20,30,40,50]
if 30 not in a:
    print("true")
    
a=[10,20,30,40,50]
if 60 not in a:
    print("true")

a=int(input("a value"))
if 40 in a:
    print("true")
a=[10,20,30,40,50]
b=int(input("a value"))
if b in a:
    print("true")

a=[10,20,30,40,50]
b=int(input("a value"))
if b in a:
    print("true")


    


    
    




    
    
    
    
    
    
    


    
    

