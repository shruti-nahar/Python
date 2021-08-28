'''input:--
output:- 
*  
* *  
* * *
* * * *
* * * * *
description:right half Star Pyramid 
date: 28-08-2021
Author name: Shruti Nahar'''
x=5
m=(2*x)-2
for i in range(0,x):
    for j in range(0,m):
        print(end="")
    m=m-1
    for j in range(0,i+1):
        print("*",end=' ')
    print(" ")