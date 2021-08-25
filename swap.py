'''input:
enter value of a10
enter value of b20
output:-
before swapping
a= 10
b= 20
After swapping
a= 20
b= 10
description: Logic to swap two numbers using third variable 
date: 25-08-2021
Author name: Shruti Nahar'''
def  swap(a,b):
     print("before swapping")
     print("a=",a)
     print("b=",b)
     print("After swapping")
     temp=a
     a=b
     b=temp
     print("a=",a)
     print("b=",b)
a=int(input("enter value of a"))
b=int(input("enter value of b"))
swap(a,b)


     
     

