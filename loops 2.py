#Break:the break statment is used to terminate the enter loop the continue statment is skips the correct iteration
#and rest of the code will continue...\

#pass:a pass is a null statment it does nothing,but syntaxically we need...\

#break

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''
#as the print is outside the loop than it will print the last digit 
'''a=20
while a>5:
    a=a-1
    if a==10:
        break
print(a)'''

#it will print upto 6 but there is break statment at 8 so it print upto 9
'''a=20
while a>5:
    print(a)
    a=a-1
    if a==8:
        break'''

#it actually print upto 0 to 19 but now it will stop at 5
'''for i in range(20):
    if i==3:
        break
    print(i)'''

#it will work on strings also

'''a="python"
for i in a:
    if i=='h':
        break
    print(i)'''

#continue
'''a=30
while a>10:
    a=a-1
    if a==19:
        continue
    print(a)'''

'''a=40
while a>15:
    a=a-1
    if a==25:
        continue
    print(a)'''

'''for i in range (25):
    if i==17:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''

#pass
'''a=15
while a>10:
    print(a)
    a=a-1
    if a==14:
        pass'''
'''for i in  range(20):
    if i==15:
        pass
    print(i)'''
#break and continue
'''for i in range(1, 11):

    if i == 3:
        continue

    if i == 8:
        break

    print(i)'''

#student details
'''no_stu=int(input("no:of studuent:"))
absent=0
present=0
for i in range(no_stu):
    s=input(f"the student are absent or present{i+1}")
    if s=='a':
      absent+=1
    if s=="p":
       present+=1
          
print("absent:",absent)
print("presnt:",present)
print("total:",s)'''
a=int(input())
for a in range(1,n+1):
    print('*'*n)

    
    
