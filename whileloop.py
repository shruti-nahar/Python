'''Input:-Enter the value 10
output:-Addition is  55
description:Find the addition of number till n
date: 26-08-2021
Author name: Shruti Nahar'''
num=int(input("Enter the value "))  
if(num<=0):
     print("Enter a valid value ")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
print("Addition is ",sum)
