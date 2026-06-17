# *argument-> *is used to unpack the elements

'''a=[2,3,4,5,6,7]
print(a)
print(type(a))
print(*a)'''

'''a=(2,3,4,5)
print(a)
print(type(a))
print(*a)'''

'''a={2,3,4,5}
print(a)
print(type(a))
print(*a)'''

'''a={'name':"pooja",'branch':"AI&DS"}
print(a)
print(type(a))
print(*a)'''

'''a='codegnan'
print(a)
print(type(a))
print(*a)'''

#it shows error ,because one variable will store only one value
'''a,b,c=2,3,4,6,7
print(a)
print(type(a))
print(*a)'''

#if we keep * it will print more value accept the assigned values to the remanining variables

'''a,*b,c=2,3,4,5,6
print(a)
print(*b)
print(c)'''

#variable length arguments are automativally stores in tuple and we use start arguments

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5)
b=[2,3,4]
check(*b)
d={2,3,45}
check(*d)
e={"year":2026,"month":"june"}
check(*e)'''

'''def check1(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (float,int):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,7)
check1(3,4,5.6,7.8)
check1(3,4,5,"ppja")'''

#rail way ticket application
while True:
    def ticket(gender,age,cost):
        gender=input("enter the gender:")
        age=int(input("enter the age:"))
        cost=1000
        if gender=='f':
                if age>=60:
                  print("senior citizen")
                  price=cost-50/100*cost
                  print("ticket price is:",price)
                else:
                    print("normal citizen")
                    price=cost-30/100*cost
                    print("ticket price is:",price)

        else:
            if age>=60:
                print("senior citizen")
                price=cost-30/100*cost
                print("ticket price is:",price)

            else:
                print("normal citizen")
                price=cost
                print("ticket price is:",price)
    ticket('gender','age','cost')            

            
