#function: a function is a block of organized,resuable code and that is used to perform a single or multiple taste,
#python gives inbulit functions like print,you can make your own function also and called user
#are called defined function

#fun blocks begin with the keyword"def" followed by the'fun name' and (())

#normal of writing code
'''a=10
b=10
print("sum:",a+b)
print("sub:",a-b)
print("multiplication:",a*b)
a=100
b=200
print("sum:",a+b)
print("sub:",a-b)
print("multiplication:",a*b)'''

#the difference between the funvtions and normal code is we can asscess the code mutlipul times by writing one function 
'''def cal(a,b):
    print("sum:",a+b)
    print("sub:",a-b)
    print("multiplication:",a*b)
cal(10,20)
cal(100,200)
cal(1,89)'''

'''def cal(a,b):
    print("sum:",a+b)
    print("sub:",a-b)
    print("multiplication:",a*b)
    print("division:",a//b)
    print("power:",a**b)
    print("modulus:",a%b)
cal(10,20)'''

#user define
'''def add():
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    print(a+b)
add()'''

#by using while Ture function we cand asses data easily
'''while True:
    def add():
        a=int(input("enter the value:"))
        b=int(input("enter the value:"))
        print(a+b)
    add()'''
#recurrsion fun :it is function is called by it self is called recurrsion
'''def add():
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    print(a+b)
    add()
add()'''

#adding the last name and full name

'''def fullname():
    fname=input("data:")
    lname=input("data:")
    print((fname+" "+lname).title())
fullname()'''

#difference between the return and print
#print just shows the human user input in a console
#return will terminate the function and gives back a value in the function
