''''
INPUT:-
OUTPUT:-
1
10
inside c1 is 11
99
in main 99
DESCRIPTION:-Implementation of global variable
DATE:1-09-2021
AUTHOR NAME:-SHRUTI NAHAR
'''
c=1
def add():
    print(c)
add()
c1=10
print(c1)
def add1():
    
    global c1
    c1=9
    c1=c1+2
    print("inside c1 is",c1)
    c1=99
    print(c1)
add1()
print("in main",c1)
    
