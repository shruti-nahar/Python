'''input:--
output:-
A  
B C  
D E F
G H I J
K L M N O
description:character right half Pyramid pattern
date: 30-08-2021
Author name: Shruti Nahar'''
x=5
n=65
for i in range(0,x):
    for j in range(0,i+1):
        print(chr(n),end=' ')
        n=n+1
    print(" ")
    