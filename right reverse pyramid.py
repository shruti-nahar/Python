'''input:--
output:-
* * * * * *

* * * * *

* * * *

* * *

* *

*
description:Implementation of global and local variable
date: 03-09-2021
Author name: Shruti Nahar'''
def pattern(n):
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("*",end=' ')
        print("\n")
pattern(10)