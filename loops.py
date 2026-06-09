#loops
#for loop
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''
#if we want to print it in single line
'''a=[10,20,30,40,50]
for i in a:
    print(i,end="")'''
#if we want space between them
'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''
#if we want ','between them

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")'''

#print the tyoe of 'i' and a

'''a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(i))
    print(type(a))'''
#incase type of i and a have to come the bootom after the number
'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(i))
print(type(a))'''

#by using tuple
'''a=(10,20,30,40,50)
for i in a:
    print(i)
print(type(i))
print(type(a))'''

#by using set{}
'''a={10,20,30,40,50}
for i in a:
    print(i)
print(type(i))
print(type(a))'''

#by using disct
'''a={"name":"vidya","year":2026,"month":6}
for i in a:
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
print(type(i))
print(type(a))'''

#to print only keys()

'''a={"name":"vidya","year":2026,"month":6}
for i in a.keys():
    print(i)
print(type(i))
print(type(a))'''
#to print only values()
'''a={"name":"vidya","year":2026,"month":6}
for i in a.values():
    print(i)
    print(type(i))
    print(type(a))'''

#to print items()

'''a={"name":"vidya","year":2026,"month":6}
for i in a.items():
    print(i)
    print(type(i))
    print(type(a))'''
#all data types
'''a=[1,2.6,"vidya",8+7j,True,False]
for i in a:
    print(i)
    print(type(i))
    print(type(a))'''

#while loop()
'''a=10
while a>1:
    print(a)'''
#it will print upto 2
'''a=10
while a>1:
    print(a)
    a=a-1'''
#it will print upto 1

'''a=10
while a>=1:
    print(a)
    a=a-1'''

#it will print 20 to 6 at increasing order

'''a=20
while a>6:
    print(a)
    a=a-1'''

#if last digit

'''a=10
while a>=1:
    a=a-1
print(a)'''

#along with zero
'''a=10
while a>=1:
    a=a-1
    print(a)'''
#increasment
'''a=6
while a<20:
    print(a)
    a+=1'''
#decreasment to stop the iteration we have to keep lower number in a and higher number at condition

'''a=8
while a<20:
    print(a)
    a+=1'''
#infinity variable must have highest number and condition have highest numbertha it will grow infity


'''a=20
while a>6:
    print(a)
    a+=1'''

    
#range(): the range function return a sequence of number ,starting from "0" by default and
#increment one by on and stop before a specific number
#start-stop-step

#stop (if we give only one number it will consider as stop)
'''for i in range (10):
    print(i)'''
'''#start-stop
for i in range(0,10):
    print(i)
#step with range function

for i in range(0,28,3):
    print(i,end=",")'''

#student marks
while True:
    a=int(input("enter the marks:"))
    if a in range(91,101):
        print("A-Grade")
    elif a in range (81,91):
        print("B-Grade")
    elif a in range (71,61):
        print("C-Grade")
    elif a in range (61,71):
        print("D-Grade")
    else:
        print("Fail")


     








    











    
