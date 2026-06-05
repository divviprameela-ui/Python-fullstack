#if else condition

a=2
b=4
if a<b:
    print("true")
else:
    print("false")

a=2
b=4
if a>b:
    print("true")
else:
    print("false")

a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")
else:
    print("true")

#logical
a=int(input("enter the value"))
b=int(input("enter the value"))
if a<b and b>a:
    print("true")
else:
    print("false")

a=int(input("enter the value"))
b=int(input("enter the value"))
if a<b or b>a:
    print("true")
else:
    print("false")
#identify opertor
a=10
if type(a) is int:
    print("true")
else:
    print("false")

a=int(input("enter the value"))
if type(a) is int:
    print("true")
else:
    print("false")

a=178
if type(a) is int:
    print("true")
else:
    print("false")

a=str(input("enter the data"))
if type(a) is str:
    print("true")
else:
    print("false")

a=str(input("enter the data"))
if type(a) is not str:
    print("true")
else:
    print("false")
#membership

a=[10,20,30]
if 50 in a:
    print("is there")
else:
    print("not there")

a=[10,20,30,40,50]
b=int(input("enter the values"))
if b in a:
    print("is there")
else:
    print("false")


'''a=[10,20,30]
if 50 not in a:
    print("true")
else:
    print("false")'''

a=[10,20,30,40,50]
b=int(input("enter the values"))
if b not in a:
    print("is there")
else:
    print("false")




    


    
    
    
