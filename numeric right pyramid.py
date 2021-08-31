'''input:--
output:- 
1  
2 3  
4 5 6  
7 8 9 10        
11 12 13 14 15  
description:numeric Pyramid pattern
date: 31-08-2021
Author name: Shruti Nahar'''
x=5
n=1
for i in range(0,x):
    for j in range(0,i+1):
        print(n,end=' ')
        n=n+1
    print(" ")