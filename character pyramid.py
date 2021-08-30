'''input:--
output:-
        A  
       B C
      D E F  
     G H I J
    K L M N O 
description:character Pyramid pattern
date: 30-08-2021
Author name: Shruti Nahar'''
x=5
n=65
m=(2*x)-2
for i in range(0,x):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print(chr(n),end=' ')
        n=n+1
    print(" ")