#gobal &local variable:
#defination:variables in side and out side the funcation is called gobal and local variables
#a variable define up the funaction and is excessable to the entire gobal space is call gobal variable
#a variable is define inside the function is called local variable

#it is just created only one variable outside that is the reason why it is assgned for both the gobal and local varibale
'''a=3
def check():
    print("inside the value is",a)
check()
print("outside value is :",a)'''

#if we created two variables one is gobal and local so the variable which is at in side will asssign with inside part and
#the variable which is craeted outside will assign to the outside variable gobal variable

'''a=2
def check1():
    a=9
    a=a**2
    print("inside value is:",a)
check1()
print("outside value is:",a)'''

#we can add more variable in the function the variable which is declared one time will be aa local variable and next thing is
#the insight value is only addigned to the inside variable not for outside
#in this case it will raise error because b value is not declared outside so uotsie b value is not
#defined but inside value also cant assigned
'''a=1
def check2():
     a=2
     a=9
     print("inside value is:",a)
     b=6
     b=b+a
     print("update value is :",b)
check2()
print("outside value is:",a)
print("outside value of b is:",b)'''

#for retifing the above error we have create one b variable outside the function

'''a=1
b=8
def check2():
     a=2
     a=9
     print("inside value is:",a)
     b=6
     b=b+a
     print("update value is :",b)
check2()
print("outside value is:",a)
print("outside value of b is:",b)'''

#usage of gobal keyword: when user want to acces the gobal variable inside
#the function directly and carry forward the updated value even outside the function
#than we need to use gobal variable..

#final case of both gobal and local variable
'''a=9
def check3():
    global a
    print("inside value is :",a)
    a=5
    print("updated value is:",a)
    global b
    b=2
    b=b+a
    print("b value is :",b)
check3()
print("value of a is:",a)
print("value of b is:",b)'''

#we can also write it as
a=9
def check3():
    global a,b
    print("inside value is :",a)
    a=5
    print("updated value is:",a)
    b=2
    b=b+a
    print("b value is :",b)
check3()
print("value of a is:",a)
print("value of b is:",b)
