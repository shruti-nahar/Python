'''input:- Enter the Number 10
output:-Even Number
description: Check whether the number is even or odd 
date: 27-08-2021
Author name: Shruti Nahar'''

num=int(input("Enter the Number "))
if(num%2==0):
    print("Even Number")
elif(num% 2!= 0):
    print("Odd Number ")
else:
    print("Try Again")