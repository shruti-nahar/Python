'''input:- --
output:-
1
3
5
7
9
11
13
15
17
19
description: Continue statement to print odd numbers till range
date: 27-08-2021
Author name: Shruti Nahar'''

for x in range(20):
   
    if(x%2==0):
        continue
    print(x)