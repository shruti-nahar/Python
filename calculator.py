'''input:1.ADD 
       2.SUB
       3.MUL
       4.DIV
       5.SIMPLE INTEREST
       6.COMPOUND INTEREST
       7.SQUARE
       8.SQUAREROOT
       Enter the choice 5
output:Simple Interest  1000.0
description:Use of Function to perform Arithmetic Operation
date: 24-08-2021
Author name: Shruti Nahar'''
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2
 
def si(p,r,t):
    return (p*r*t)/100

def ci(p,r,t):
    return p * pow((1+r/100),t)

def sqr(num):
    return num**2

def st(num):
    return num**0.5

print("1.ADD \n2.SUB \n3.MUL \n4.DIV \n5.SIMPLE INTEREST \n6.COMPOUND INTEREST \n7.SQUARE \n8.SQUAREROOT ")
num=int(input("Enter the choice "))

if(num==1):
    print("Addition is ",add(10,20))
    
elif (num==2):
        print("Substraction is ",sub(20,10))
elif(num==3):
        print("Multiplication is ",mul(10,5))
elif(num==4):
        print("Division is ",div(10,2))
elif(num==5):
        print("Simple Interest ",si(10000,2,5))
elif(num==6):
        print("Compound Interest is ",ci(2000,4,6))
elif(num==7):
        print("Square is ",sqr(4))
elif(num==8):
        print("Square root is ",st(36))