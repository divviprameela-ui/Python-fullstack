#vote

a=int(input("enter the age"))
if a>=18:
    print("eligible for vote")
else:
    print("not eligible")
#even or odd
num=int(input("enter the value:"))
if num%2==0:
    print("it is even number")
else:
    print("it is odd number")

#leap year
year=int(input("data:"))
if (year%4==0):
    print("it is a leap year")
else:
    print("it is not a leap year")
    
#guess code
name=input("data:")
if (name=="sri vidya"):
    print("welcome:sri vidya")
else:
    print("welcome guess")

#vowels

'''letter=input("character:")
if (letter=='a'):
    print("it is vowel")
    if(letter=='e'):
        print("it is vowel")
    if (letter=='i'):
        print("it is vowel")
    if (letter=='o'):
        print("it is vowel")
    if (letter=='u'):
        print("it is vowel")
    
else:
    print("it is not vowel")'''

letter=input("character:")
if (letter=='a','e','i','o','u'):
    print("it is vowel")
    
else:
    print("it is not vowel")

