'''input:- madam
output:-Palidrome
description: Check the string is palidrome or not
Date: 27-08-2021
Author name: Shruti Nahar'''
def palidrome(num):
    x=num[::-1]
    if(x==num):
        print("Palidrome")
    else:
        print("Not a Palidrome ")
palidrome("madam ")
