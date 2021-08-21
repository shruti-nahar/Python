#input:10
#output:0 1 1 2 3 5 8 13 21 34
#description:Fibnocii series using function
#date: 21-08-2021
#Author name: Shruti Nahar
def fibo(n):
    a=0
    b=1
    print(a,"\n")
    print(b,"\n")
    for x in range(n-2):
        c=a+b
        print(c,"\n")
        a=b
        b=c
    return c
num=int(input("Enter the number "))
fibo(num)